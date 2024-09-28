# Função principal
def ordenar_valores():
    # Leitura dos três valores
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    valor3 = float(input("Digite o terceiro valor: "))

    # Criar uma lista com os valores
    valores = [valor1, valor2, valor3]

    # Ordenar a lista
    valores.sort()

    # Exibir os valores em ordem crescente
    print("Os valores em ordem crescente são:", valores)

# Chamada da função
ordenar_valores()
