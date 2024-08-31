# Função para calcular a média ponderada
def calcular_media_ponderada(n1, n2, n3):
    peso1 = 2
    peso2 = 3
    peso3 = 5
    soma_pesos = peso1 + peso2 + peso3
    media_final = (n1 * peso1 + n2 * peso2 + n3 * peso3) / soma_pesos
    return media_final

# Leitura das notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média ponderada
media = calcular_media_ponderada(nota1, nota2, nota3)

# Exibição da média final
print(f"A média final do aluno é: {media:.2f}")
