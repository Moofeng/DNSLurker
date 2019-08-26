import dns.message
import socket


receive_list = []
tmp = ''

def handler(address, message):
    msg = dns.message.from_wire(message)
    name = msg.question[0].name
    name = str(name).split('.')[0]
    global tmp
    if name == tmp:
        pass
    else:
        print(name)
        receive_list.append(name)
        tmp = name
    resp = dns.message.make_response(msg)
    s.sendto(resp.to_wire(), address)



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 53))
print("[+] I'm listening ...")
while True:
    message, address = s.recvfrom(1024)
    handler(address, message)

