'''
@File    :   server.py
@Time    :   2020/11/29 12:40:23
@Author  :   Chengze Zhang 
@Contact :   chengze1996@gmail.com
@License :   Copyright (c) 2020 Chengze Zhang
@Desc    :   None
'''

# here put the import lib
import socket

address = ('127.0.0.1', 5005)  # 服务端地址和端口

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(address)  # 绑定服务端地址和端口
s.listen(5)

conn, addr = s.accept()  # 返回客户端地址和一个新的 socket 连接
print('[+] Connected with', addr)
while True:
    data = conn.recv(1024)  # buffersize 等于 1024
    data = data.decode()
    if not data:
        break
    print('[Received]', data)
    send = input('Input: ')
    conn.sendall(send.encode())
    
conn.close()
s.close()