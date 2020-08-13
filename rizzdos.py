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

def flush(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)

def out():
        exit()

def back():
        raw_input('\n\x1b[1;91m                                 [ \x1b[1;97mBack \x1b[1;91m]')
        home()

def nxt():
        raw_input('\n\x1b[1;91m                                 [ \x1b[1;97mNext \x1b[1;91m]')
        os.system('clear')

def logo():
        f = open('Baner/asci')
        print merah+f.read()
        f.close
        print '---------------------------------------------------'
        print cyan+' Author  : '+green+'MRH {ExploiID} '
        print cyan+' Github  : '+green+'http://github.com/MRH02 '
        print cyan+' Youtube : '+green+'MRH Official '                   
        print putih+'---------------------------------------------------'
        print ''

def req():
    os.system('clear')
    logo()
    home()

def ddos():
    os.system('clear')
    logo()
    print merah+"Contoh Alamat IP (192.168.xxx.xxx)"
    name=raw_input(merah+"Masukkan IP Target : ")
    os.system('clear')
    print hijau+"[*] Sedang DDoS, Mohon Bersabar..."
    time.sleep(2)
    dos2()
    
def dos2():
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    print merah+"Sedang DDoS  "+name+" Sampai Down!"
    dos2()

def update():
	os.system('clear')
	os.system('git stash && git pull origin master')
	os.system('python2 install.py')
	raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
	home()

def menu():
        os.system('clear')
        time.sleep(1)
        logo()
        flush (merah+"FOLLOW IG : @jalanyanglurus_")
        flush (merah+"1. Start DDoS"           merah+"2.Update")
        flush (green+"3.Install Requirements"  merah+"4.Quit")
def pilih():
    zedd = raw_input(merah+'RizzDos$ > ')
    if zedd == '':
        print '\x1b[1;91m[!] Can\'t empty'
        time.sleep(1)
        os.system('clear')
        home()
    else:
        if zedd == '1':
            ddos()
        else:
            if zedd == '2':
                update()
            else:
              if zedd == '3':
                req()
                home()
              else:
                                  if zedd == '4':
                                        out()
                                  else:
                                    print "merah+pilih 1-4"
                                    os.system('clear')
                                    home()

def home():
	menu()
	pilih()         

home()