#Complete as funcoes a seguir

def soma(a, b):
	print ("Soma é: ", a+b)

def subtrai(a, b):
	print ("Subtração é: ", a-b)

def multiplica(a, b):
	print ("Multiplicação é: ", a*b)

def divide(a, b):
        if (b == 0):
            print("Não pode dividir por zero!")
        else:
            print("O resultado da divisão é: ", a / b)
	


#Programa principal
	

print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma(num1, num2)
subtrai(num1, num2)
multiplica(num1, num2)
divide(num1, num2)

