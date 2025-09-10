def converter_dolar_real(valor):
    return valor * 5.8

def converter_real_dolar(valor):
    return valor / 5.8

converter = int(input("[Digite -> 1] - Converter Dólar para Real: \n[Digite -> 2] - converter Real para Dólar: "))
valor = float(input("Digite o valor para ser convertido: "))

if converter == 1:
    print(converter_dolar_real(valor))
elif converter == 2:
    print(converter_real_dolar(valor))
else:
    print("Valor inválido")