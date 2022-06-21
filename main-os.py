import os
from select import select
import time
import socket
import sys
import datetime

login_pass = open('user/password.txt')
login_name = open('user/username.txt')
l_p = login_pass.read()
l_n = login_name.read()

print("""

██████╗░██╗░░░██╗██████╗░░█████╗░██╗░░░░░███████╗░░░░░░░█████╗░░██████╗
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██║░░░░░██╔════╝░░░░░░██╔══██╗██╔════╝
██████╔╝██║░░░██║██║░░██║██║░░██║██║░░░░░█████╗░░█████╗██║░░██║╚█████╗░
██╔══██╗██║░░░██║██║░░██║██║░░██║██║░░░░░██╔══╝░░╚════╝██║░░██║░╚═══██╗
██║░░██║╚██████╔╝██████╔╝╚█████╔╝███████╗██║░░░░░░░░░░░╚█████╔╝██████╔╝
╚═╝░░╚═╝░╚═════╝░╚═════╝░░╚════╝░╚══════╝╚═╝░░░░░░░░░░░░╚════╝░╚═════╝░
""")
print("Welcome " + l_n + "!")
print("Today is: " + time.strftime("%m%d%y"))

print("""
[1] Open Google In Rudolf-Browser
[2] Open Rudolf-Pad
[3] Open Rudolf-Explorer
[4] Open Rudolf-Time
[5] Quit Rudolf-Os Safley
""")
select = input("[?]: ")

if select == '1':
    os.startfile('browser.pyw')

if select == '2':
    os.startfile('notepad.pyw')

if select == '3':
    os.startfile('explorer.pyw')

if select == '4':
    os.startfile('time.pyw')

if select == '5':
    quit()

