import os
import sys
import webbrowser # Opens the link in your real browser

def banner():
    os.system('clear')
    print("\033[1;35m")
    print(" __      __   ____   _____  _______  ________   __")
    print(" \ \    / /  / __ \ |  __ \|__   __||  ____\ \ / /")
    print("  \ \  / /  | |  | || |__) |  | |   | |__   \ V / ")
    print("   \ \/ /   | |  | ||  _  /   | |   |  __|   > <  ")
    print("    \  /    | |__| || | \ \   | |   | |____ / . \ ")
    print("     \/      \____/ |_|  \_\  |_|   |______/_/ \_\\")
    print("\n      [ VORTEX - Google Dork Automator ]")
    print("\033[0m")

def dork_menu():
    banner()
    target = input("\n\033[1;36m[?] Enter Target Domain (e.g. tesla.com): \033[0m")
    
    if not target:
        sys.exit()

    print("\n\033[1;33mSelect a Dork Type:\033[0m")
    print("1. Find SQL Files (Database Leaks)")
    print("2. Find Config Files (Passwords/Keys)")
    print("3. Find Admin Panels (Login Pages)")
    print("4. Find Exposed Documents (PDF/XLS)")
    print("5. Find Backup Files (.bak/.old)")
    print("0. Exit")

    choice = input("\n\033[1;36m[>] Selection: \033[0m")

    dork = ""
    if choice == '1':
        dork = f"site:{target} ext:sql | ext:dbf | ext:mdb"
    elif choice == '2':
        dork = f"site:{target} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ini | ext:env"
    elif choice == '3':
        dork = f"site:{target} inurl:admin | inurl:login | inurl:adminlogin | inurl:cpanel | inurl:portal"
    elif choice == '4':
        dork = f"site:{target} ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"
    elif choice == '5':
        dork = f"site:{target} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup"
    elif choice == '0':
        sys.exit()
    else:
        print("Invalid choice.")
        sys.exit()

    # Construct the URL
    final_url = f"https://www.google.com/search?q={dork}"
    
    print(f"\n\033[1;32m[+] Opening Google Dork for: {target}...\033[0m")
    print(f"URL: {final_url}")
    
    # Open Chrome/Firefox on the phone
    try:
        # In Termux, this calls the Android Intent to open the browser
        os.system(f"termux-open-url '{final_url}'") 
    except:
        # Fallback for PC/Kali
        webbrowser.open(final_url)

if __name__ == "__main__":
    dork_menu()

