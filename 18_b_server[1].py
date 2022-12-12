import socket
s=socket.socket()
port=12345
s.bind(('',port))
print("socket binded to %s"%(port))
s.listen(5)
print ("socket is listening")
while True:
    c,addr=s.accept()
    print('Got Connection from',addr)
    c.send('Thank you for Connecting'.encode())
    c.close()
    break