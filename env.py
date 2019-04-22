#!/usr/bin/python
#!/usr/bin/python2
#!/usr/bin/python3
#!/usr/bin/env python
#!/usr/bin/env python2
#!/usr/bin/env python3
# -*- coding: utf8 -*-

##!/bin/sh -x
#Author               :- Md Jabed Ali(jabed)

import os
import psutil
import bs4
import random
import time
from socket import *
import struct
import subprocess
import sys
import re
import requests
import smpt

"""def processstat(pid):
    for a in open("/proc/%d/status" % pid).readlines():
        if a.startswith(":"):
            return a.split(":",1)[1].strip().split(' ')[0]
    return None"""

def random_useragent():
    #http://useragentstring.com/pages/useragentstring.php
    url = "https://fake-useragent.herokuapp.com/browsers/0.1.8"
    r = requests.get(url)
    randomuseragent = loads(r.text)['browsers']
    #print(random.choice(randomuseragent[random.choice(list(randomuseragent))]))
    return random.choice(randomuseragent[random.choice(list(randomuseragent))])

#ua = random_useragent()

gethstname = os.popen("ipconfig /all").readlines() #wndws

#http://checkip.dyndns.org/
#http://ip.nefsc.noaa.gov
#x-client-ip , https://www.wikipedia.org ,  header
#re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', str)
#chmod 400 2013.pem
#ssh -i 2013.pem
#chmod 400 2014.pem
#os.system("curl ipinfo.io/ip")
#uname -a
#hostname
#nmap
#git clone https://github.com/-/SS7Client/
#ss7.dos
#sigploit
#os.system("sudo nano /etc/sshd_config")
#os.system("ssh -f -N ....@.com -R 1664:127.0.0.1:0000")
#os.system("sudo nano /etc/sshd_config")
#netstat -atun
#os.system("sudo netstat -plunt
#os.system("sudo lshw -short")
#os.system("vim /sys/class/net/*/address")

thost = ""
tport = 
lhost = ""
lport =

def forwarding(data, port):
    print ('Forwarding: ' , data 'from port', port)
    sock = socket.socket(AF_INET, SOCK_DGRAM)
    sock.bind(("127.0.0.1", port)) 
    sock.sendto(data, (thost, tport))

def listening(host, port):
    listening_socket = socket.socket(AF_INET, SOCK_DGRAM)
    listening_socket.bind((host, port))
    print ("Listening:", host, port)
    while True:
        data, addr = listening_socket.recvfrom() #1024
        forwarding(data, addr[1])
        
ip = requests.get('https://api.ipify.org').text
print ('IP address:', ip)
print ('Host Name / User :', str(re.findall('Host Name(.*?)\'', str(gethstname), re.DOTALL)[0]).replace('\\n', '').split(':')[-1])
addrs = psutil.net_if_addrs()
addrs.keys()

def processstat():
    for prcslist in psutil.process_iter():
        try:
            name = prcslist.name()
            id = prcslist.pid
            print(name + ' : ', id)
        except:
            psutil.NoSuchProcess
            pass

    
