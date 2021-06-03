import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('',5555))
    print(s.getsockname())
    s.listen()
    conn,addr=s.accept()
    with conn:
        print('Client:',addr)
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(data)

    

