import os
import time


def check_ping():
    hostname = "google.com"
    response = os.system("ping -n 2 -w 500 " + hostname)
    if response == 0:
        return True
    else:
        return False


def reset_wifi():
    # Disconnect from the Wi-Fi network
    os.system('netsh wlan disconnect')
    time.sleep(1)
    # Reconnect to the Wi-Fi network
    os.system('netsh wlan connect name=VIRGIN620_5.0')
    time.sleep(10)


while True:
    if not check_ping():
        print("Resetting...\n")
        reset_wifi()
        print("Reset complete.\n")
    time.sleep(1)
