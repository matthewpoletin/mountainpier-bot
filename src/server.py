#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import socket
import queue


class Server(threading.Thread):
	"""
	Class for upd server
	"""

	def __init__(self, address, port):
		"""
		Constructor for server
		:param address: Host of udp server
		:param port: Port of udp server
		"""
		super(Server, self).__init__()
		send_queue = queue.Queue()
		self.address = address
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((self.address, self.port))
		print('starting up on %s port %s' % (self.address, self.port))

	def run(self):
		"""
		Main process of thread
		:return: Reason of stopping
		"""
		while True:
			print('\nwaiting to receive message')
			data, address = self.sock.recvfrom(4096)
			print('received %s bytes from %s' % (len(data), address))
			if data:
				sent = self.sock.sendto(data, address)
				print(data)
				print('sent %s bytes back to %s' % (sent, address))

	def send(self, data, address):
		"""
		Sends udp data to address
		:param data: Information to send in utf-8 string
		:param address: Host and port of destination
		:return: Success of sending
		"""
		# TODO: add to send queue and exit
		sent = self.sock.sendto(data.encode('utf-8'), address)
		if sent == 0:
			# TODO: Log error in sending package
			pass
