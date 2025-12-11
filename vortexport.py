import socket
import threading
import sys
import os
from datetime import datetime

def banner():
    os.system('clear')
    print("\033[1;35m")
    print(" __      __   ____   _____  _______  ________   __")
    print(" \ \    / /  / __ \ |  __ \|__   __||  ____\ \ / /")
    print("  \ \  / /  | |  | || |__) |  | |   | |__   \ V / ")
    print("   \ \/ /   | |  | ||  _  /   | |   |  __|   > <  ")
    print("    \  /    | |__| || | \ \   | |   | |____ / . \ ")
    print("     \/      \____/ |_|  \_\  |_|   |______/_/ \_\\")
    print("\n      [ VORTEX - Turbo Port Scanner ]")
    print("\033[0m")

# The list of "Common" ports to scan (Top 20)
common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3306, 3389, 5900, 8080]

def scan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"\033[1;32m[+] Port {port}\tOPEN\033[0m")
        sock.close()
    except:
        pass

def start_scan():
    banner()
    target_input = input("\n\033[1;36m[?] Enter Target IP or URL: \033[0m")
    
    # Resolve URL to IP
    try:
        target = socket.gethostbyname(target_input)
    except:
        print("\033[1;31m[!] Could not resolve host.\033[0m")
        sys.exit()

    print(f"\n\033[1;33m[*] Scanning {target}...\033[0m\n")
    
    threads = []
    
    # Scan standard ports
    for port in common_ports:
        t = threading.Thread(target=scan, args=(target, port))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()

    print(f"\n\033[1;37m[-] Scan Complete.\033[0m")

if __name__ == "__main__":
    start_scan()

