import hashlib
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
    print("\n      [ VORTEX - Hash Identifier & Cracker ]")
    print("\033[0m")

def identify_hash(h):
    l = len(h)
    if l == 32: return "MD5"
    if l == 40: return "SHA1"
    if l == 64: return "SHA-256"
    if l == 96: return "SHA-384"
    if l == 128: return "SHA-512"
    return "Unknown"

def crack_md5(target_hash):
    print(f"\n\033[1;33m[*] Attempting to crack MD5: {target_hash}...\033[0m")
    
    # A mini wordlist built-in (The most common passwords)
    wordlist = ["password", "123456", "12345678", "123456789", "qwerty", "admin", "admin123", "pass123", "google", "iloveyou"]
    
    for word in wordlist:
        # Hash the word
        hashed_word = hashlib.md5(word.encode()).hexdigest()
        
        if hashed_word == target_hash:
            print(f"\n\033[1;32m[+] CRACKED SUCCESS: {target_hash} == {word}\033[0m")
            return
            
    print("\033[1;31m[-] Failed to crack with mini-list. Use a real wordlist (rockyou.txt).\033[0m")

def main():
    banner()
    target_hash = input("\n\033[1;36m[?] Enter Hash String: \033[0m").strip()
    
    if not target_hash:
        sys.exit()

    htype = identify_hash(target_hash)
    print(f"\n\033[1;37m[+] Detected Hash Type: \033[1;32m{htype}\033[0m")
    
    if htype == "MD5":
        crack = input("\n[?] Do you want to try to crack it? (y/n): ")
        if crack.lower() == 'y':
            crack_md5(target_hash)

if __name__ == "__main__":
    main()

