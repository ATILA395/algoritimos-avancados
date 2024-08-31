# Passo 1: Ler a temperatura em Fahrenheit
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Passo 2: Calcular a temperatura em Celsius
celsius = (5 / 9) * (fahrenheit - 32)

# Passo 3: Exibir o resultado
print(f"A temperatura em graus Celsius é: {celsius:.2f}")
