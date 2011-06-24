#!/usr/bin/python

# py-abemails
# 
# Extract all e-mail addresses from the Mac OS X address book
#
# (c) Benjamin Esham, 2011.  See the accompanying README.md for this file's
# license and other information.

import sys, os, sqlite3

script_version = "1.0"


# print version and help information

def version_text():
	old_out = sys.stdout
	sys.stdout = sys.stderr

	print "py-abemails", script_version
	print "(c) 2011, Benjamin Esham"
	print "https://github.com/bdesham/py-abemails"

	sys.stdout = old_out

def help_text():
	version_text()

	old_out = sys.stdout
	sys.stdout = sys.stderr

	print
	print "usage: python py-abemails [-f input-file] [output-file]"

	sys.stdout = old_out


# parse command-line arguments

args = sys.argv[1:]

if "-v" in args or "--version" in args:
	version_text()
	exit()

if len(args) > 3 or "-h" in args or "--help" in args:
	help_text()
	exit()

if "-f" in args:
	ind = args.index("-f")

	try:
		in_file = args[ind+1]
	except IndexError, e:
		help_text()
		exit()

	args.pop(ind)
	args.pop(ind)
else:
	in_file = "~/Library/Application Support/AddressBook/AddressBook-v22.abcddb"

in_file = os.path.expanduser(in_file)

if not os.path.isfile(in_file):
	print >> sys.stderr, "py-abemails: the file \"%s\" does not exist" % in_file
	exit()

if len(args):
	try:
		out = open(os.path.expanduser(args[0]), 'w')
	except IOError, r:
		print >> sys.stderr, "py-abemails: error opening the output file."
		print >> sys.stderr, e
		exit()
	output_to_file = True
else:
	out = sys.stdout
	output_to_file = False


# look at the database

conn = sqlite3.connect(in_file)

try:
	addresses = conn.execute("SELECT ZADDRESSNORMALIZED FROM ZABCDEMAILADDRESS")
except sqlite3.OperationalError, e:
	print >> sys.stderr, "py-abemails: error reading the Address Book database."
	print >> sys.stderr, e
	exit()


# output the addresses

for a in addresses:
	print >> out, a[0]

# clean up

if output_to_file:
	out.close()
