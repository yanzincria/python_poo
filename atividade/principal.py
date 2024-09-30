#Estamos acessando o arquivo ´pesso.py´e dentro desse arquivo estamos importando a classe ´Pessoa`
from livro import Livro

#Criando objetos

l1 =Livro("Harry Potter", "Thomas Shelby",2015)
l1.exibirInformacoes()
l1.verificarIdadeLivro()

l2 = Livro("joão e botas", "Antônio Montenegro" , 1920)
l2.exibirInformacoes()
l2.verificarIdadeLivro()