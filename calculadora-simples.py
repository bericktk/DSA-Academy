#Crie uma calculadora simples que realizar as 4 operações matemáticas
#1- Deseje Boas Vindas ao usuário;
#2- Peça ao usuário que digite o primeiro valor;
#3- Peça ao usuário que digite o segundo valor;
#4- Peça ao usuário que escolha qual operação matemática ele deseja fazer;
#5- Apresente o resultado ao usuário;

print("Olá, seja Bem Vindo!")
  
num1 = float(input("Digite o valor do primeiro número: "))
num2 = float(input("Digite o valor do segundo número: "))
operacao = (input("Selecione a operação desejada: +, -, *, / "))

if operacao == "+":
    resultado = num1 + num2
    print("O resultado é: ", resultado)

elif operacao == "-":
    resultado = num1 - num2
    print("O resultado é: ", resultado)
    
elif operacao == "*":
    resultado = num1 * num2
    print("O resultado é: ", resultado)
    
elif operacao == "/":
    resultado = num1 / num2
    print("O resultado é: ", resultado)
    
else:
    print("Operação inválida, tente novamente!")
