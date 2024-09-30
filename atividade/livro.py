class Livro:
    #Método Construtor
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor =autor
        self.anoPublicacao = anoPublicacao
    
     #Criando Métodos
    def exibirInformacoes(self):
        print(f"O livro {self.titulo}, do autor {self.autor}  foi publicado {self.anoPublicacao}") 

    def  verificarIdadeLivro (self):
        if  (2024 -self.anoPublicacao )>50:
            print("Este livro é um clássico")
        elif (2024 -self.anoPublicacao )<50:
            print("Ainda não é considerado clássico")
       