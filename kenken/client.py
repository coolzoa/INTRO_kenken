import socket


s = socket.socket()
host = socket.gethostname()
port = 9999


s.connect((host,port))

while True:
        message = input('Mensaje: ')
        s.send(message.encode("utf-8"))
        print('Espero respuesta')
        reply = s.recv(1024).decode("utf-8")
        print('Recibido',reply)

s.close()
