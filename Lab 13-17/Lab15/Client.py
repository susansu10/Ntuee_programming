import socket

HOST = '127.0.0.1'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# outdata = 'hello I am client'
# print('send: ' + outdata)
# s.send(outdata.encode())

# indata = s.recv(1024)
# print('Clent recv from Server : ' + indata.decode())

while True:
    message = input('C - Please Entering input >>> ')
    s.send(message.encode())

    if message == 'ByeBye':
        print("Sent 'ByeBye' to the server. Closing the connection.")
        s.close()
        break

    indata = s.recv(1024)
    print(indata.decode())

    if indata.decode() == 'ByeBye':
        print("Server said 'ByeBye'. Closing the connection.")
        s.close()
        break


s.close()