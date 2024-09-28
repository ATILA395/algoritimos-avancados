# Função principal
def soma_dos_maiores():
    # Leitura dos três valores
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    valor3 = float(input("Digite o terceiro valor: "))

    # Encontrar os dois maiores valores
    maior = max(valor1, valor2, valor3)  # Maior valor
    menor = min(valor1, valor2, valor3)  # Menor valor

    # Soma dos dois maiores
    soma = (valor1 + valor2 + valor3) - menor

    # Exibir a soma
    print("A soma dos dois maiores valores é:", soma)

# Chamada da função
soma_dos_maiores()
