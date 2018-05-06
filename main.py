#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from settings import config

from src.bot import IrcBot
from src.server import Server


def main(argv):
	bot_thread = IrcBot(config['host'], config['port'], config['oauthToken'], config['username'], config['channels'])
	server_thread = Server("127.0.0.1", 54321)
	server_thread.start()
	bot_thread.start()


if __name__ == "__main__":
	main(sys.argv)
