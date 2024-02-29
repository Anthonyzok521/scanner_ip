#Modules
import nmap                                                                             import socket
import netifaces
from colorama import *

init() #Initialize colorama

#Get ip of the device current witj socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('8.8.8.8', 0))

local_ip = sock.getsockname()[0] #IP
gateway = netifaces.gateways()[2][0][0] #Gateway
red = gateway.split('.')[:3] #Network
red = '.'.join(red) + '.0' #Format .0 end
sock.close()

#Show IPs
print(Style.BRIGHT + '-'*25)                                                            print(Fore.WHITE + "IP local: " + local_ip)
print(Fore.GREEN + "Gateway: " + gateway)
print(Fore.CYAN + "Red: " + red)
print('-'*25)
print(Style.NORMAL + Fore.WHITE)

scanner =  nmap.PortScanner()

msg = input("Scan current red? Y/n: ")

print(Fore.YELLOW)
print('Scanning...')
if not msg or msg.upper()  == "Y":
    scanner.scan(f'{gateway}/24', timeout=30)

else:
    ip = input("Enter a ip with mac /8, /16  or /24: ")
    scanner.scan(ip, timeout=30)


ips = scanner.all_hosts()
msg = "Addresses"
print(Style.BRIGHT + Fore.GREEN)
print('-'*25)
print(f'{"|":<8}{msg}{"|":>8}')
print('-'*25)

#Table of divices scanners
spc = 0
def createSpaces(ip):
    if len(ip) == 15:                                                                           return 3
    else:
        return abs(len(ip) -  15) + 3

for ip in ips:
    spc = createSpaces(ip)
    print("|", ip, sep=" "*5, end=f'{" "*spc}|\n')
print('-'*25)
~
