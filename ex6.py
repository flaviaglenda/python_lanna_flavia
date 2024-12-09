# Flávia Glenda e Lanna Kamilly
def calcula_media_temperatura(temperaturas): 
    """Calcula a média de uma lista de temperaturas.""" 
    if len(temperaturas) == 0: 
        return 0  
    return sum(temperaturas) / len(temperaturas) 

medias_cidades = [] 

for i in range(1, 6):   
    print(f"Insira as temperaturas da cidade {i}, separadas por espaço:") 
    temperaturas = list(map(float, input().split()))  
    media = calcula_media_temperatura(temperaturas) 
    medias_cidades.append(media) 
    print(f"Média de temperatura da cidade {i}: {media:.2f}°C") 

print("\nMédias de temperatura das 5 cidades:") 
for i, media in enumerate(medias_cidades, 1): 
    print(f"Cidade {i}: {media:.2f}°C") 