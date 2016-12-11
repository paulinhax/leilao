import socket
import random
from threading import Thread, BoundedSemaphore
from random import randrange, seed, shuffle
import time, sys


HOST = '127.0.0.1'   # Symbolic name meaning all available interfaces
PORT = 50029




def cadastro():

    while (True):
        nome = raw_input ("Informe seu nome de cadastro: ")
        n_tel= raw_input ("Informe seu numero de telefone: ")
        end= raw_input("Informe seu endereco: ")
        email= raw_input ("Informe seu e-mail: ")
        senha= raw_input ("Informe sua senha: ")

    
        s.sendall("Adiciona_usuario,"+nome+","+n_tel+","+end+","+email+","+senha)
          #enviando os dados para o servidor

        print 'enviando dados'

        data=s.recv(4096)
        if data == "not_ok1":
            print "Houve erro no envio de dados, por favor escreva novamente o cadastro: "
            break
        elif data == "not_ok2":
            print "Nome de usuario ja existente, por favor refaca seu cadastro "
            cadastro()
##      elif data == "not_ok3":
##          print "E-mail de usuario ja existente, por favor refaca seu cadastro "
##          cadastro()
        else:
            print "Cadastro realizado com sucesso"
            break    


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4,tipo de socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST, PORT))
print "conexao feita"

cadastro()
s.close
