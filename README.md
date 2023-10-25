<img src=zebra_day/imgs/bar_red.png>

## zebra_day Overview [v0.0.26 - very beta](https://github.com/Daylily-Informatics/zebra_day/releases/tag/v0.0.26)
<ul>

#### For The Impatient
* Verify there are zebra printers connected & powered up to the same network that the PC you are installing this s/w to is connected.
```bash
python --version  # should be 3.10*  # advisable to run in some kind of venv

pip install zebra_day

echo 'load a fresh env'  # sometimes a package installed with pip will not be visible until the env refreshes.

zday_quickstart  # will do some network scanning for available zebra printers, and launch the web UI.
```

### It Is 3+ Things

  (1) Zebra Printer Management & Configuration

  (2) ZPL Label Template Tools

  (3) A Python Library To Manage Formulating & Sending Label Print Requests

  (bonuses)
    * a web gui to make some of the above more approachable && expose (3) as a http API.
    * Documentation sufficent for organization to successfuly assemble & deploy a reasonalbly sized barcoding system in your operational environment in potentially weeks.
      * ... and cheaply! a 10 printer install could cost ~$5,000.00 in purchases.  With ongoing operational expenses of ~$150/mo (depends on label stock consumption mostly).

### And It Is Not

* _An Identify Generating Authority_
  * you will need to produce your own UID/GUID/etc. This can be manual, spreadsheets, custom code, various RDBMS, LIMS systems, Salesforce... but should not be tangled in this package.
    * also, METADATA regaring your UID is important as these metadata can be presented on the labels in addition to the human readable and scannable representation of the provided UID. [Unique Identifier Maxims](zebra_day/docs/uid_screed_light.md).

</ul>

## Getting Started

<ul>
  
