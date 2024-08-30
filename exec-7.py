from datetime import datetime

def calcular_idade(data_nascimento, data_atual):
    # Calcula a diferença em anos
    anos = data_atual.year - data_nascimento.year
    # Ajusta se o aniversário ainda não ocorreu este ano
    if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
        anos -= 1
    
    # Calcula a diferença em meses
    meses = data_atual.month - data_nascimento.month
    if data_atual.day < data_nascimento.day:
        meses -= 1
    if meses < 0:
        meses += 12
    
    # Calcula a diferença em dias
    if data_atual.day >= data_nascimento.day:
        dias = data_atual.day - data_nascimento.day
    else:
        # Se o dia do mês atual é menor que o dia do mês de nascimento
        ultimo_dia_mes_anterior = (data_atual.replace(day=1) - timedelta(days=1)).day
        dias = ultimo_dia_mes_anterior - data_nascimento.day + data_atual.day

    return anos, meses, dias

# Exemplo de uso
data_nascimento = datetime(2002, 10, 19)
data_atual = datetime(2024, 8, 30)

anos, meses, dias = calcular_idade(data_nascimento, data_atual)
print(f"Idade: {anos} anos, {meses} meses e {dias} dias")
