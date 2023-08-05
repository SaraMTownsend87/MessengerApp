import socket, pyaes, pbkdf2, os, secrets

###### AES Setup ######

password = "U9ZPPipbJi"
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(password,passwordSalt).read(32)
initial_vector = secrets.randbits(256)

###### Encrypt Plaintext ######
def encrypt_AES(plaintext):
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(initial_vector))
    ciphertext = aes.encrypt(plaintext)
    return ciphertext

###### Decrypt Ciphertext ######

def decrypt_AES(ciphertext_inbound):
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(initial_vector))
    plaintext_dycrypted = aes.decrypt(ciphertext_inbound)
    return  plaintext_dycrypted

###### Messanger Setup ######

port = int(input("please input an open port:"))
ip_address = input("please input an your ip Address:")
buffer_size = 1024
print("running")
socket_client = socket.socket()
socket_client.connect((ip_address,port))

receved_msg = socket_client.recv(buffer_size)
print(receved_msg)

msg_to_server = input("Enter Username")
socket_client.send(msg_to_server)

while True:
    receved_encrypted_msg = socket_client.recv(buffer_size)
    recived_msg = decrypt_AES(receved_encrypted_msg)
    print(receved_msg)


    msg_to_server = input("Send Message -> (@user:message)")
    if msg_to_server == "exit" or "Exit":
        break

    else:
        ### AES Encrytion
        encrypted_msg_to_server = encrypt_AES(msg_to_server)
        socket_client.send(encrypted_msg_to_server)

print("goodbye")
socket_client.close()
