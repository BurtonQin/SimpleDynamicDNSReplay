#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Collect ipv4 and ipv6 info from client reports and record in hosts
'''

import socket
import sys
import subprocess

__author__ = "Qin Boqin"
__copyright__ = "Copyright 2017, The GTensor Project"
__credits__ = ["Qin Boqin"]
__license__ = "GPL"
__version__ = "2.0.0"
__maintainer__ = "Qin Boqin"
__email__ = "bobbqqin@bupt.edu.cn"
__status__ = "Production"

hosts = 'hosts'

class Record(object):
	"""
		ipv4, ipv6 info of client
	"""
	
	def __init__(self, ipv4, ipv6):
		self.ipv4 = ipv4
		self.ipv6 = ipv6

	def __eq__(self, other):
		return self.ipv4 == other.ipv4 and self.ipv6 == other.ipv6

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('::', 10000)
print 'starting up on %s port %s' % server_address

sock.bind(server_address)

records = {}

while True:
	print '\nwaiting to receive message'
	data, address = sock.recvfrom(4096)
	
	print 'received %s bytes from %s' % (len(data), address)
	print data
	
	if data:
		result = data.split( )
		if len(result) == 3:	
			hostname = result[0]
			hostname6 = hostname + '6'
			ipv4 = result[1]
			ipv6 = result[2]
			new_record = Record(ipv4, ipv6)
		
			if records.has_key(hostname):
				if (new_record == records[hostname]):
					resp = 'exists and no change'
					print resp
				else:
					records[hostname] = new_record
					substitute = 's/.* %s$/%s %s/' % (hostname, ipv4, hostname)
					substitute6 = 's/.* %s$/%s %s/' % (hostname6, ipv6, hostname6)
					subprocess.call(['sed', '-i', '-e', substitute, hosts])
					subprocess.call(['sed', '-i', '-e', substitute6, hosts])
					resp = 'exists and changes'
					print resp
			else:
				records[hostname] = new_record
			
				insertion = '1i%s %s' % (ipv4, hostname)
				insertion6 = '2i%s %s' % (ipv6, hostname6)
			
				subprocess.call(['sed', '-i', insertion, hosts])
				subprocess.call(['sed', '-i', insertion6, hosts])
				resp = 'not exists and inserts'	
				print resp
		else:
			resp = 'bad format'
			print resp
		
		sent = sock.sendto(resp, address)
