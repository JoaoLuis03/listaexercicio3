soma = 0
numero = int(input("Digite um número inteiro positivo: "))
while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10 
   
print(f'A soma dos dígitos é: {soma}')