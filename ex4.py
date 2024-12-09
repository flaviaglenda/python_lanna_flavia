# Flávia Glenda e Lanna Kamilly
def converter_temperatura(): 
    print("Conversor de Temperatura") 
    print("1. Celsius para Fahrenheit") 
    print("2. Celsius para Kelvin") 

    opcao = int(input("Escolha uma opção (1 ou 2): ")) 
    celsius = float(input("Digite a temperatura em Celsius: ")) 

    if opcao == 1: 
        fahrenheit = (celsius * 9/5) + 32 
        print(f"{celsius}°C é igual a {fahrenheit:.2f}°F.") 

    elif opcao == 2: 
        kelvin = celsius + 273.15 
        print(f"{celsius}°C é igual a {kelvin:.2f}K.") 

    else: 
        print("Opção inválida.") 

converter_temperatura() 