# Função para determinar o vencedor
def determina_vencedor(time1, gols1, time2, gols2):
    if gols1 > gols2:
        return f"O vencedor é {time1}!"
    elif gols2 > gols1:
        return f"O vencedor é {time2}!"
    else:
        return "EMPATE"

# Ler os nomes dos times e os gols
time1 = input("Digite o nome do primeiro time: ")
gols1 = int(input(f"Digite o número de gols do {time1}: "))
time2 = input("Digite o nome do segundo time: ")
gols2 = int(input(f"Digite o número de gols do {time2}: "))

# Determinar e imprimir o resultado
resultado = determina_vencedor(time1, gols1, time2, gols2)
print(resultado)
