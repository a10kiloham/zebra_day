import os
import sys
import socket
import datetime
import json
import requests


def get_current_date():
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%Y-%m-%d")
    return formatted_date

def send_zpl_code(zpl_code, printer_ip, printer_port=9100):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timeout = 5
    sock.settimeout(timeout)

    try:
        # Connect to the printer
        sock.connect((printer_ip, printer_port))

        # Send the ZPL code as raw bytes
        sock.sendall(zpl_code.encode())
        print("ZPL code sent successfully to the printer!")

    except ConnectionError as e:
        print(f"Error connecting to the printer: {e}")

    finally:
        # Close the socket connection
        sock.close()


class zpl:

    def __init__(self, debug=0):
        self.load_printer_json()
        self.debug = False if debug in [0,'0'] else True


    def probe_zebra_printers_add_to_printers_json(self, ip_stub="192.168.1", scan_wait="0.25",lab="scan-results"):
        
        if lab not in self.printers['labs']:
            self.printers['labs'][lab] = {}

        self.printers['labs'][lab]["Download-Label-png"] = { "ip_address": "dl_png", "label_zpl_styles": ["test_2inX1in"],"print_method": "generate png"}

        res = os.popen(f"bin/scan_for_networed_zebra_printers_curl.sh {ip_stub} {scan_wait}")
        for i in res.readlines():
            ii = i.rstrip()
            sl = ii.split('|')
            if len(sl) > 1:
                zp = sl[0]
                ip = sl[1]
                model = sl[2]
                serial = sl[3]
                status = sl[4]                
                if ip not in self.printers['labs'][lab]:
                    self.printers['labs'][lab][ip] = {"ip_address" : ip, "label_zpl_styles" : ["blank_0inX0in", "test_2inX1in","tube_2inX1in", "plate_1inX0.25in", "tube_2inX0.3in"], "print_method" : "unk"}  # The label formats set here are the installed defaults

        self.save_printer_json()


        
    # USING SELF.PRINTERS
    def save_printer_json(self, json_filename="etc/printer_config.json"):
        with open(json_filename, 'w') as json_file:
            json.dump(self.printers, json_file, indent=4)
        self.load_printer_json(json_filename)
        
            
    def load_printer_json(self, json_file="etc/printer_config.json"):
        fh = open(json_file)
        self.printers_filename = json_file
        self.printers = json.load(fh)

        
    def clear_printers_json(self, json_file="etc/printer_config.json"):
        os.system(f"""echo '{{"labs" : {{}} }}' > {json_file}""")
        fh = open(json_file)
        self.printers_filename = json_file
        self.printers = json.load(fh)
        
        
    def replace_printer_json_from_template(self):
        os.system('cp etc/printer_config.template.json etc/printer_config.json')


    def get_valid_label_styles_for_lab(self,lab=None):
        unique_labels = set()

        for printer in self.printers['labs'][lab]:
            for style in self.printers['labs'][lab][printer]['label_zpl_styles']:
                unique_labels.add(style)

        result = list(unique_labels)
        return result

    
    def formulate_zpl(self,uid_barcode=None, uid_human_readable=None, alt_a=None, alt_b=None, alt_c=None, alt_d=None, alt_e=None, alt_f=None, label_zpl_style=None):

        zpl_file = f"etc/label_styles/{label_zpl_style}.zpl"
        if not os.path.exists(zpl_file):
            raise Exception(f"ZPL File : {zpl_file} does not exist.")

        with open(zpl_file, 'r') as file:
            content = file.read()
        zpl_string = content.format(uid_barcode=uid_barcode, uid_human_readable=uid_human_readable,alt_a=alt_a, alt_b=alt_b, alt_c=alt_c, alt_d=alt_d, alt_e=alt_e, alt_f=alt_f, label_zpl_style=label_zpl_style)

        return zpl_string

    
    def generate_label_png(self,zpl_string=None, png_fn=None):

        if zpl_string in [None] or png_fn in [None]:
            raise Exception('ERROR: zpl_string and png_fn may not be None.')
        
        # Labelary API URL                                                                                          
        labelary_url = "http://api.labelary.com/v1/printers/8dpmm/labels/4x6/0/"

        # Create a POST request to the Labelary API                                                                 
        response = requests.post(labelary_url, data=zpl_string)

        # Check if the request was successful                                                                       
        if response.status_code == 200:
            # Save the image to a file                                                                              
            with open(png_fn, "wb") as f:
                f.write(response.content)
                print(f"Image saved as {png_fn}")
        else:
            print(f"Failed to convert ZPL to image. Status code: {response.status_code}")

        return png_fn
    
            
    def print_zpl(self, lab=None, printer_name=None, uid_barcode='', uid_human_readable='', alt_a='', alt_b='', alt_c='', alt_d='', alt_e='', alt_f='', label_zpl_style=None):
        rec_date = str(datetime.datetime.now()).replace(' ','_')
        
        if label_zpl_style in [None,'','None']:
            label_zpl_style = self.printers['labs'][lab][printer_name]['label_zpl_styles'][0]  # If a style is not specified, assume the first
        elif label_zpl_style not in self.printers['labs'][lab][printer_name]['label_zpl_styles']:
            print(f"\n\nWARNING:::\nZPL style: {label_zpl_style} is not valid for {lab} {printer_name} ... {self.printers['labs'][lab][printer_name]['label_zpl_styles']}")

        printer_ip = self.printers['labs'][lab][printer_name]["ip_address"]

        zpl_string = self.formulate_zpl(uid_barcode=uid_barcode, uid_human_readable=uid_human_readable, alt_a=alt_a, alt_b=alt_b, alt_c=alt_c, alt_d=alt_d, alt_e=alt_e, alt_f=alt_f, label_zpl_style=label_zpl_style)

        ret_s = None
        if printer_ip in ['dl_png']:
            png_fn = f"files/zpl_label_{label_zpl_style}_{rec_date}.png"
            ret_s = self.generate_label_png(zpl_string, png_fn)
            
        else:
            send_zpl_code(zpl_string, printer_ip)
            ret_s = zpl_string
            
        if self.debug:
            print(f"\nZPL STRING  :: {zpl_string}\n")

        return ret_s
