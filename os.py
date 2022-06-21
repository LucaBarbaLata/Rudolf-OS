import os
import time

print("""

██████╗░██╗░░░██╗██████╗░░█████╗░██╗░░░░░███████╗░░░░░░░█████╗░░██████╗
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██║░░░░░██╔════╝░░░░░░██╔══██╗██╔════╝
██████╔╝██║░░░██║██║░░██║██║░░██║██║░░░░░█████╗░░█████╗██║░░██║╚█████╗░
██╔══██╗██║░░░██║██║░░██║██║░░██║██║░░░░░██╔══╝░░╚════╝██║░░██║░╚═══██╗
██║░░██║╚██████╔╝██████╔╝╚█████╔╝███████╗██║░░░░░░░░░░░╚█████╔╝██████╔╝
╚═╝░░╚═╝░╚═════╝░╚═════╝░░╚════╝░╚══════╝╚═╝░░░░░░░░░░░░╚════╝░╚═════╝░
""")

print("""
[1] Continue with the setup.
[2] I've Already Done The Setup.
""")
setup = input("[?]: ")

if setup == '1':
    name = input(str("Please enter your Username: "))
    pas = input(str("Please enter your password to login: "))

    with open('user/username.txt', "w") as f:
        f.writelines(name)

    with open('user/password.txt', "w") as f:
        f.writelines(pas)
    print("Setup Complete!")
    time.sleep(3)
    quit()

if setup == '2':
    login_pass = open('user/password.txt')
    login_name = open('user/username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()

while True:
    login = input(str("Please enter the password for " + l_n + " Username: "))
    if login == l_p:
        os.startfile('main-os.py')
        quit()
    else:
        print("Wrong Password!")



