import zipfile
import sys
import os

def banner():
    os.system('clear')
    print("\033[1;31m") # Red for Danger
    print("      [ VORTEX - Zip Lock Breaker ]")
    print("\033[0m")

def crack_zip():
    banner()
    zip_file = input("\n\033[1;36m[?] Enter path to .zip file: \033[0m")
    pass_file = input("\033[1;36m[?] Enter path to wordlist (e.g. rockyou.txt): \033[0m")

    if not os.path.exists(zip_file) or not os.path.exists(pass_file):
        print("\033[1;31m[!] File not found.\033[0m")
        sys.exit()

    print(f"\n\033[1;33m[*] Attacking {zip_file}...\033[0m")

    zip_obj = zipfile.ZipFile(zip_file)
    n_words = len(list(open(pass_file, "rb")))
    
    print(f"[*] Total passwords to try: {n_words}")

    with open(pass_file, "rb") as wordlist:
        for word in wordlist:
            try:
                password = word.strip()
                zip_obj.extractall(pwd=password)
                print(f"\n\033[1;32m[+] PASSWORD FOUND: {password.decode()}\033[0m")
                print(f"[+] Files extracted successfully.")
                return
            except:
                continue
    
    print("\n\033[1;31m[-] Password not found in list.\033[0m")

if __name__ == "__main__":
    crack_zip()

