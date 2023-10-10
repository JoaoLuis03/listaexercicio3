palavra = input("Digite uma palavra: ")

contador_vogais = 0

palavra = palavra.lower()

for caractere in palavra:
    if caractere in "aeiou":
        contador_vogais += 1

print(f"A palavra digitada possui {contador_vogais} vogais.")
