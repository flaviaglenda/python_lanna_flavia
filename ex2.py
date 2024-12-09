# Flávia Glenda e Lanna Kamilly 
catastrofes = [ 
    {"nome": "Furacão Katrina", "tipo": "furacão", "intensidade": 9}, 
    {"nome": "Enchente do Vale do Rio Doce", "tipo": "enchente", "intensidade": 6}, 
    {"nome": "Furacão Irma", "tipo": "furacão", "intensidade": 8}, 
    {"nome": "Enchente de Blumenau", "tipo": "enchente", "intensidade": 7}, 
    {"nome": "Furacão Sandy", "tipo": "furacão", "intensidade": 7.5}, 
] 

eventos_filtrados = [] 

for evento in catastrofes: 
    if evento["intensidade"] > 7: 
        eventos_filtrados.append(evento) 

print("Eventos com intensidade maior que 7:") 
for evento in eventos_filtrados: 
    print(f"{evento['nome']} ({evento['tipo']}) - Intensidade: {evento['intensidade']}") 

 