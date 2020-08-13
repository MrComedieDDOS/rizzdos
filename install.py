import os, sys
import time
import random

os.system('clear')

def flush(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

def nxt():
	print '---------------------------------------------------'
	raw_input('\n\x1b[1;91m					[ \x1b[1;97mNext \x1b[1;91m]')
	
def time():
	time
	os.system('time')
flush('izinkan akses penyimpanan')
nxt()
os.system('termux-setup-storage')
nxt()
os.system('pkg install unstable-repo')
os.system('apt upgrade')
os.system('apt install ruby -y')
os.system('apt install figlet')
os.system('gem install lolcat')
os.system('clear')
flush('cleaning...')
nxt()
os.system('rm -rf install.py')
print ('Starting RizzDos'+'time')
os.system('python2 rizdos.py')
