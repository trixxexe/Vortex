import platform
import os
import sys
import shutil

def banner():
    os.system('clear')
    print("\033[1;37m") # White
    print("      [ VORTEX - System Forensics ]")
    print("\033[0m")

def sys_info():
    banner()
    uname = platform.uname()
    
    print(f"\n\033[1;33m[ SYSTEM ]\033[0m")
    print(f" System:    {uname.system}")
    print(f" Node Name: {uname.node}")
    print(f" Release:   {uname.release}")
    print(f" Version:   {uname.version}")
    print(f" Machine:   {uname.machine}")
    print(f" Processor: {uname.processor}")
    
    print(f"\n\033[1;33m[ STORAGE ]\033[0m")
    total, used, free = shutil.disk_usage("/")
    print(f" Total: {total // (2**30)} GiB")
    print(f" Used:  {used // (2**30)} GiB")
    print(f" Free:  {free // (2**30)} GiB")

    print(f"\n\033[1;33m[ USER ]\033[0m")
    print(f" Current User: {os.getlogin()}")
    print(f" PID:          {os.getpid()}")

if __name__ == "__main__":
    sys_info()

