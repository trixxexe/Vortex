import qrcode
import sys
import os

def banner():
    os.system('clear')
    print("\033[1;35m")
    print(" [ VORTEX - Quick Response (QR) Generator ]")
    print("\033[0m")

def generate():
    banner()
    data = input("\n\033[1;36m[?] Enter text/url to encode: \033[0m")
    if not data: sys.exit()
    
    qr = qrcode.QRCode(border=1)
    qr.add_data(data)
    qr.make(fit=True)
    
    print("\n\033[1;32m")
    qr.print_ascii(invert=True)
    print("\033[0m")

if __name__ == "__main__":
    generate()

