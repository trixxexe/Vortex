import socket
import os
import time
import threading
from datetime import datetime

# The "VORTEX" Banner
def banner():
    os.system('clear')
    print("\033[1;35m")
    print(" __      __   ____   _____  _______  ________   __")
    print(" \ \    / /  / __ \ |  __ \|__   __||  ____\ \ / /")
    print("  \ \  / /  | |  | || |__) |  | |   | |__   \ V / ")
    print("   \ \/ /   | |  | ||  _  /   | |   |  __|   > <  ")
    print("    \  /    | |__| || | \ \   | |   | |____ / . \ ")
    print("     \/      \____/ |_|  \_\  |_|   |______/_/ \_\\")
    print("\n      [ VORTEX - Local Network Sweeper ]")
    print("\033[0m")

# The Scanner Function
def scan_ip(ip):
    # We try to connect to port 53 (DNS) or 80 (Web). 
    # If the device refuses or accepts, it's ALIVE. 
    # If it times out, it's dead.
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # Fast timeout
        result = sock.connect_ex((ip, 53)) # Try Port 53 first
        if result == 0 or result == 111: # 0=Open, 111=Refused (But Alive!)
            print(f"\033[1;32m[+] DEVICE FOUND: {ip}\033[0m")
        sock.close()
    except:
        pass

def start_scan():
    banner()
    # Get user input for the network range
    net = input("\n\033[1;36m[?] Enter Subnet (e.g. 192.168.1): \033[0m")
    
    if not net:
        print("\033[1;31m[!] No network entered. Defaulting to 192.168.1\033[0m")
        net = "192.168.1"

    print(f"\n\033[1;33m[*] Sweeping {net}.1 to {net}.254...\033[0m\n")
    
    start_time = datetime.now()
    threads = []

    # Launch 254 threads at once (SIGMA SPEED)
    for i in range(1, 255):
        ip = f"{net}.{i}"
        t = threading.Thread(target=scan_ip, args=(ip,))
        threads.append(t)
        t.start()
        
    # Wait for all threads to finish
    for t in threads:
        t.join()

    end_time = datetime.now()
    duration = end_time - start_time
    print(f"\n\033[1;37m[-] Scan completed in {duration}\033[0m")

if __name__ == "__main__":
    try:
        start_scan()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Scan Cancelled.\033[0m")

