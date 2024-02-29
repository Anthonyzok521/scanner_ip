"""
    SCANNER OF IPs

"""
from colorama import init, Fore, Style
import socket
import nmap
import netifaces


init() #Initialize colorama

#Get ip of the device current witj socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('8.8.8.8', 0))

local_ip = sock.getsockname()[0] #IP
gateway = netifaces.gateways()[2][0][0] #Gateway
network = gateway.split('.')[:3] #Network
network = '.'.join(network) + '.0' #Format .0 end
sock.close()

#Show IPs
print(Style.BRIGHT + '-'*25)
print(Fore.GREEN + "Gateway: " + gateway)
print(Fore.CYAN + "network: " + network)
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
MSG = "Addresses"
print(Style.BRIGHT + Fore.GREEN)
print('-'*25)
print(f'{"|":<8}{msg}{"|":>8}')
print('-'*25)

#Table of divices scanners
def create_spaces(address_):
    """Create Spaces for separate the address

    Args:
        address_ (list): _description_

    Returns:
        int: return the number of spaces
    """
    if len(address_) == 15:
        return 3
    else:
        return abs(len(address_) -  15) + 3

for address in ips:
    spc = create_spaces(address)
    print("|", address, sep=" "*5, end=f'{" "*spc}|\n')
print('-'*25)
