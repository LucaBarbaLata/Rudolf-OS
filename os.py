import os
import time
os.system("pip install PyQt5 PyQtWebEngine")
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
    name = input("Please enter your Username: ")
    pas = input("Please enter your password to login: ")

    with open('user/username.txt', "w") as f:
        f.writelines(name)

    with open('user/password.txt', "w") as f:
        f.writelines(pas)
    print("Setup Complete!")
    time.sleep(3)
    quit()

elif setup == '2':
    try:
        with open('user/password.txt', 'r') as login_pass, open('user/username.txt', 'r') as login_name:
            l_p = login_pass.read().strip()
            l_n = login_name.read().strip()
    except FileNotFoundError:
        print("Error: Setup files not found. Please run the setup first.")
        quit()
else:
    print("Invalid option selected. Exiting.")
    quit()

while True:
    login = input("Please enter the password for " + l_n + " Username: ")
    if login == l_p:
        os.startfile('main-os.py')
        quit()
    else:
        print("Wrong Password!")
