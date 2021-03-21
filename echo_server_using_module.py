import MyTCPServer as my
port = 2500
BUFSIZE = 1024
sock = my.TCPServer(port)

while True:
    conn, addr = sock.Accept()
    print('connected by', addr)
    data = conn.recv(BUFSIZE)
    if not data:
        break
    print("Received message: ", data.decode())
    conn.send(data)
conn.close()
