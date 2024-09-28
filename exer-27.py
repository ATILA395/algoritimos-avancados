# Função principal
def verificar_valor():
    # Leitura do valor
    valor = float(input("Digite um valor: "))

    # Verificação do valor
    if valor > 0:
        print("O valor é positivo.")
    elif valor < 0:
        print("O valor é negativo.")
    else:
        print("O valor é zero.")

# Chamada da função
verificar_valor()
