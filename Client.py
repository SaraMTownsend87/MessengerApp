#from ipaddress import ip_address
import socket

socket_client = socket.socket()
port = int(input("please input an open port:"))
ip_address = input("please input an your ip Address:")
buffer_size = 1024
print("running")

socket_client.connect((ip_address,port))

receved_msg = socket_client.recv(buffer_size)
print(receved_msg)

msg_to_server = input("Enter Username")
socket_client.send(msg_to_server)

while True:
    receved_msg = socket_client.recv(buffer_size)
    print(receved_msg)

    msg_to_server = input("Send Message -> [@user:message]")
    if msg_to_server == 'exit' or 'Exit':
        break

    else:
        socket_client.send(msg_to_server)

print("goodbye")
socket_client.close()
