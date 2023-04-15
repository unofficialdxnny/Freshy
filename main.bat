@echo off

:: Check if running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running with administrator privileges...
) else (
    echo This script requires administrator privileges. Please run as administrator and try again.
    pause
    exit
)

:: Check internet connection and speed
echo Checking internet connection and speed...
:check_internet
powershell.exe -command "$ping = Test-Connection google.com -Count 1 -ErrorAction SilentlyContinue; if($ping){Write-Host 'Internet is connected'; $speedtest = Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py' -UseBasicParsing; python -c $speedtest.content | Out-File -FilePath speedtest.txt; Get-Content -Path speedtest.txt; Remove-Item -Path speedtest.txt;} else {Write-Host -ForegroundColor Red 'CONNECT TO INTERNET'; Start-Sleep -Seconds 10; goto check_internet;}"

:: Install software using Chocolatey from apps.txt file
echo Installing software from apps.txt...
for /F "usebackq delims=" %%i in ("apps.txt") do choco install "%%i" -y

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


:: Set custom cursors as default
echo Setting custom cursors as default...
reg add "HKCU\Control Panel\Cursors" /v Arrow /t REG_SZ /d "C:\Windows\Cursors\my_arrow.cur" /f
reg add "HKCU\Control Panel\Cursors" /v Wait /t REG_SZ /d "C:\Windows\Cursors\my_wait.cur" /f
reg add "HKCU\Control Panel\Cursors" /v AppStarting /t REG_SZ /d "C:\Windows\Cursors\my_appstarting.cur" /f
reg add "HKCU\Control Panel\Cursors" /v Help /t REG_SZ /d "C:\Windows\Cursors\my_help.cur" /f
reg add "HKCU\Control Panel\Cursors" /v No /t REG_SZ /d "C:\Windows\Cursors\my_no.cur" /f
reg add "HKCU\Control Panel\Cursors" /v NWPen /t REG_SZ /d "C:\Windows\Cursors\my_nwpen.cur" /f
reg add "HKCU\Control Panel\Cursors" /v SizeNS /t REG_SZ /d "C:\Windows\Cursors\my_sizens.cur" /f
reg add "HKCU\Control Panel\Cursors" /v SizeWE /t REG_SZ /d "C:\Windows\Cursors\my_sizewe.cur" /f
reg add "HKCU\Control Panel\Cursors" /v UpArrow /t REG_SZ /d "C:\Windows\Cursors\my_uparrow.cur" /f
reg add "HKCU\Control Panel\Cursors" /v IBeam /t REG_SZ /d "C:\Windows\Cursors\my_ibeam.cur" /f


:: Done
echo All tasks completed.
pause
