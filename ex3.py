# Flávia Glenda e Lanna Kamilly
def calculadora_poupanca():
  
    valor_diario = float(input("Quanto você pode economizar por dia? R$ "))

    poupanca_anual = valor_diario * 365

    print(f"Se você economizar R$ {valor_diario:.2f} por dia, em 1 ano terá poupado R$ {poupanca_anual:.2f}.")

calculadora_poupanca()
