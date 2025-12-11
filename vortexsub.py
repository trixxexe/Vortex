import requests
import sys
import os

# The "VORTEX" Banner
def banner():
    os.system('clear')
    print("\033[1;35m") # Purple Color
    print(" __      __   ____   _____  _______  ________   __")
    print(" \ \    / /  / __ \ |  __ \|__   __||  ____\ \ / /")
    print("  \ \  / /  | |  | || |__) |  | |   | |__   \ V / ")
    print("   \ \/ /   | |  | ||  _  /   | |   |  __|   > <  ")
    print("    \  /    | |__| || | \ \   | |   | |____ / . \ ")
    print("     \/      \____/ |_|  \_\  |_|   |______/_/ \_\\")
    print("\n      [ VORTEX - Subdomain Scanner Module ]")
    print("\033[0m")

def scan_domain():
    banner()
    domain = input("\n\033[1;36m[?] Enter Target Domain (e.g., google.com): \033[0m")
    
    if not domain:
        sys.exit()

    # Common subdomains to hunt for
    subs = ["www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "webdb", "blog", "dev", "test", "admin", "panel", "api", "mobile", "secure"]
    
    print(f"\n\033[1;33m[*] Hunting subdomains for: {domain}...\033[0m\n")

    found_count = 0
    
    try:
        for sub in subs:
            # Construct the full URL
            url = f"http://{sub}.{domain}"
            
            try:
                # Try to connect (Active Scan)
                requests.get(url, timeout=2)
                # If no error, it exists!
                print(f"\033[1;32m[+] FOUND: {url}\033[0m")
                found_count += 1
            except requests.ConnectionError:
                pass # Doesn't exist, ignore it
            except KeyboardInterrupt:
                print("\n\033[1;31m[!] Stopping Scan...\033[0m")
                sys.exit()

    except KeyboardInterrupt:
        sys.exit()

    print(f"\n\033[1;37m[-] Scan Complete. Found {found_count} subdomains.\033[0m")

if __name__ == "__main__":
    scan_domain()

