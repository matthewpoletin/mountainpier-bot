#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ssl
import socket
import threading

from src.reg import message
from src.channel import Channel
from src.user import User


class IrcBot(threading.Thread):
	"""
	Twitch IRC bot
	"""

	# Map of channels bot operates
	channels = {}

	def __init__(self, host, port, oauth_token, username, channels):
		"""
		Constructor for irc bot
		:param host: Host to connect to
		:type host: str
		:param port: Port of host
		:type port: int
		:param oauth_token: Password for authentication
		:type oauth_token: str
		:param username: Bot username
		:type username: str
		:param channels: List of channels to operate on
		:type channels: list of str
		"""
		super(IrcBot, self).__init__()
		print("Initializing irc bot")
		self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.ssl_sock = ssl.wrap_socket(self.tcp_sock)
		self.ssl_sock.connect((host, port))
		self.send_msg('PASS oauth:{}'.format(oauth_token))
		self.send_msg('NICK {}'.format(username))
		# TODO: move to run
		for channel in channels:
			bot_name = 'MountainPierBot'
			# TODO: check if response msg received ()
			self.join_channel(channel)
			self.channels[channel] = Channel(channel)
			self.private_msg(channel, '{} joined channel'.format(bot_name))

	def run(self):
		"""
		Main process in thread
		:return: Reason of stopping thread
		"""
		while True:
			data = self.ssl_sock.read()
			if data == b'':
				self.stop()
				return
			msg = data.decode("utf-8")
			print(msg)

			if msg.find('PING') != -1:
				self.send_msg('PONG {}'.format(msg.split()[1]))
			self.receive_msg(msg)

	def stop(self):
		"""
		Closes bot connection
		"""
		self.send_msg('QUIT')
		self.ssl_sock.close()
		self.tcp_sock.close()

	def receive_msg(self, msg):
		"""
		Processes received messages
		:param msg: Message
		:type msg: str
		"""
		# TODO: Split messages into several separate by \r\n
		# e.g.: :tmi.twitch.tv 001 mountainpierbot :Welcome, GLHF!\r\n:tmi.twitch.tv 002 mountainpierbot :Your host is tmi.twitch.tv\r\n...
		# TODO: Check for JOIN message (add to active if he is)
		# e.g.: :matthewpoletin!matthewpoletin@matthewpoletin.tmi.twitch.tv JOIN #mountainpier
		if msg.find('PRIVMSG') != -1:
			msg_info = message(msg)
			# TODO: Check if user on is server (add to active if he is)
			if msg_info['privmsg'].find('!help') != -1:
				self.private_msg(msg_info['channel'], 'List of supported commands: !server - get server adders;')
			elif msg_info['privmsg'].find('!server') != -1:
				# TODO: 1) get channel id
				# TODO: 2) get server by twitch channel id
				self.private_msg(msg_info['channel'], 'http://mountainpier.ru/servers/1')
			elif msg_info['privmsg'].find('!join') != -1:
				user = User(msg_info)
				ch = self.channels[msg_info['channel']]
				ch.add_user(user)

	def send_msg(self, msg):
		"""
		Sends a message into socket.
		:param msg: Utf-8 data
		:type msg: str
		"""
		self.ssl_sock.write(msg.encode() + b'\r\n')

	def join_channel(self, channel):
		"""
		Joins a channel
		:param channel: Utf-8 channel name
		:type channel: str
		"""
		self.cap('REQ :twitch.tv/membership')
		self.cap('REQ :twitch.tv/tags')
		self.cap('REQ :twitch.tv/commands')
		self.send_msg('JOIN #{}'.format(channel))

	def part(self, channel):
		"""
		Depart from a channel.
		:param channel: Utf-8 channel name
		:type channel: str
		"""
		self.send_msg('PART #{}'.format(channel))

	def cap(self, msg):
		"""
		The client capability negotiation extension.
		:param msg: Message
		"""
		self.send_msg("CAP {}".format(msg))

	def private_msg(self, channel, msg):
		"""
		Sends message to the channel.
		:param channel: Channel name
		:type channel: str
		:param msg: Message
		:type msg: str
		"""
		self.send_msg('PRIVMSG #{} :{}'.format(channel, msg))
