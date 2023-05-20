import os
import time


def check_ping():
    hostname = "google.com"
    response = os.system("ping " + hostname)
    if response == 0:
        return True
    else:
        return False


def reset_wifi():
    os.system("netsh interface set interface name=\"Wi-Fi\" admin=disable")
    time.sleep(5)
    os.system("netsh interface set interface name=\"Wi-Fi\" admin=enable")


while True:
    if not check_ping():
        print("Resetting...\n")
        reset_wifi()
        print("Reset complete.\n")
    time.sleep(30)
