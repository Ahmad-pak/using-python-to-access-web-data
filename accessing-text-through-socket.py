import socket

mysocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org',80))
#connection is established know time for sending request
command= 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(command)

#this loop will keep running till whole file recieved
while True:
    data=mysocket.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysocket.close()
