numero = int(input("Digite um número inteiro positivo: "))
if numero < 0:
    print("O fatorial não está definido para números negativos.")
else:
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    print(f'O fatorial de {numero} é {resultado}.')