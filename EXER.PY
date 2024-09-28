def verificar_resposta(x, y):
    z = (x + y) + 5

    if z <= 0:
        return "A"
    elif z <= 100:
        return "B"
    else:
        return "C"

# Testes
testes = [
    (-10, -5),  # Espera "A"
    (20, 50),   # Espera "B"
    (200, -100) # Espera "C"
]

for x, y in testes:
    resposta = verificar_resposta(x, y)
    print(f"Entrada: x = {x}, y = {y} => Saída: {resposta}")
