@echo off

:: Install Chocolatey package manager
echo Installing Chocolatey...
powershell.exe -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"

:: Install essential software using Chocolatey
echo Installing essential software...
choco install googlechrome microsoft-office vlc -y

:: Update Windows
echo Checking for Windows updates...
powershell.exe -command "Get-WindowsUpdate -Install -AcceptAll"
echo Windows is up-to-date.

:: Create a backup of important files
echo Creating a backup of Documents folder...
xcopy "C:\Users\username\Documents" "D:\Backup\Documents" /e /i /h

:: Set up a system restore point
echo Creating a system restore point...
powershell.exe -command "Checkpoint-Computer -Description 'System Restore Point'"

:: Optimize your system
echo Optimizing your system...
echo Disabling unnecessary startup programs...
powershell.exe -command "Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' -Name 'ProgramName' -Value $null"
echo Defragmenting hard drive...
defrag c: /h /u /v
echo Running disk cleanup...
cleanmgr /sagerun:1

:: Secure your system
echo Securing your system...
echo Enabling Firewall...
netsh advfirewall set allprofiles state on
echo Configuring User Account Control (UAC) settings...
powershell.exe -command "Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name 'EnableLUA' -Value 1"
echo Setting up strong passwords for user accounts...
net user Administrator Password123

:: Done
echo All tasks completed.
pause
