# import socket

# HOST = '127.0.0.1'
# PORT = 8000
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
# s.connect((HOST, PORT))  # 要连接的IP与端口
# s.sendall("你好".encode(encoding="utf-8"))  # 把命令发送给对端
# data = s.recv(1024)  # 把接收的数据定义为变量
# print(type(data))
# print(data.decode())  # 输出变量
# s.close()  # 关闭连接

import socket
import Utils


class TouchEvent:
    def __init__(self, x, y, action):
        self.x = x
        self.y = y
        self.action = action

    def __repr__(self):
        return 'TouchEvent X : %s , Y : %d' % (self.x, self.y)


if __name__ == '__main__':
    p = TouchEvent(10, 22, 1)
    print(p)
    q = Utils.toJsonStr(p)
    print(q)
    print(type(q))

    HOST = '127.0.0.1'
    PORT = 8000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
    s.connect((HOST, PORT))  # 要连接的IP与端口
    s.sendall("CONNECT_GET_RULES".encode(encoding="utf-8"))  # 把命令发送给对端
    data = s.recv(1024)  # 把接收的数据定义为变量
    print(type(data))
    print(data.decode())  # 输出变量
    s.close()  # 关闭连接
