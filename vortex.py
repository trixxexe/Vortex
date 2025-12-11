import os
import sys
import time

# ANSI Colors
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
C = "\033[1;36m"  # Cyan
Y = "\033[1;33m"  # Yellow
P = "\033[1;35m"  # Purple
W = "\033[1;37m"  # White
rst = "\033[0m"   # Reset

def clear():
    os.system('clear')

def banner():
    clear()
    print(f"{P}")
    print(" █      █  ██████  ██████  ████████  ██████  █    █")
    print("  █    █   █    █  █    █     ██     █       █    █")
    print("   █  █    █    █  ██████     ██     ██████   █  █ ")
    print("    ██     █    █  █  █       ██     █         ██  ")
    print("     █     ██████  █   █      ██     ██████   █  █ ")
    print(f"{rst}")
    print(f"      {C}[ VORTEX FRAMEWORK - v1.0 | By Tr1xx ]{rst}")
    print(f"      {G}[ {len(os.listdir('.')) - 2} Tools Loaded ]{rst}\n")

def main_menu():
    while True:
        banner()
        print(f"{Y}[ RECONNAISSANCE ]{rst}")
        print(f"  {W}01.{rst} Subdomain Scanner   (VortexSub)")
        print(f"  {W}02.{rst} Google Dorker       (VortexDork)")
        print(f"  {W}03.{rst} Web Crawler/Spider  (VortexCrawl)")
        print(f"  {W}04.{rst} IP Tracker          (VortexIP)")
        print(f"  {W}05.{rst} Metadata Extractor  (VortexMeta)")
        
        print(f"\n{Y}[ NETWORK & SYSTEMS ]{rst}")
        print(f"  {W}06.{rst} Local Network Scan  (VortexNet)")
        print(f"  {W}07.{rst} Port Scanner        (VortexPort)")
        print(f"  {W}08.{rst} System Forensics    (VortexSys)")
        
        print(f"\n{Y}[ OFFENSIVE & UTILITY ]{rst}")
        print(f"  {W}09.{rst} Hash Cracker        (VortexHash)")
        print(f"  {W}10.{rst} Zip Brute Force     (VortexZip)")
        print(f"  {W}11.{rst} Stress/Spam Test    (VortexSpam)")
        print(f"  {W}12.{rst} QR Code Generator   (VortexQR)")
        
        print(f"\n{R}[ 00. EXIT ]{rst}")
        
        choice = input(f"\n{C}VORTEX > {rst}")

        if choice == '1' or choice == '01':
            os.system('python3 vortexsub.py')
        elif choice == '2' or choice == '02':
            os.system('python3 vortexdork.py')
        elif choice == '3' or choice == '03':
            os.system('python3 vortexcrawl.py')
        elif choice == '4' or choice == '04':
            os.system('python3 vortexip.py')
        elif choice == '5' or choice == '05':
            os.system('python3 vortexmeta.py')
        elif choice == '6' or choice == '06':
            os.system('python3 vortexnet.py')
        elif choice == '7' or choice == '07':
            os.system('python3 vortexport.py')
        elif choice == '8' or choice == '08':
            os.system('python3 vortexsys.py')
        elif choice == '9' or choice == '09':
            os.system('python3 vortexhash.py')
        elif choice == '10':
            os.system('python3 vortexzip.py')
        elif choice == '11':
            os.system('python3 vortexspam.py')
        elif choice == '12':
            os.system('python3 vortexqr.py')
        elif choice == '00' or choice == '0':
            print(f"\n{R}[!] Shutting down VORTEX...{rst}")
            sys.exit()
        else:
            print(f"\n{R}[!] Invalid Selection.{rst}")
            time.sleep(1)
        
        input(f"\n{Y}[ Press Enter to return to menu ]{rst}")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Force Exit Detected.{rst}")

