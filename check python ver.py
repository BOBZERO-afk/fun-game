import sys
import sysconfig
import os
import re
import urllib.request
import subprocess
import ctypes
import time
from packaging.version import Version

PYTHON_FTP = "https://www.python.org/ftp/python/"
INSTALLER_SUFFIX = "amd64.exe"
TEMP_INSTALLER = os.path.join(os.environ["TEMP"], "python_latest.exe")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def reboot():
    ctypes.windll.user32.ExitWindowsEx(0x02 | 0x04, 0)

def get_latest_python_installer():
    with urllib.request.urlopen(PYTHON_FTP) as response:
        html = response.read().decode("utf-8")

    versions = re.findall(r'href="(\d+\.\d+\.\d+)/"', html)
    versions.sort(key=Version, reverse=True)

    for version in versions:
        installer_url = f"{PYTHON_FTP}{version}/python-{version}-{INSTALLER_SUFFIX}"
        try:
            urllib.request.urlopen(installer_url)
            return Version(version), installer_url
        except:
            continue

    raise RuntimeError("No valid Python installer found.")

if not is_admin():
    print("ERROR: Run this script as Administrator.")
    sys.exit(1)

current_version = Version(sysconfig.get_python_version())
print("Current Python version:", current_version)

latest_version, installer_url = get_latest_python_installer()
print("Latest Python version:", latest_version)

if current_version >= latest_version:
    print("Python is already up to date.")
    sys.exit(0)

print("Downloading newest Python...")
urllib.request.urlretrieve(installer_url, TEMP_INSTALLER)

print("Starting Python installer...")
subprocess.Popen([
    TEMP_INSTALLER,
    "/quiet",
    "InstallAllUsers=1",
    "PrependPath=1",
    "Include_test=0"
])

print("Installer launched.")
print("System will reboot in 15 seconds...")

time.sleep(15)
reboot()
sys.exit(0)