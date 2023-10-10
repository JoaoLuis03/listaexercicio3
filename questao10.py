def sequencia_fibonacci(n):
    fibonacci = [0, 1]

    while len(fibonacci) < n:
        proximo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo)

    return fibonacci
n_termos = int(input("Digite um número: "))
resultado = sequencia_fibonacci(n_termos)
print("Sequência de Fibonacci:")
for termo in resultado:
    print(termo)
