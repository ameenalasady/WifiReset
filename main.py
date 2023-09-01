import os
import time
import json
import subprocess

with open('info.json', 'r') as f:
    data = json.load(f)

network_name = data['networkName']


def check_ping():
    hostname = "192.168.2.1"
    response = subprocess.run(
        "wsl ping -c 6 -i 0.1 -W 0.5 " + hostname, shell=True)
    if response.returncode == 0:
        return True
    else:
        return False


def reset_wifi():
    # Disconnect from the Wi-Fi network
    os.system('netsh wlan disconnect')
    time.sleep(1)
    # Reconnect to the Wi-Fi network
    os.system('netsh wlan connect name=' + str(network_name))
    time.sleep(10)


while True:
    if not check_ping():
        print("Resetting...\n")
        reset_wifi()
        print("Reset complete.\n")
