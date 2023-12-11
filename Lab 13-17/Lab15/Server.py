import socket

# '127.0.0.1' is a special IP address which is means 'localhost'
HOST = '127.0.0.1'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

state = 0
while True:
    conn, addr = s.accept()
    print('connected by ' + str(addr))

    # indata = conn.recv(1024)
    # print('recv: ' + indata.decode())

    # outdata = 'encode' + indata.decode()
    # conn.send(outdata.encode())
    # conn.close()
    
    while True:
        indata = conn.recv(1024)
        print(indata.decode())

        if indata.decode() == 'ByeBye':
            print("Client said 'ByeBye'. Closing the connection.")
            conn.close()
            state = 1
            break

        message = input('S - Please Entering input >>> ')
        conn.send(message.encode())

        if message == 'ByeBye':
            print("Sent 'ByeBye' to the client. Closing the connection.")
            conn.close()
            state = 1
            break
        
    if state == 1:
        break

s.close()