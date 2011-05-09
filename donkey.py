#!/usr/bin/python
import getpass
import sys
import telnetlib
import os
import re

if sys.argv[1]:
    bturl = str(sys.argv[1])
    btcommand = "startbt '%s' \n" % bturl
    print "We will add %s " % bturl
    debuglevel = 0
    ipcommand = "curl ifconfig.me/ip"
    ip = str(os.popen(ipcommand).read())
    re_ip = re.compile(r"^83.*")
    re_ip_result = re_ip.match(ip)
    if re_ip_result:
        print "We are in home (%s) -> using local IP" % ip
        host = "10.0.0.1"
        port = 4000
        tn = telnetlib.Telnet(host,port)
        tn.set_debuglevel(debuglevel)
        tn.read_until("> ")
        tn.write("auth admin dup4 \n")
        tn.read_until("\x1b[7mMLdonkey command-line:\x1b[2;37;0m\n> ")
        tn.write(btcommand)
        tn.read_until("\x1b[7mMLdonkey command-line:\x1b[2;37;0m\n> ")
    else:
        print "We aren't in home %s - connecting to rotor :O " % ip
        host = "rotor.ath.cx"
        port = 4000
        tn = telnetlib.Telnet(host,port)
        tn.set_debuglevel(debuglevel)
        tn.read_until("> ")
        tn.write("auth admin dup4 \n")
        tn.read_until("\x1b[7mMLdonkey command-line:\x1b[2;37;0m\n> ")
        tn.write(btcommand)
        tn.read_until("\x1b[7mMLdonkey command-line:\x1b[2;37;0m\n> ")
else:
    print "You have to give bittorent link !"
