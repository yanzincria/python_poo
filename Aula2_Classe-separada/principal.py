#Estamos acessando o arquivo ´pesso.py´e dentro desse arquivo estamos importando a classe ´Pessoa`
from pessoa import Pessoa

#Criando objetos

p1 =Pessoa("Joana", "Correr", "Rua dos alfinetes 2121")
p1.exibirHobby()
p1.mudarHobby("Natação")

#Solicitando dados do usuario
nomePessoa = input("Informe o nome da pessoa: ")
hobbyPessoa = input("Informe o hobby da pessoa: ")
endPessoa =input("Informe o endereço da pessoa: ")

p2 = Pessoa(nomePessoa, hobbyPessoa, endPessoa)
p2.exibirHobby()

