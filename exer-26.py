# Função principal
def controle_estoque():
    # Leitura dos dados
    quantidade_atual = int(input("Digite a quantidade atual em estoque: "))
    quantidade_maxima = int(input("Digite a quantidade máxima em estoque: "))
    quantidade_minima = int(input("Digite a quantidade mínima em estoque: "))

    # Cálculo da quantidade média
    quantidade_media = (quantidade_maxima + quantidade_minima) / 2

    # Verificação da quantidade em estoque
    if quantidade_atual >= quantidade_media:
        print("Não efetuar compra")
    else:
        print("Efetuar compra")

# Chamada da função
controle_estoque()
