import base64
import hashlib

ENCODING = 'utf-8'

# 将文件转换成字符串
def file2string(filename):
    with open(filename, 'rb') as f:
        content = f.read()
        return base64.urlsafe_b64encode(content).decode(ENCODING)

# 将字符串恢复成文件
def string2file(string, filename):
    byte = base64.urlsafe_b64decode(string.encode(ENCODING))
    with open(filename, 'wb') as w:
        w.write(byte)

# 将字符串转换成要传输的等长列表形式，n为传输长度
def string2msg(string, n=60):
    return (string[i:i+n] for i in range(0, len(string), n))

def file2md5(file):
    return hashlib.md5(open(file,'rb').read()).hexdigest()