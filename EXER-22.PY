def calcular_salario_total(horas_trabalhadas, salario_por_hora):
    horas_normais_por_semana = 40
    semanas_por_mes = 4
    percentual_acrescimo = 0.50

    horas_normais_por_mes = horas_normais_por_semana * semanas_por_mes

    if horas_trabalhadas > horas_normais_por_mes:
        horas_extras = horas_trabalhadas - horas_normais_por_mes
        valor_hora_extra = salario_por_hora * (1 + percentual_acrescimo)
        salario_total = (horas_normais_por_mes * salario_por_hora) + (horas_extras * valor_hora_extra)
    else:
        salario_total = horas_trabalhadas * salario_por_hora

    return salario_total

horas_trabalhadas = float(input("Digite o número total de horas trabalhadas no mês: "))
salario_por_hora = float(input("Digite o valor do salário por hora: "))


salario_total = calcular_salario_total(horas_trabalhadas, salario_por_hora)


print(f"O salário total do funcionário é: R$ {salario_total:.2f}")
