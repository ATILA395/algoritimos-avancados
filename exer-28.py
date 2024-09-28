# Função principal
def encontrar_maior():
    # Leitura dos três valores
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    valor3 = float(input("Digite o terceiro valor: "))

    # Encontrar o maior valor
    maior = valor1  # Assume que o primeiro valor é o maior

    if valor2 > maior:
        maior = valor2
    if valor3 > maior:
        maior = valor3

    # Exibir o maior valor
    print("O maior valor é:", maior)

# Chamada da função
encontrar_maior()
