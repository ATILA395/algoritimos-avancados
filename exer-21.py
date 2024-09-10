def calcular_duracao(h_i, h_f):
    if h_f >= h_i:
        return h_f - h_i
    else:
        return (24 - h_i) + h_f

# Solicita as horas de início e fim ao usuário
hora_inicio = int(input("Digite a hora de início (0 a 23): "))
hora_fim = int(input("Digite a hora de fim (0 a 23): "))

# Verifica se as horas fornecidas são válidas
if 0 <= hora_inicio <= 23 and 0 <= hora_fim <= 23:
    duracao = calcular_duracao(hora_inicio, hora_fim)
    print(f"A duração do jogo é: {duracao} horas")
else:
    print("Por favor, insira horas válidas (de 0 a 23).")
