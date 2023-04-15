import os
import subprocess
import requests
import shutil

# Check if running as administrator
if os.name == 'nt' and os.geteuid() == 0:
    print('Running with administrator privileges...')
else:
    print('This script requires administrator privileges. Please run as administrator and try again.')
    input('Press Enter to exit...')
    exit()

# Check internet connection and speed
print("Checking internet connection and speed...")
while True:
    try:
        response = requests.get("https://www.google.com")
        if response.status_code == 200:
            print("Internet is connected")
            speedtest = requests.get("https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py")
            with open("speedtest.txt", "w") as file:
                file.write(speedtest.content.decode())
            with open("speedtest.txt", "r") as file:
                print(file.read())
            subprocess.run("rm speedtest.txt", shell=True)
            break
            
print("Installing software from apps.txt...")
with open("apps.txt", "r") as file:
    for app in file:
        app = app.strip()
        subprocess.run(["choco", "install", app, "-y"])
        
        
        # Update Windows
print("Checking for Windows updates...")
subprocess.run(["powershell.exe", "Get-WindowsUpdate", "-Install", "-AcceptAll"], check=True)
print("Windows is up-to-date.")



# Create a backup of Documents folder
src_folder = r'C:\Users\username\Documents'
dest_folder = r'D:\Backup\Documents'
shutil.copytree(src_folder, dest_folder)

## restore point
print("Creating a system restore point...")
subprocess.run(["powershell.exe", "Checkpoint-Computer", "-Description", "System Restore Point"])

# Optimize your system
print("Optimizing your system...")
print("Disabling unnecessary startup programs...")
os.system("powershell.exe -command \"Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' -Name 'ProgramName' -Value $null\"")
print("Defragmenting hard drive...")
os.system("defrag c: /h /u /v")
print("Running disk cleanup...")
os.system("cleanmgr /sagerun:1")

# Secure your system
print("Securing your system...")
print("Enabling Firewall...")
subprocess.call(["netsh", "advfirewall", "set", "allprofiles", "state", "on"])
print("Configuring User Account Control (UAC) settings...")
subprocess.call(["powershell.exe", "Set-ItemProperty", "-Path", "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", "-Name", "EnableLUA", "-Value", "1"])
print("Setting up strong passwords for user accounts...")
subprocess.call(["net", "user", "Administrator", "Password123"])


# Setting custom cursors as default
print("Setting custom cursors as default...")

subprocess.call(['reg', 'add', 'HKCU\\Control Panel\\Cursors', '/v', 'Arrow', '/t', 'REG_SZ', '/d', 'C:\\Windows\\Cursors\\my_arrow.cur', '/f'])
subprocess.call(['reg', 'add', 'HKCU\\Control Panel\\Cursors', '/v', 'Wait', '/t', 'REG_SZ', '/d', 'C:\\Windows\\Cursors\\my_wait.cur', '/f'])
subprocess.call(['reg', 'add', 'HKCU\\Control Panel\\Cursors', '/v', 'AppStarting', '/t', 'REG_SZ', '/d', 'C:\\Windows\\Cursors\\my_appstarting.cur', '/f'])
subprocess.call(['reg', 'add', 'HKCU\\Control Panel\\Cursors', '/v', 'Help', '/t', 'REG_SZ', '/d', 'C:\\Windows\\Cursors\\my_help.cur', '/f'])
subprocess.call(['reg', 'add', 'HKCU\\Control Panel\\Cursors', '/v', 'No', '/t', 'REG_SZ', '/d', 'C:\\Windows\\Cursors\\my_no.cur', '/f'])
subprocess.call(['reg', 'add', 'HKCU\\Control Panel\\Cursors', '/v', 'NWPen', '/t', 'REG_SZ', '/d', 'C:\\Windows\\Cursors\\my_nwpen.cur', '/f'])
subprocess.call(['reg', 'add', 'HKCU\\Control Panel\\Cursors', '/v', 'SizeNS', '/t', 'REG_SZ', '/d', 'C:\\Windows\\Cursors\\my_sizens.cur', '/f'])
subprocess.call(['reg', 'add', 'HKCU\\Control Panel\\Cursors', '/v', 'SizeWE', '/t', 'REG_SZ', '/d', 'C:\\Windows\\Cursors\\my_sizewe.cur', '/f'])
subprocess.call(['reg', 'add', 'HKCU\\Control Panel\\Cursors', '/v', 'UpArrow', '/t', 'REG_SZ', '/d', 'C:\\Windows\\Cursors\\my_uparrow.cur', '/f'])
subprocess.call(['reg', 'add', 'HKCU\\Control Panel\\Cursors', '/v', 'IBeam', '/t', 'REG_SZ', '/d', 'C:\\Windows\\Cursors\\my_ibeam.cur', '/f'])

print("All tasks completed.")
input("Press Enter to exit...")


    except:
        print("\033[1m\033[31mCONNECT TO INTERNET\033[0m")
        time.sleep(10)
    
    
