#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Program: "senhador.py"
Creator: Sh11td0wn <sh11td0wn@gmail.com>
Date: 01/Feb/2015

Description: by default, generates a string based on a md5 hash of a word given by the user, with special characters (@) at both ends.

Ex.
	senhador.py
	<user input: 'python'>
	<copied to clipboard: '@23eeeb4347bdd26bfc6b7ee9a3b755dd@'>

Dependencies:
	This program requires the package 'xclip' installed on system.
"""

# Modules #
from hashlib import md5
from sys import argv
from getpass import getpass
from os import system

# Functions #

def help_me():
	result="""
	Texto de ajuda
	"""
	return result

def version_me():
	result="""
	Versão 0.1
	"""
	return result

def generate_hash(word):
	result = md5(word).hexdigest()
	return result

# Flags #
F_HELP=0
F_VERSION=0
F_HIDDEN=1
F_VISIBLE=0
F_ONLY_HASH=0
F_STRING=0

# Parameters treatment #
for item in range(1,len(argv)):
	if argv[item] == '-h' or argv[item] == '--help':
		F_HELP = 1
	elif argv[item] == '-v' or argv[item] == '--version':
		F_VERSION = 1
	elif argv[item] == '-H' or argv[item] == '--hidden':
		F_HIDDEN = 1
	elif argv[item] == '-V' or argv[item] == '--visible':
		F_VISIBLE = 1
	elif argv[item] == '-o' or argv[item] == '--only-hash':
		F_ONLY_HASH = 1
	elif argv[item] == '-s' or argv[item] == '--string':
		F_STRING = 1
	else:
		print('Invalid option!')
		exit(1)

# Generic flags treatment #

if F_HELP == 1:
	print(help_me())
	exit(0)

if F_VERSION == 1:
	print(version_me())
	exit(0)

# Validate the situation of '-s' without '-V'
if F_VISIBLE == 0 and F_STRING == 1:
	print('Option -s|--string requires option -V|--visible')
	exit(1)

# Read the string from user input without echo on screen
word = getpass(prompt='')
debug = 1
# Special flags treatment #

if F_ONLY_HASH == 1:
	result = generate_hash(word)
else:
	result = '@' + generate_hash(word) + '@'

if F_VISIBLE == 1 and F_STRING == 1:
	if F_STRING == 1:
		print('String: %s' % (word))
		print('')
	print(result)
	exit(0)
elif  F_VISIBLE == 1 and F_STRING == 0:
	print(result)
	exit(0)
else:
	# Obs. This program requires the package 'xclip' installed.
	system('printf %s | xclip -selection clipboard' % (result))
	exit(0)

#EOF

