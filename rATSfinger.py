#!/usr/bin/env python
# fingerprint Armitage Team Servers
# checks for a static string of control characters (^U^C^A^@^B^B) within a "ghost file".
# When issuing a get request for a non-existent file (ghost file) to an Armitage Team Server port (55553 by default) over HTTP, 
# we receieve a file containing non-readable control characters. We can use them to fingerprint a team server.
# author: @0rbz_ (Fabrizio Siciliano)
# usage: python rATSfinger.py ip:port
import os
import sys

if len(sys.argv) != 2:
    print 'Usage: python %s [ip:port]' % sys.argv[0]
    exit()

target_ip = sys.argv[1]

# download ghost file containing control characters
ratsfinger = os.system("wget " + "http://" + target_ip + "/rATSFINGER" + " --quiet --output-document=/tmp/rATSFINGER")

# read it
with open('/tmp/rATSFINGER', 'r') as content:
    content = content.read()

# check for the existence of "^U^C^A^@^B^B" control characters in the ghost file
if "\025\003\001\000\002\002" in content:
    print "\n\n"
    print "==============================================================================="
    print "======== RECEIVED CONTROL CHARACTERS CONSISTENT WITH GHOST FILE =============="
    print "*** Looks like an Armitage Team Server is listening on " + target_ip + " ***"
    print "==============================================================================="
    print "\n\n"

if "\025\003\001\000\002\002" not in content:

    print "Probably not an Armitage Team Server. No control characters received."
