# Flávia Glenda e Lanna Kamilly
def classificar_desastre(tipo, intensidade):
    if intensidade < 3:
        categoria = "Baixo Impacto"
    elif intensidade < 6:
        categoria = "Médio Impacto"
    else:
        categoria = "Alto Impacto"

    return f"O desastre {tipo} com intensidade {intensidade} foi classificado como: {categoria}"

desastres = [
    "Tremor de terra",
    "Tsunami",
    "Deslizamentos",
    "Ciclones",
    "Tempestade",
    "Onda de Calor"
]

for desastre in desastres:
    print(f"\nClassificação do desastre: {desastre}")
    intensidade = float(input("Digite a intensidade do desastre (de 0 a 10): "))
    resultado = classificar_desastre(desastre, intensidade)
    print(resultado)
