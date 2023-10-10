def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite o número para a operação desejada: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    resultado = adicao(num1, num2)
elif escolha == '2':
    resultado = subtracao(num1, num2)
elif escolha == '3':
    resultado = multiplicacao(num1, num2)
elif escolha == '4':
    resultado = divisao(num1, num2)
else:
    resultado = "Escolha inválida. Por favor, selecione uma operação válida."

print(f"Resultado: {resultado}")
