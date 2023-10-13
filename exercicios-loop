# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
dia = {'segunda':2, 'terça':3, 'quarta':4, 'quinta':5, 'sexta':6}
descanso = {'domingo':1, 'sabado':7}

print(dia)
print(descanso)

hoje = input("Digite o dia da semana hoje: ")

if hoje in ["2", "3", "4", "5", "6"]:
    print("Você precisa trabalhar!")
    
elif hoje in ["1", "7"]:
    print("Hoje é dia de descanso")
    
else:
    print("Opção inválida")

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
lista = ['banana', 'manga', 'maçã', 'melão', 'morango']

for fruta in lista:
    if fruta == 'morango':
        print("Tem morango")

# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista
tup = (1, 2, 3, 4)
list1 = []

for i in tup:
    valor = i * 2
    list1.append(valor)

print(list1)

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for i in range(100,151,2):
    print(i)

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela
temperatura = 40

while temperatura > 35:
    print(temperatura)
    temperatura = temperatura - 1

# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
contador = 0

while contador < 100:
    if contador == 23:
        break
    else:
        print(contador)
        contador += 1

# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
par = list()
x = 4

while (x <= 20):
    par.append(x)
    x = x + 2
print(par)

# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
num = range(5, 45, 2)
print(list(num))

# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura >= 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.” 

frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão."
count = 0

for caracter in frase:
    if caracter == 'r':
        count += 1
print("O R aparece %s vezes na frase" %(count))
