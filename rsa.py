#-------------------------------------#
#-----------AAHIL---CODING
import os, time, platform
os.system("cd $HOME/")
os.system("termux-setup-storage")
try:
    import requests
except ImportError:
    os.system("pip2 install requests")
    os.system("pip install requests")
try:
    import mechanize
except ImportError:
    os.system("pip2 install mechanize")
    os.system("pip install mechanize")

rana=platform.architecture()[0]
if rana=="64bit":
    import rsa64
    rsa64.security()
elif rana=="32bit":
    import rsa32
    rsa32.security()
#-------------------------------------#
