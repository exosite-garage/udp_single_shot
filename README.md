================================================================================
UDP Single Shot Example
================================================================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is a simple python script demonstrating how to send data to Exosite's 
cloud data platform via the UDP Single Shot API.

License is BSD, Copyright 2011, Exosite LLC (see LICENSE file)

Built/tested with Python 2.6.5

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Quick Start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Install python
  * http://www.python.org/download/
  * http://www.python.org/download/releases/2.7.2/

* Register for API keys on the One Platform by signing up for Exosite Portals
  at https://portals.exosite.com

* Create a Client (Device) and a Datasource (Alias) in Exosite Portals. 

* Copy the Client's CIK and paste it in place of the PUTCIKHERE in the python
  script.  Copy the Datasource's Alias and paste it in place of the 
  PUTALIASHERE in the python script.

* Run the script

    python udp_single_shot_example.py

* View your data in Exosite Portals to verify everything worked OK!

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
More Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* UDP Overview -> http://en.wikipedia.org/wiki/User_Datagram_Protocol
* UDP API documentation -> http://exosite.com/api

**Notes**

* UDP is inherently non-secure and non-reliable.  Use the API only if you are
  OK with those inherent issues.

