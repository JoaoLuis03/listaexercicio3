escolha = input("Digite 1 para converter de Celsius para Fahrenheit ou digite 2 para converter de Fahrenheit para Celsius: ")

if escolha == '1':
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit.")
elif escolha == '2':
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} graus Fahrenheit é igual a {celsius} graus Celsius.")
else:
    print("Escolha inválida. Por favor, selecione 1 ou 2 para a conversão desejada.")