#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

# List of patterns in PRIVMSG
patterns = {
	# TODO: fix for empty badges string
	# TODO: e.g.: "badges=;"
	# badges=broadcaster/1;
	"badges": r'badges=(.+?);',
	# color=#0000FF;
	"color": r'color=(#[0-9A-F]{6});',
	# display-name=MatthewPoletin;
	"display-name": r'display-name=(.+?);',
	# emotes=;
	"emotes": r'emotes=(.);',
	# id=a9469a2d-2b16-4b70-8a34-e5fe96c5d1e6;
	"id": r'id=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})',
	# mod=0;
	"mod": r'mod=(\d);',
	# room-id=38828408;
	"room-id": r'room-id=(\d+);',
	# subscriber=0;
	"subscriber": r'subscriber=(\d);',
	# tmi-sent-ts=1525508207528;
	"tmi-sent-ts": r'tmi-sent-ts=(\d{13});',
	# turbo=0;
	"turbo": r'turbo=(\d);',
	# user-id=38828408;
	"user-id": r'user-id=(\d+);',
	# TODO: fix user type regex
	# user-type=
	"user-type": r'user-type=(.+?)\s*?:',
	# PRIVMSG #mountainpier :Привет
	"channel": r'PRIVMSG\s#(.+?)\s:',
	# PRIVMSG #mountainpier :Привет
	"privmsg": r'PRIVMSG\s#.+?\s:(.+?)$',
}

comps = {}
for name, pattern in patterns.items():
	comps[name] = re.compile(pattern)


def message(msg):
	"""
	Retrieves info from PRIVMSG
	:param msg: Message
	:return: Information about message
	:rtype: dict
	"""
	res = {}
	for _name, comp in comps.items():
		match = comp.search(msg)
		if match is not None:
			if match.group(1):
				res[_name] = match.group(1)
	return res


# TODO: Create tests
def main(argv):
	msg1 = "@badges=broadcaster;color=#0000FF;display-name=MatthewPoletin;emotes=;id=a9469a2d-2b16-4b70-8a34-e5fe96c5d1e6;mod=0;room-id=38828408;subscriber=0;tmi-sent-ts=1525508207528;turbo=0;user-id=38828408;user-type= :matthewpoletin!matthewpoletin@matthewpoletin.tmi.twitch.tv PRIVMSG #matthewpoletin :Привет"
	msg2 = "@badges=broadcaster/1;color=#0000FF;display-name=MatthewPoletin;emotes=;id=2f2e3950-13f9-4712-9416-a52a52472ac7;mod=0;room-id=218077315;subscriber=0;tmi-sent-ts=1525508585383;turbo=0;user-id=38828408;user-type= :matthewpoletin!matthewpoletin@matthewpoletin.tmi.twitch.tv PRIVMSG #mountainpier :Пока"
	msg3 = "@badges=;color=#0000FF;display-name=MatthewPoletin;emotes=;id=ba58ed75-3f36-4f87-9b39-8c6a34fa4a3e;mod=0;room-id=218077315;subscriber=0;tmi-sent-ts=1525591993648;turbo=0;user-id=38828408;user-type= :matthewpoletin!matthewpoletin@matthewpoletin.tmi.twitch.tv PRIVMSG #mountainpier :Привет"

	print("1:")
	res1 = message(msg1)
	for i in res1:
		print("{}: {}".format(i, res1[i]))
	print("2:")
	res2 = message(msg2)
	for i in res2:
		print("{}: {}".format(i, res2[i]))


if __name__ == "__main__":
	main(sys.argv)
