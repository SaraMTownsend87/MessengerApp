from pickle import APPEND
import socket,select
from sqlite3 import connect

port = int(input("please input an open port:"))
socket_list = []
user = {}
print("running")
serverSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
serverSocket.bind(('',port))
serverSocket.listen(5)
socket_list.append(serverSocket)

while True:
    nowRead,nowWrite,error = select.select(socket_list,[],[],0) 
    for sock in nowRead:
        if sock == serverSocket:
            connect, addr = serverSocket.accept()
            socket_list.append(connect)
            connect.send("connection made at: "+str(addr))
        else:
            try:
                data = sock.recv(2048)
                if data.startswith("#"):
                    user[data[1:].lower()]=connect
                  
                    print 
                    "User " + data[1:] +" added."
                    connect.send("Your user detail saved as : "+str(data[1:]))
                
                elif data.startswith("@"):
                    user[data[1:data.index(':')].lower()].send(data[data.index(':')+1:])
            except:
                continue
    
