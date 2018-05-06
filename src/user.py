#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class User:
	"""
	Represents an user of channel.
	"""

	def __init__(self, info):
		"""
		Constructor for user object
		:param info:
		:type info: dict
		"""
		self.name = info['display-name']
		self.twitch_id = info['user-id']
		# TODO: make request to api, get full info
		# TODO: if fails send error to user
		# TODO: this one is temporary
		self.id = 1
		self.color = info['color']

	def __repr__(self):
		return "<User: %s>" % self.name

	# TODO: find better way to jsonify
	def __str__(self):
		return '{"id": {}, "username": "{}"}'.format(self.id, self.name)
