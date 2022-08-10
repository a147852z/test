# -*- coding=utf-8 -*-
import base64
import socket
from pathlib import Path
from socket import *
import numpy as np
import cv2
import base64
import socket

def client():
        s = socket.socket(AF_INET, SOCK_STREAM)
        s.connect(('192.168.56.1', 5612))
        filepath = r'C:\Users\Gslab\Desktop\123.png'
        with open(filepath, 'rb') as fp:
            data = fp.read()
        s.send(data)
        s.close()
    

def server():
    HOST = ''
    PORT = 9999
    BUFSIZ = 1024*20
    ADDR = (HOST, PORT)
    tcpSerSock = socket.socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
    while True:
        rec_d = bytes([])
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('...connected from:', addr)
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data or len(data) == 0:
                break
            else:
                rec_d = rec_d + data
        rec_d = base64.b64decode(rec_d)
        np_arr = np.frombuffer(rec_d, np.uint8)
        image = cv2.imdecode(np_arr, 1)
        cv2.imwrite('./55555.jpg',image)
        cv2.imshow('image', image)
        cv2.waitKey(0)
        tcpCliSock.sendall("完成".encode("utf-8"))#數字與英文就用b''中文用.encode("utf-8")
        tcpCliSock.close()
    tcpSerSock.close()

if __name__ == "__main__":
    name = input("輸入server為伺服器模式\n輸入client為客戶端模式\n請輸入:")
    while True:
        if name == "server":
            server()
        elif name =="client":
            client()
        else:
            name = input("輸入錯誤請重新輸入:")

