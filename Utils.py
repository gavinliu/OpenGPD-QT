import json
import socket


def toJsonStr(obj):
    # convert object to a dict
    d = {}
    # d['__class__'] = obj.__class__.__name__
    # d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return json.dumps(d, sort_keys=True)


def jsonStrToObject(obj):
    return json.loads(obj)


# adb forward tcp:8000 tcp:9000
# adb forward tcp:8001 tcp:9001

def getRules():
    HOST = '127.0.0.1'
    PORT = 8001
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
    s.connect((HOST, PORT))  # 要连接的IP与端口
    s.sendall("ACTION_GET_RULES".encode(encoding="utf-8"))  # 把命令发送给对端
    data = ""
    while True:
        try:
            buf = s.recv(1024).decode("utf-8")
            data = data + buf
            if not len(buf):
                break
        except Exception as e:
            print(e)
    s.close()  # 关闭连接
    return data

def sendMSG(message):
    HOST = '127.0.0.1'
    PORT = 8000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
    s.connect((HOST, PORT))  # 要连接的IP与端口
    s.sendall(message.encode(encoding="utf-8"))  # 把命令发送给对端
    data = ""
    while True:
        try:
            buf = s.recv(1024).decode("utf-8")
            data = data + buf
            if not len(buf):
                break
        except Exception as e:
            print(e)
    s.close()  # 关闭连接
    pass
