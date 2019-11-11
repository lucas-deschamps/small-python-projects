# a small program that prints out all prime numbers in a user-defined range.
# written for a college assignment.

numeros_primos = []
numero_inicial = int(input("\nDigite o número inicial: \n"))
numero_final = int(input("Digite o número final: \n"))
range_primos = range(numero_inicial, numero_final)

print(f"\n\t\t\t[Números primos entre {numero_inicial} e {numero_final}.]\n")

for numero in range_primos:
    if numero > 1:
        for divisor in range(2, numero):
            if numero % divisor == 0:
                break
        else:
            numeros_primos.append(numero)

print(f"Números primos: {numeros_primos}")
print("\nNúmeros primos são os números somente divisíveis por si mesmos e 1.")
