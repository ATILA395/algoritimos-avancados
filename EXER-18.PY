# Função para verificar se a pessoa pode votar
def verificar_aptidao_para_voto(ano_atual, ano_nascimento):
    idade = ano_atual - ano_nascimento
    
    # Verificar se a pessoa pode votar
    if idade >= 16:
        resultado = "pode votar"
    else:
        resultado = "não pode votar"
    
    # Exibindo o resultado
    print(f"Com base no ano de nascimento {ano_nascimento} e no ano atual {ano_atual}, a pessoa {resultado} este ano.")

# Leitura do ano atual e do ano de nascimento
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Verificar se a pessoa pode votar
verificar_aptidao_para_voto(ano_atual, ano_nascimento)
