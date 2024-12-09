# Flávia Glenda e Lanna Kamilly 
import csv
from collections import defaultdict

def calcular_media_mensal(arquivo_csv):
    temperaturas_por_mes = defaultdict(list)
    
    # Ler o arquivo CSV
    with open(arquivo_csv, mode='r') as arquivo:
        leitor_csv = csv.DictReader(arquivo)  
        
        for linha in leitor_csv:
            data = linha['Data']
            temperatura = float(linha['Temperatura'])  
            mes = data[:7]  

            temperaturas_por_mes[mes].append(temperatura)
    
    medias_mensais = {}
    for mes, temperaturas in temperaturas_por_mes.items():
        medias_mensais[mes] = sum(temperaturas) / len(temperaturas)
    
    return medias_mensais

arquivo = 'dados_climaticos.csv'

medias = calcular_media_mensal(arquivo)

print("Médias mensais de temperatura:")
for mes, media in medias.items():
    print(f"{mes}: {media:.2f}°C")
