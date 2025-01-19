def # projeto-1
Projeto Escolar
def somar(a, b):
  return a + b

def subtrair(a, b):
  return a - b

def multiplicar(a, b):
  return a * b

def dividir(a, b):
  if b == 0:
    return "Divisão por zero não é permitida."
  else:
    return a / b

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite a operação (+, -, *, /): ")

if operador == '+':
  resultado = somar(num1, num2)
elif operador == '-':
  resultado = subtrair(num1, num2)
elif operador == '*':
  resultado = multiplicar(num1, num2)
elif operador == '/':
  resultado = dividir(num1, num2)
else:
  resultado = "Operador inválido"

print("Resultado:", resultado)

def somar(a, b):
  return a + b

def subtrair(a, b):
  return a - b

def multiplicar(a, b):
  return a * b

def dividir(a, b):
  if b == 0:
    return "Divisão por zero não é permitida."
  else:
    return a / b

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite a operação (+, -, *, /): ")

if operador == '+':
  resultado = somar(num1, num2)
elif operador == '-':
  resultado = subtrair(num1, num2)
elif operador == '*':
  resultado = multiplicar(num1, num2)
elif operador == '/':
  resultado = dividir(num1, num2)
else:
  resultado = "Operador inválido"

print("Resultado:", resultado)
