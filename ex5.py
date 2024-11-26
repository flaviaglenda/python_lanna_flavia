# Flávia Glenda e Lanna Kamilly
def calcular_media_e_mediana(niveis):
    soma = 0
    for nivel in niveis:
        soma += nivel
    media = soma / len(niveis)

    niveis_ordenados = sorted(niveis)
    meio = len(niveis_ordenados) // 2

    if len(niveis_ordenados) % 2 == 0:
        mediana = (niveis_ordenados[meio - 1] + niveis_ordenados[meio]) / 2
    else:
        mediana = niveis_ordenados[meio]

    return media, mediana


niveis_do_rio = [2.5, 3.0, 2.8, 3.2, 2.7, 2.9, 3.1, 3.3, 3.0, 2.8, 3.4, 2.6]

media, mediana = calcular_media_e_mediana(niveis_do_rio)

print(f"Média do nível do rio: {media:.2f} metros")
print(f"Mediana do nível do rio: {mediana:.2f} metros")

