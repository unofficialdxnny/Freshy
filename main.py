import subprocess
from elevate import elevate


elevate()



subprocess.run(["reg.exe", "add", "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\StorageSense\Parameters\StoragePolicy", "/v", "01", "/t", "REG_DWORD", "/d", "1", "/f"], shell=True)
subprocess.run(["reg.exe", "add", "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\StorageSense\Parameters\StoragePolicy", "/v", "02", "/t", "REG_DWORD", "/d", "1", "/f"], shell=True)
subprocess.run(["reg.exe", "add", "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\StorageSense\Parameters\StoragePolicy", "/v", "04", "/t", "REG_DWORD", "/d", "1", "/f"], shell=True)
subprocess.run(["reg.exe", "add", "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\StorageSense\Parameters\StoragePolicy", "/v", "06", "/t", "REG_DWORD", "/d", "1", "/f"], shell=True)

subprocess.run(["reg.exe", "query", "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\StorageSense\Parameters\StoragePolicy"], shell=True)


subprocess.run(["powershell", "-Command", "(Invoke-WebRequest -Uri https://chocolatey.org/install.ps1 -UseBasicParsing).Content | powershell -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command -"], shell=True)

subprocess.run(["choco", "version"], shell=True)

with open("apps.txt", "r") as f:
    apps = [line.strip() for line in f.readlines()]


for app in apps:
    subprocess.run(["choco", "install", app, "-y"], shell=True)
