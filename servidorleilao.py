
import socket
from threading import Thread, BoundedSemaphore
from random import randrange, seed
import time, sys
import linecache



HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50029
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4,tipo de socket
s.bind((HOST, PORT)) #liga o socket com IP e porta
usuarios ={}

print "esperando conexao"

def recebe_cliente(conn):
    while (1):
        dados = conn.recv(4096) #Recebe os dados 
        dados1 = dados.split (',') #coloca os dados em um vetor separando as posiçoes o que esta entre as virgulas
        print 'dados1=', dados1
        f = open("dados_dos_usuarios.txt",'w')
        f.write('Dados dos Usuários Cadastrados \n')
        f.write(str(dados1))
        f.close()
        if len(dados1) !=6 or dados1[0] != 'Adiciona_usuario': 
            print "dados1=",dados1
            print "Houve erro no envio de dados"
            conn.sendall("not_ok1")
            time.sleep(1)
            return
        elif dados1[1] in usuarios:
            print "Nome de usuario ja existente"
            conn.sendall("not_ok2")
            time.sleep(1)
            recebe_cliente(conn)
##      elif dados1[4] in usuarios: 
##          print "E-mail de usuario ja existente"
##          conn.sendall("not_ok3")
##          time.sleep(1)
##          recebe_cliente(conn)
        else:
            if dados1[1] not in usuarios:
                usuarios[dados1[1]]=[dados1[2],dados1[3],dados1[4],dados1[5],[],[]]
                print "Cliente inserido no sistema"
                print "Usuarios=",usuarios
                conn.sendall("ok")
                time.sleep(1)
                return

        

while(1):
    s.listen(1) #espera chegar pacotes na porta especificada
    conn, addr = s.accept()#mais uma conexão aceita
    print "Aceitou mais uma"
    t = Thread(target=recebe_cliente, args=(conn,))
    t.start()
    conn.close
    

    
    
