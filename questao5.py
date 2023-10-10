def primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False

    for i in range(5, int(numero**0.5) + 1, 6):
        if numero % i == 0 or numero % (i + 2) == 0:
            return False

    return True

numero = int(input("Digite um número: "))

if primo(numero):
    print(f'{numero} é um número primo.')
else:
    print(f'{numero} não é um número primo.')