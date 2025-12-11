import requests
import json
import os
import sys

def banner():
    os.system('clear')
    print("\033[1;35m")
    print(" __      __   ____   _____  _______  ________   __")
    print(" \ \    / /  / __ \ |  __ \|__   __||  ____\ \ / /")
    print("  \ \  / /  | |  | || |__) |  | |   | |__   \ V / ")
    print("   \ \/ /   | |  | ||  _  /   | |   |  __|   > <  ")
    print("    \  /    | |__| || | \ \   | |   | |____ / . \ ")
    print("     \/      \____/ |_|  \_\  |_|   |______/_/ \_\\")
    print("\n      [ VORTEX - IP Geolocation Tracker ]")
    print("\033[0m")

def track_ip():
    banner()
    target = input("\n\033[1;36m[?] Enter Target IP (Leave empty for My IP): \033[0m")
    
    print("\n\033[1;33m[*] Locating Target...\033[0m")
    
    try:
        # Use free API
        url = f"http://ip-api.com/json/{target}"
        response = requests.get(url)
        data = json.loads(response.text)
        
        if data['status'] == 'fail':
            print("\033[1;31m[!] Invalid IP Address.\033[0m")
            return

        print("\033[1;32m")
        print(f" [+] IP:       {data.get('query')}")
        print(f" [+] City:     {data.get('city')}")
        print(f" [+] Region:   {data.get('regionName')}")
        print(f" [+] Country:  {data.get('country')}")
        print(f" [+] ISP:      {data.get('isp')}")
        print(f" [+] Lat/Lon:  {data.get('lat')}, {data.get('lon')}")
        print(f" [+] Timezone: {data.get('timezone')}")
        print("\033[0m")
        
        # Sigma Move: Generate Google Maps Link
        print(f"\033[1;37m[>] Google Maps: https://www.google.com/maps/place/{data.get('lat')},{data.get('lon')}\033[0m")

    except Exception as e:
        print(f"\n\033[1;31m[!] Error: {e}\033[0m")

if __name__ == "__main__":
    track_ip()

