class Pessoa: 
    # Criar o método construtor
    #innit  - inicial
    def __init__(self, nome, altura, idade):
        #estamos criando os atributos da classe utilizando o método construtor.Nesse caso precisamos passar os parâmetros que serão usados como valores do atributos.
        self.nome = nome 
        self.altura = altura
        self.idade = idade 

    #criando os métodos
    def exibirDados(self):
        print(f"Olá {self.nome}, sua altura é {self.altura} e sua idade é {self.idade}")


#Criando os objetos 
p1 =Pessoa("Getúlio", 1.87 , 99)
p2 = Pessoa("Tatiana", 1.72 , 75)

p1.exibirDados()
p2.exibirDados()