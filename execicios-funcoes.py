# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números
def listaPar():
    for i in range(0, 21, 2):
        print(i)

listaPar()

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
def nome(texto):
    print(texto.upper())
    return
nome('Rumo a análise de dados')

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista
def elementos(elementos):
    print(elementos.append('fogo'))
    print(elementos.append('ar'))

elementos2 = ['terra', 'água']
elementos(elementos2)
print(elementos2)
