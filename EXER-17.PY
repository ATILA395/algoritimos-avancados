# Função para calcular a média e verificar a aprovação
def verificar_aprovacao(nota1, nota2):
    # Calculando a média aritmética simples
    media = (nota1 + nota2) / 2
    
    # Determinando a situação do aluno
    if media >= 6:
        resultado = "aprovado"
    else:
        resultado = "não aprovado"
    
    # Exibindo a média e a situação do aluno
    print(f"A média das notas é: {media:.2f}")
    print(f"Com base nessa média, o aluno foi {resultado}.")

# Leitura das notas
nota1 = float(input("Digite a nota da 1ª avaliação: "))
nota2 = float(input("Digite a nota da 2ª avaliação: "))

# Verificar aprovação com base nas notas fornecidas
verificar_aprovacao(nota1, nota2)
