#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Collect ipv4 and ipv6 info from localhost and report to share
'''

import socket
import sys
import subprocess
import os

__author__ = "Qin Boqin"
__copyright__ = "Copyright 2017, The GTensor Project"
__credits__ = ["Qin Boqin"]
__license__ = "GPL"
__version__ = "2.0.0"
__maintainer__ = "Qin Boqin"
__email__ = "bobbqqin@bupt.edu.cn"
__status__ = "Production"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('share.gtensor.com', 10000)
path = os.path.dirname(os.path.realpath(__file__))
message = subprocess.check_output([path + '/get_ip.sh'])

try:

    # Send data
    print 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    print 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print 'received "%s"' % data

finally:
    print 'closing socket'
    sock.close()
