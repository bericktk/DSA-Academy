# Jogo da Forca(Hangman)
# Estudo da Programação Orientada a Objetos

# Import
import random

# Classe
class Hangman:

	# Método Construtor
     def __init__(self, palavra):
        self.palavra = palavra
        self.letras_acertadas = ['_'] * len(palavra)
        self.letras_erradas = []
        self.letras_adivinhadas = []

	# Método para adivinhar a letra
     def adivinhar_letra(self, letra):
        if letra in self.letras_adivinhadas:
            print("Você já tentou essa letra!")
        else:
            self.letras_adivinhadas.append(letra)
            if letra in self.palavra:
                for i in range(len(self.palavra)):
                    if self.palavra[i] == letra:
                        self.letras_acertadas[i] = letra
            else:
                self.letras_erradas.append(letra)    
	
	# Método para verificar se o jogo terminou
     def jogo_acabou(self):
        return '_' not in self.letras_acertadas or len(self.letras_erradas) == 6		
	# Método para verificar se o jogador venceu
     def exibir_situacao_do_jogo(self):
        print('Palavra: ', ' '.join(self.letras_acertadas))	
	# Método para não mostrar a letra no board
		
	# Método para checar o status do game e imprimir o board na tela
def jogar():
    palavras = ['laranja','maca','uva','banana']
    palavra_selecionada = random.choice(palavras)    
    jogo = Hangman(palavra_selecionada)
    while not jogo.jogo_acabou():
        jogo.exibir_situacao_do_jogo()
        letra = input('Digite uma letra: ')
        jogo.adivinhar_letra(letra)
    jogo.exibir_situacao_do_jogo()

jogar()
