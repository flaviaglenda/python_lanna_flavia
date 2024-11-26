# Flávia Glenda e Lanna Kamilly
def cidade_com_maior_temperatura(dados_climaticos):

    cidade_mais_quente = None
    maior_temperatura = None

    for cidade, clima in dados_climaticos.items():
        if 'temperatura' in clima:
            if maior_temperatura is None or clima['temperatura'] > maior_temperatura:
                maior_temperatura = clima['temperatura']
                cidade_mais_quente = cidade

    return cidade_mais_quente or "Nenhuma cidade possui dados de temperatura."


dados = {
    "São Paulo": {"temperatura": 25, "umidade": 60, "vento": 15},
    "Rio de Janeiro": {"temperatura": 33, "umidade": 70, "vento": 10},
    "Belo Horizonte": {"temperatura": 28, "umidade": 65, "vento": 8}
}

resultado = cidade_com_maior_temperatura(dados)
print(f"A cidade com a maior temperatura é: {resultado}")
