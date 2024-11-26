# Flávia Glenda e Lanna Kamilly

import matplotlib.pyplot as plt

def gerar_grafico_temperaturas(temperaturas_maximas, temperaturas_minimas, dias):
    if len(temperaturas_maximas) != 7 or len(temperaturas_minimas) != 7:
        print("Erro: deve fornecer 7 dias de dados para temperaturas máximas e mínimas.")
        return

    x = range(7)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(x, temperaturas_maximas, width=0.4, label='Temperaturas Máximas', align='center', color='red')
    ax.bar(x, temperaturas_minimas, width=0.4, label='Temperaturas Mínimas', align='edge', color='blue')

    ax.set_xlabel('Dias')
    ax.set_ylabel('Temperatura (°C)')
    ax.set_title('Temperaturas Máximas e Mínimas dos Últimos 7 Dias')
    ax.set_xticks(x)
    ax.set_xticklabels(dias)

    ax.legend()


    plt.show()

dias = ['Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5', 'Dia 6', 'Dia 7']
temperaturas_maximas = [30, 32, 29, 31, 33, 34, 35]
temperaturas_minimas = [20, 21, 19, 20, 22, 23, 24]

gerar_grafico_temperaturas(temperaturas_maximas, temperaturas_minimas, dias)
