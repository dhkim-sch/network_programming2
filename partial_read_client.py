from socket import *
sock = create_connection(('localhost', 9999))
data_size = 20  #수신할 데이터의 크기
rx_size = 0
total_data = []
while rx_size < data_size:
    data = sock.recv(4) #최대 4바이트 수신하도록 설정
    if not data:
        break
    rx_size += len(data)
    total_data.append(data.decode())
    print(total_data)
    
message = ''.join(total_data)
print(message)
sock.close()