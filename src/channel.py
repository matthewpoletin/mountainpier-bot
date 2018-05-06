#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Channel:
	"""
	Represents an IRC channel.
	"""

	# Name of a channel
	name = ''
	# List of active users
	users = {}
	# Is any bot on this channel
	joined = False

	def __init__(self, name):
		"""
		Constructor for channel
		:param name: Name of channel
		:type name: str
		"""
		self.name = name
		self.joined = False

	def __repr__(self):
		return "<Channel: %s>" % self.name

	def join(self):
		"""
		Starts operating on channel
		:return: Status of entry
		"""
		self.joined = True
		return self.joined

	def leave(self):
		"""
		Stops operating on channel
		:return: Status of entry
		"""
		self.joined = False
		return self.joined

	def add_user(self, user):
		"""
		Adds user to the list of active
		:param user:
		:type user: User
		"""
		self.users[user.name] = user
		return self.users

	def remove_user(self, username):
		"""
		Removes user from the list of active
		:param username:
		:type username: str
		"""
		del self.users[username]