### Facilitated :: Daylily Orchestrated Build and Deploy ( deliverable in ~1month )
* [Daylily is available to lead or contribute to the building and deployment of universal barcoding systems to your organizations operations](https://www.linkedin.com/in/john--major/). Daylily offers expertise with the entire process from evaluating existing operations systems, proposing integration options, securing all hardware, deploying hardware and software, and importantly: connecting newly deployed barcoding services to other LIS systems.

#### Universal Barcoding Capability Project Timing Estimates

<ul>
<ul>
  
> <img src=zebra_day/imgs/UBC_gantt_chart.png height=200 width=450>

</ul>
</ul>

### Requirements
* Tested and runs on MAC and Ubuntu (but other flavors of Linux should be no problem). Windows would be a rather large hassle, though presumably possible.
* [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation) and [mamba](https://anaconda.org/conda-forge/mamba) installed. This is not, in fact, a blocking requirement, but other env setups have not been tested yet.  __for MAC users, it may be advisable to install conda with homebrew__.
  * create conda environment `ZDAY`, which will be used to run the UI
    ```bash
    mamba create -n ZDAY -c conda-forge python==3.10 pip ipython
    ```

### Install From PIP 
you can pip install `zebra_day` to any python environment running 3.10.*.  If you plan to run the web UI or use the HTTP API functionality, run this in the above described `ZDAY` conda env.  To install with pip:

```bash
pip install zebra_day
```
* reload your environment/shell.


### Install From Source

#### Clone Repository & Local PIP

*  [From github via ssh](https://github.com/Daylily-Informatics/zebra_day)

```bash
git clone git@github.com:Daylily-Informatics/zebra_day.git
cd zebra_day
conda activate ZDAY  # ZDAY was built with mamba earlier
python setup.py sdist
pip install dist/PATH_TO_HIGHEST_VERSIONED_FILE.tar.gz
```

* `zebra_day` is now installed in your current python environment.
* reload your environment/shell.

<br><br><br>

</ul>


## Hardware Config
### Quick
* Connect all zebra printers to the same network the machine you'll be running `zebra_day` is connected to. Load labels, power printerson, confirm status lights are green.

### [Hardware Config Guide](zebra_day/docs/hardware_config_guide.md)
<br><br>

</ul>

<img src=zebra_day/imgs/bar_purp3.png>

# USAGE

<ul>

## QUICKSTART
* zebra printers -> power on and connect via cable or wifi to the same network the machine you installed `zebra_day` is on.
* activate the environment you have `zebra_day` installed into.
* If you have just pip installed `zebra_day` in the shell you are in, start a new shell.
* run `zday_quickstart`, which will detect you IP address, scan the detected network for zebra printers, build a printer fleet config for printers detected, and launch the `zebra_day` web gui (the IP:port will be printed for you if the launch succeeds, open the IP:port in a web browser with visibility to the IP).

### Example Output From `zday_quickstart`
<pre>

zday_quickstart

(ip addr show | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1' || ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1') 2> /dev/null

IP detected: 192.168.1.12 ... using IP root: 192.168.1

 ..... now scanning for zebra printers on this network (which may take a few minutes...

Zebra Printer Scan Complete.  Results:{'labs': {'scan-results': {'Download-Label-png': {'ip_address': 'dl_png', 'label_zpl_styles': ['test_2inX1in'], 'print_method': 'generate png', 'model': 'na', 'serial': 'na'}, '192.168.1.7': {'ip_address': '192.168.1.7', 'label_zpl_styles': ['blank_0inX0in', 'test_2inX1in', 'tube_2inX1in', 'plate_1inX0.25in', 'tube_2inX0.3in'], 'print_method': 'unk', 'model': 'ZTC GX420d', 'serial': 'ZBR7563510 '}}}}

Now starting zebra_day web GUI


     	       **** THE ZDAY WEB GUI WILL BE ACCESSIBLE VIA THE URL: 192.168.1.12:8118

               The zday web server will continue running, and not return this shell to a command prompt until it is shut down

               .... you may shut down this web service by hitting ctrl+c.


(ip addr show | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1' || ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1') 2>/dev/null
[24/Oct/2023:00:45:51] ENGINE Listening for SIGTERM.
[24/Oct/2023:00:45:51] ENGINE Listening for SIGHUP.
[24/Oct/2023:00:45:51] ENGINE Listening for SIGUSR1.
[24/Oct/2023:00:45:51] ENGINE Bus STARTING
CherryPy Checker:
The Application mounted at '' has an empty config.

[24/Oct/2023:00:45:51] ENGINE Started monitor thread 'Autoreloader'.
[24/Oct/2023:00:45:51] ENGINE Serving on http://0.0.0.0:8118
[24/Oct/2023:00:45:51] ENGINE Bus STARTED
</pre>

  > If `zday_quickstart` ends with `ENGINE Bus STARTED` and does not return the cursor, the web service is running (and will continue to do so until you ctrl+c in the shell it is running in.  From a web browser, navigate to the URL printed in the quickstart STDOUT, in the above, this would be `192.168.1.12:8118`.

#### zebra_day Web GUI Launched From `zday_quickstart`

> The `zebra_day` web gui will look like this:  <img src=zebra_day/imgs/zday_quick_gui.png>

<br><br>
  

## Programatic
### Quick
Open an ipython shell.

```python
import zebra_day.print_mgr as zdpm

zlab = zdpm.zplo()  ## !!! NOTE (see note below) NOTE !!!
## !!! NOTE !!! due to something I have not yet sorted out with my pypy packaging, instantiating the print_mgr.zpl() class directly does not allow the class to see its package data files.  This hack solves the problem and returns you the same behaving object.


zlab.probe_zebra_printers_add_to_printers_json('192.168.1')  # REPLACE the IP stub with the correct value for your network. This may take a few min to run.  !! This command is not required if you've sucessuflly run the quickstart already, also, won't hurt.

print(zlab.printers)  # This should print out the json dict of all detected zebra printers. An empty dict, {}, is a failure of autodetection, and manual creation of the json file may be needed. If successful, the lab name assigned is 'scan-results', this may be edited latter.
# The json will loook something like this
## {'labs': {'scan-results': {'192.168.1.7': {'ip_address': '192.168.1.7', 'label_zpl_styles': ['test_2inX1in'], 'print_method': 'unk'}}}
##               'lab' name     'printer' name(can be edited latter)                              label_zpl_style

# Assuming a printer was detected, send a test print request.  Using the 'lab', 'printer' and 'label_zpl_style' above (you'd have your own IP/Name, other values should remain the same for now.  There are multiple label ZPL formats available, the test_2inX1in is for quick testing & only formats in the two UID values specified.

zlab.print_zpl(lab='scan-results', printer_name='192.168.1.7', label_zpl_style='test_2inX1in', uid_barcode="123aUID")
# ZPL code sent successfully to the printer!
# Out[13]: '^XA\n^FO235,20\n^BY1\n^B3N,N,40,N,N\n^FD123aUID^FS\n^FO235,70\n^ADN,30,20\n^FD123aUID^FS\n^FO235,115\n^ADN,25,12\n^FDalt_a^FS\n^FO235,145\n^ADN,25,12\n^FDalt_b^FS\n^FO70,180\n^FO235,170\n^ADN,30,20\n^FDalt_c^FS\n^FO490,180\n^ADN,25,12\n^FDalt_d^FS\n^XZ'
```

* This will produce a label which looks like this (modulo printer config items needing attention).
  ![test_lab](zebra_day/imgs/quick_start_test_label2.png)


### [Programatic Guide](zebra_day/docs/programatic_guide.md)


<br><br>



## Web UI

### Quick Start
* Start the `zebra_day` service.  The current network security for this service is minimal, as such, running this so it is fully visible to the public internet is no advised. Within a local network, or on a well configured AWS(etc) host is fine.

```bash
# consider running this via tmux or screen
conda activate ZDAY # or any python environment where you have pip installed zebra_day (from pypy or local pip)
python zebra_day/bin/zserve.py  # This service will continue running until stopped or until it crashes. Access and error logs are printed to STDout/err.

# ctrl-c to shutdown the web service

```

* The web UI should now be accessible at `YOUR.HOST.IP.ADDR:8118`, or if physically on the box you're running the service on, `localhost:8118`.
  * Unreachable?  Are the ports open?  Is the python cherrypy service started above still running, or has it exited?

* You can send a label print request via the UI (the process is a little involved ATM)... also, you can send the service requests via HTTP, ie, the programatic print request from above, can be similarly accomplished with this URL

```http
http://YOUR.HOST.IP.ADDR:8118/_print_label?lab=scan-results&printer=192.168.1.7&printer_ip=192.168.1.7&label_zpl_style=test_2inX1in&uid_barcode=123aUID&alt_a=&alt_b=&alt_c=&alt_d=&alt_e=&alt_f=
```

_or_ with the unused (in this ZPL template!) fields removed, this URL

```http
http://YOUR.HOST.IP.ADDR:8118/_print_label?lab=scan-results&printer=192.168.1.7&label_zpl_style=test_2inX1in&uid_barcode=123aUID
```

* There will be more details on the web tools available via this GUI in the `Web UI Guide`.

### [Web UI Guide](zebra_day/docs/zebra_day_ui_guide.md)


<br><br>

</ul>
<img src=zebra_day/imgs/bar_red.png>

# Other Topics

## Security
### Secrets
No credentials of any kind are stored or used by `zebra_day`. It solely offers zebra printer management and label print request formatting and brokering services.  It does not need to know how to connect to other systems, other systems will use the library code provided here, or the http api.

### Host and Network Security
In it's present state, `zebra_day` is safe to run on a machine located in a properly configured & secure local network or cloud hosted instance residing in a secure VPN/VPC.
  * `zebra_day` should not be deployed in such a way the host is fully visible to the public internet.
    * a potential exception would be exposing the service via an encryped and secure open port. __POC demonstrating this concept can be found below__.
    
### Programatic Use Of `zebra_day` Package/Library
Using the python library in other python code poses no particularly unique new risk. `zebra_day` may be treated similarly to how other third party tools are handled in each users organization.

## Regulatory & Compliance
### HIPAA / CAP / CLIA
No PHI is needed by `zebra_day` to function.  PHI may be sent in print rquests, each organization will have their own use cases. `zebra_day` does not store any of the print request metadata sent to it, the info is redirected to the appropriate zebra printer, and that is that.  It is straightforward when setting up the host machine/environment this package will be running in to check off the various HIPAA and CAP/CLIA expectations where they apply.


## Hardware

### Zebra Printers
* Printers will need to be able to secure an IP address either via a wired connection or via wireless.  The printers will need to be visible to the machine running this package in order to accept print requests. Further, there are tools to scan the local network and identify Zebra Printers. Identified printers are automatically configured for use by `zebra_day`.

  * Network attached printers should be able to run w/out any connection to a PC/laptop. This affors much greater flexibility in placing print stations. In fact, `zebra_day` does not communicate with USB only printers.
* The below zebra printer models have been tested, but any zebra printer able to obtain an IP address and accept `ZPL` should also work.
* _IMPORTANT_, The initial configuration of zebra printers can be a little gnarly. I intend to add some notes on this topic soon. In the mean time, the GUI printer status report includes links to access the web server admin utility each zebra printer exposes.
  * the printer admin UIs all use the default un/pw: `admin/1234`.
    * The first thing I suggest when setting up a new printer is resetting the factory defaults - doable via the zebra printer admin UIs.
  * Wired ethernet connections are advised for greater robustness.  Configure the wired network settings to obtain an IP automatically.  ask your network admins to set DNS rules which will assign the same IP to each printer.  You'll need to supply the printer MAC address to do this, which you can find on via each printers admin UI.
    * __NOTE__ Sometimes these printers can not seem to obtain an IP with DHCP, this could be a router/hub issue, but sometimes you'll need to set the printer to a static IP.  This can be done via the printer admin UI. If the network config is saved with an error, you'll now need to connect to the printer via USB to reset (there might be a button seuquece cycle which can be hit to factory reset...).
    * Wireless setup is _SUPER_ fussy. You'll need to know precisely what bands your router is running on, and the precise auth used. This can be done via the zebra printer admin UI, or when connected via a USB cable to a computer running a driver config program(not advised really).
  * Next, you may have to mess around with calibration settings for label width and length.
  * I have used this driver/config tool on a MAC when I have needed to connect to a printer via `USB`, [Peninsula Zebra Printer Driver](https://www.peninsula-group.com/install-zebra-printer-mac-osx/install-zebra-printer-mac-osx.html). I'm fairly sure there are several windows options.


#### GX420d - wired, no LCD screen

These printers are NOT reccomended b/c the lack of LCD screen makes them a pain to configure.  You will probably need to connect via USB to set good initial settings.  If you have the `zebra_day` UI running, try connecting the printer to the network and powering on, then run the zebra printer network scan.  If the printer is discovered, you're in luck and can admin it via the UI on the printer.

* [Available From Amazon](https://www.amazon.com/gp/product/B07KCQ67Y1/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* Cost per printer : `$264.00`
* [manual]()

#### GX420d - wired, with LCD screen
These are solid, but aging out and not as easy to find for sale.

* [Available From Amazon](https://www.amazon.com/gp/product/B011Q95XX2/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* Cost per printer : `$425.00`
* [manual]()


#### ZD620d - wired and wireless, with color LCD screen
These are solid, but aging out and not as easy to find for sale.

* [Available From Amazon](https://www.amazon.com/gp/product/B07VHDR33Z/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* Cost per printer : `$331.00`
* [manual]()

#### Zebra QLn420 Direct Thermal Printer - Monochrome - Portable 

* [Amazon](https://www.amazon.com/dp/B084P4KBWS?psc=1&ref=ppx_yo2ov_dt_b_product_details)
* Cost per printer : `$136`
* [manual]()

#### Zebra - ZD620d Direct Thermal Desktop Printer with LCD Screen - Print Width 4 in - 203 dpi - Interface: WiFi, Bluetooth, USB, Serial, Ethernet - ZD62142-D01L01EZ

* [Amazon](https://www.amazon.com/dp/B07VHDR33Z?psc=1&ref=ppx_yo2ov_dt_b_product_details)
* Cost per printer : `$331`
* [manual]()


#### Zebra ZD620t Thermal Transfer Desktop Printer 203 dpi Print Width 4 in Ethernet Serial USB ZD62042
<font color=magenta>note, this is a thermal transfer printer & requires ribbons to print</font>
* [Amazon](https://www.amazon.com/dp/B08PW6ZRL6?psc=1&ref=ppx_yo2ov_dt_b_product_details)
* Cost per printer : `$500`
* [manual]()

### Thermal Transfer Ribbons
Also require distinct label stock from the direct thermal transfer printer labels.

* [Amazon](https://www.amazon.com/dp/B07FX3PJ2M?psc=1&ref=ppx_yo2ov_dt_b_product_details)
* Cost per roll: `$7`


### Label Stock
The `zebra_day` code can easily manage a printer fleet comprised of different printing mechanism.

#### Direct Thermal Transfer Labels
Require no ribbon, cheaper, can be less robust in some situations, speciality use case label stock mfgs are numerous.

##### Aegis Direct Thermal Labels
For general purpose use. Very inexpensive and easy to source.

###### 2in x 1in
Good for paperwork, some larger tubes.

* [Available On Amazon](https://www.amazon.com/gp/product/B01GJGC2OK/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1)
* Cost per roll : `$3.21`

###### 2in x 0.5in
Good for smaller tubes, or tubes that already have space taken up by labels.

* [Available On Amazon](https://www.amazon.com/gp/product/B098Z8JYZC/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1)
* Cost per roll : `$3.25`

##### Labtag

###### 2in x 1in


###### plate style

###### small tube w/dot

#### Thermal Transfer
These labels requier ribons to print. Per-label are more expensive, more robust, but can be prone to smudging.


### Barcode Scanners

#### Tera 1d, 2d, QR  scanner. Corded and bluetooth and wireless
Programable and well supported/adopted.

* [Available From Amazon](https://www.amazon.com/dp/B0953FJZDG?psc=1&ref=ppx_yo2ov_dt_b_product_details)
* Cost per scanner : `$63.00`

#### Tera Mini 1d 2d QR. Corded and wireless and bluetooth.
_experimenting_... tiny handheld pretty well behaving non-corded scanner.

* [Available From Amazon](https://www.amazon.com/dp/B08NDFWFKJ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
* Cost per Scanner : `$38.00`


# Exploration With A Few Integration Approaches

# Send Label Print Requests From Public Internet To Host PC w/In Your Private Network

## Ditch The Private Local Network & Expose Server Publicly ( not advised )
...

## Using NGROK To Present A Tunneled Port Connected To The `zebra_day` Host Port (up and running in <5 min!)

* Create a tunnel to connect to the zebra_day service running on a machine within your network on port 8118.  This could be a cloud instance w/in a VPC you control, or a machine physically present w/in your network.

* [NGROK DOCS]( https://dashboard.ngrok.com/get-started/setup/macos)

### Install ngrok

```bash
brew install ngrok/ngrok/ngrok
ngrok config add-authtoken MYTOKEN  # you get this once registered (its free!)
```

### Running ngrok
```bash
ngrok http 8118
```

Which starts a tunnel and presents a monitoring dashboard.  And it looks like this:
<pre>
ngrok                                                                                (Ctrl+C to quit)
                                                                                                     
Introducing Always-On Global Server Load Balancer: https://ngrok.com/r/gslb                          
                                                                                                     
Session Status                online                                                                 
Account                       USERNAME (Plan: Free)                                      
Version                       3.3.5                                                                  
Region                        United States (California) (us-cal-1)                                  
Latency                       12ms                                                                   
Web Interface                 http://127.0.0.1:4040                                                  
Forwarding                    https://dfbf-23-93-175-197.ngrok-free.app -> http://localhost:8118

Connections                   ttl     opn     rt1     rt5     p50     p90
                              8       0       0.00    0.01    10.03   28.05

HTTP Requests
-------------

GET /_print_label              200 OK
GET /_print_label              200 OK
GET /build_print_request       200 OK
GET /send_print_request        200 OK
GET /                          200 OK
GET /_print_label              200 OK
GET /_print_label              200 OK
GET /build_print_request       200 OK
GET /send_print_request        200 OK
GET /favicon.ico               200 OK        ~
</pre>

And looks like:
<img src=zebra_day/imgs/ngrok.png>

* If you leave the ngrok tunnel running, go to a different network, you can use the link named in the `Forwarding` row above to access the zebra_day UI, in the above example, this url would be `https://dfbf-23-93-175-197.ngrok-free.app`.

#### Sending Label Print Requests
##### from a web browser on a different network

`https://dfbf-23-93-175-197.ngrok-free.app/_print_label?uid_barcode=UID33344455&alt_a=altTEXTAA&alt_b=altTEXTBB&alt_c=altTEXTCC&alt_d=&alt_e=&alt_f=&lab=scan-results&printer=192.168.1.20&printer_ip=192.168.1.20&label_zpl_style=tube_2inX1in`

##### Using wget from a shell on a machine outside your local network
```bash
wget "https://dfbf-23-93-175-197.ngrok-free.app/_print_label?uid_barcode=UID33344455&alt_a=altTEXTAA&alt_b=altTEXTBB&alt_c=altTEXTCC&alt_d=&alt_e=&alt_f=&lab=scan-results&printer=192.168.1.20&printer_ip=192.168.1.20&label_zpl_style=tube_2inX1in"
```

### From SalesForce

 * There are several ways to do this, but they all boil down to somehow formulating a URL for each print request, ie: `https://dfbf-23-93-175-197.ngrok-free.app/_print_label?uid_barcode=UID33344455&lab=scan-results&printer=192.168.1.20&label_zpl_style=tube_2inX1in`, and hitting the URL via Apex, Flow, etc.
   * To send a print request, you will need to know the API url, and the `lab`, `printer_name`, and `label_zpl_style` you wish to print the salesforce `Name` aka `UID` as a label.  This example explains how to pass just one variable to print from salesforce, adding additional metadata to print involves adding additional params to the url being constructed.


#### Print Upon Object Creation (Apex Class + Flow)

> The following is a very quick prof of concept to see it work(success!). I fully expect there are more robust ways to reach this goal.

Create an Apex class to handle sending HTTP requests.

* Setup->Apex Classes, create new Apex Class, save the following as the Apex Class:

```java
public class HttpRequestFlowAction {

    public class RequestInput {
        @InvocableVariable(label='Endpoint URL' required=true)
        public String url;
        
        // Add other variables as needed, e.g. headers, body, method, etc.
    }
    
    @InvocableMethod(label='Make HTTP Request' description='Makes an HTTP request from a Flow.')
    public static List<String> makeHttpRequest(List<RequestInput> requests) {
        List<String> responses = new List<String>();
        
        for(RequestInput req : requests) {
            Http http = new Http();
            HttpRequest request = new HttpRequest();
            request.setEndpoint(req.url);
            request.setMethod('GET');  // Change method as needed: POST, PUT, etc.
            
            // Add headers, body, etc. if needed.
            
            HttpResponse response = http.send(request);
            responses.add(response.getBody());
        }
        
        return responses;
    }
}
```

* click save, the apex class is now ready.  Check the security settings and verify the profile associated with your user has access to see/use this class.

Next, create a flow which uses this Apex Class.

* setup->Flow & click `New Flow`.  I remained in the `Auto Layout` view.
* Choose `Record-Triggered Flow`
* Select the object type the flow will be triggered when an instance of this object type is created.
* Select 'A record is created` as the trigger.
* Set Entry Conditions (this might be unecessary), `Any Condition Is Met`, Field `Name`, Operator `Starts with`, Value `X`(X being the first letter of the Name field UID salesforce creates for this object.  Again, this is probably not needed, but I have not gone back to try w/out this step).
* Choose `Actions and Related Records`, and check the box at the bottom of the page to `Include a Run Asynchronously path...`
  * upon clicking this box, the graphic representation of the flow to the left of the page will now have 2 branches at the bottom of the flow rule, one `Run Immediately` and one `Run Asynchronously`.  The `Run Immediately` branch was throwing errors, so I removed it to debug at a latter date.
  * Click the node just below the `Run Asynch` oval. Add an `Action`. Select the `Make HTTP Request` we created via the Apex Class above.  Give it a `Label`, let the API Name auto generate.
  * In the `Endpoint URL` field, enter the url `https://dfbf-23-93-175-197.ngrok-free.app/_print_label?uid_barcode={!$Record.Name}&lab=scan-results&printer=!!YOURPRINTERIP!!&label_zpl_style=tube_2inX1in`, where Record.Name will be replaced with the Object.Name from the object triggering the flow.  Replace !!YOURPRINTERIP!! with one of the printer IPs zebra_day detected above.  If you are using the auto-generated zebra printers config json file, you may leave `scan-results` as the value for `lab=` as this will be the default name given when zebra_day autodetects printers.
  * add the same HTTPrequest action to the node just below `Run Immediately`.
  * click `Save` in the upper right corner of the page. Give it a name
  * Click `Debug Again`, run the `Run Immediately` branch first. This will fail.
  * You need to whitelist the URL used by Apex in this flow with Salesforce.  To do this: Setup->Remote Site Settings, click `New Remote Site`.  Give it a name, and enter your ngrok URL up to the `.app`, so: `https://dfbf-23-93-175-197.ngrok-free.app`. Click the `active` checkbox and then save.
  * CLick `Debug Again`, run the `Asyncronous` branch, this should succeed.
  * Click `Save As`, new version.
  * Click `Activate`
  * Go create one of the objects you made this flow for. This will fail!
  * Go back to your flow, click `edit flow`, switch from `Auto Layout` to `Freeform` view.
  * Click the connector labeled `Run Immediately`, delete it (leave the Async branch intact)
  * Click `Save As`, new version.
  * Click `Activate`
  * Go create a new object of the type this trigger is built to respond to... it should print, and should do so each time a new object is created.
* This toy example is intended to demonstrate this can work. Next, you should determine how you'd like to send print requests that best suits your needs.

> This was all rather a PITA honestly.

###### Create a Formula Text Field For Objects
You can construct the print URL in the formula, and this formula field can be presented on the object salesforce page.  If the user clicks the URL on the page, a print request is sent containing the data inserted by the formula for the current object.


## Host Machine Options
### Machine physically connected to your local network.
This is covered in the config and setup/install instructions above.

### AWS
#### ec2 instance
more info coming soon.  The instructions for getting the package s/w up and running is largely the same as above. However, care must be taken when configuring the network and instances which will be used at amazon.

##### From AMI?


## Other Providers
If it will work on AWS, it will work anyplace really.

## Docker
I'm not anti, but am not putting time towards this anytime soon.
