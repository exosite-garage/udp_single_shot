#!/usr/bin/python
#==============================================================================
# udp_single_shot_example.py
# Sends data to Exosite's One Platform via UDP
#==============================================================================
##
## Tested with python 2.7
##
## Copyright (c) 2012, Exosite LLC
## All rights reserved.
##
import socket

PORT = 18494
HOST = 'm2.exosite.com'
msg = "cik=PUTCIKHERE&PUTALIASHERE=hello_world!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((HOST, PORT))
sock.send(msg)
sock.close()
