#Projeto 1 - Desenvolvimento do Jogo da Forca em Linguagem Python - Versão 1
#imports
import random
from os import system, name

#Função para limpar a tela a cada execução
def limpar_tela():
  #windows
  if name == 'nt':
    _ = system('cls')

  #Mac ou Linux
  else:
    _ = system('clear')

#Função
def game():
    limpar_tela()
    print("\n Bem Vindo ao Jogo da Forca!")
    print("Adivinhe a palavra abaixo:\n")

    #Lista de palavras para o game
    palavras = ['banana', 'abacate', 'morango', 'uva', 'laranja']
    palavra = random.choice(palavras)

    #List Comprehension
    letras_descobertas = ['_' for letra in palavra]

    #Número de chances
    chances = 6

    #Lista pra Letras Erradas
    letras_erradas = []

    #Loop enquanto número de chances for maior do que zero
    while chances > 0:
        #Print
        print(" ".join(letras_descobertas))
        print("\nChances Restantes: ", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        #Tentativa
        tentativa = input("\nDigite uma Letra: ").lower()

        #condição
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        #condição 2
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era: ", palavra)
            break

    #condição 3
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era: ", palavra)

#Bloco Main
if __name__ == "_main_":
    game()
    print("\nParabéns você está aprendendo Python!!\n")
