#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from settings import config

# TODO: Add app authorization
headers = {'access-token': config['accessToken']}

env = 'dev'


class Api:
	"""
	Class for base api access
	"""

	@staticmethod
	def get_user(user_id):
		"""
		Get information about user by id
		:param user_id: Id of requested user
		:type user_id: str
		:return: User in json
		"""
		# TODO: check user id to be valid (uuid)
		r = requests.get("{}/users/{}".format(config[env]['api'], user_id), headers=headers)
		if r.status_code == 200:
			return r.json()
		else:
			print("Error ?")

	@staticmethod
	def get_server(server_id):
		"""
		Gets information about server
		:param server_id: Id of requested server
		:type server_id: int
		:return: Server in json
		"""
		# TODO: check server id to be valid (number)
		r = requests.get('{}/servers'.format(config[env]['api'], server_id), headers=headers)
		if r.status_code == 200:
			return r.json()
		else:
			print("Error ?")

	@staticmethod
	def get_users_of_server(server_id):
		"""
		Gets paginated list of users on server
		:param server_id: Id of requested server
		:type server_id: int
		:return: Users paginated in json
		"""
		# TODO: check server id to be valid (number)
		r = requests.get('{}/servers/{}/users'.format(config[env]['api'], server_id), headers=headers)
		if r.status_code == 200:
			return r.json()
		else:
			print("Error ?")

	@staticmethod
	def add_user_to_server(server_id, user_id):
		"""
		Adds user to server by id's
		:param server_id: Id of requested server
		:type server_id: int
		:param user_id: Id of requested user
		:type user_id: str
		"""
		# TODO: check server id to be valid (number)
		# TODO: check user id to be valid (uuid)
		r = requests.post('{}/servers/{}/users/{}'.format(config[env]['api'], server_id, user_id), headers=headers)
		if r.status_code == 201:
			return
		else:
			print("Error ?")

	@staticmethod
	def remove_user_from_server(server_id, user_id):
		"""
		Removes user from server by id's
		:param server_id: Id of requested server
		:type server_id: int
		:param user_id: Id of requested user
		:type user_id: str
		"""
		# TODO: check server id to be valid (number)
		# TODO: check user id to be valid (uuid)
		r = requests.delete('{}/servers/{}/users/{}'.format(config[env]['api'], server_id, user_id), headers=headers)
		if r.status_code == 204:
			return
		else:
			print("Error ?")


# TODO: Create tests
def main():
	print(Api.get_users_of_server(1))


if __name__ == "__main__":
	main()
