import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999


s.bind((host,port))
s.listen(1)
sc,addr = s.accept()

while True:
    
    print(addr,'se ha conectado')
 
    
    recibido = sc.recv(1024).decode("utf-8")
    print ("Amigo: ", recibido)
    
    if True != True:
      print("hello world")
    else:
        mensaje = input("Mensaje a enviar >> ")
        print("Yo:",mensaje)
    sc.send(mensaje.encode("utf-8"))
print ("Adios.")
        
    
        
sc.close()
s.close()

