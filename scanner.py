'''python port scanner to scsn the range of open ports in system'''
#import needed modules
from colorama import Fore
import socket
from datetime import datetime
import sys
import time

#define the target and implement algorithms
if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1])
        #add banners to makeit look pretty
        
        print("=" * 50)
        print(f"Start scanning of {target}")
        print(f"Time started @: {datetime.now()}")
    except Exception as e:
        print("exception has occoured")
else:
    print("incorrect argument. synthax: python3 scanner.py <ip>")            
print("=" * 50)

try:
    for port in range(50, 100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        time.sleep(1)
        if result == 0:
            print("=" * 20)
            print("[+] port " + str(port) + " is open")
            print("=" * 20)
        else:
            print("=" * 20)
            print(f"[+] port {port} is close")
            print("=" * 20)    
        s.close()
except KeyboardInterrupt:
    print("\Exiting program")
    sys.exit()
except socket.error:
    print("socket cant connect to port")                     
    sys.exit()    
except socket.error:
    print("couldnt connect to server")
    sys.exit(1)    
