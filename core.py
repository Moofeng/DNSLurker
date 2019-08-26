import base64

ENCODING = 'utf-8'

# ���ļ�ת�����ַ���
def file2string(filename):
    with open(filename, 'rb') as f:
        content = f.read()
        return base64.b64encode(content).decode(ENCODING)

# ���ַ����ָ����ļ�
def string2file(string, filename):
    byte = base64.b64decode(string.encode(ENCODING))
    with open(filename, 'wb') as w:
        w.write(byte)

# ���ַ���ת����Ҫ����ĵȳ��б���ʽ��nΪ���䳤��
def string2msg(string, n=60):
    return (string[i:i+n] for i in range(0, len(string), n))

