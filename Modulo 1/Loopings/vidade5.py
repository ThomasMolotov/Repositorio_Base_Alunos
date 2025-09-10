while True:
    pa = float(input("Digite a papulação A: "))
    if pa > 1000:
        break
    print("Valor inválido")

while True:
    p100a = float(input("Digite a taxa de crescimento A: "))
    if p100a < 10:
        break
    print("Valor inválido")

while True:
    pb = float(input("Digite a papulação B: "))
    if pb > 1000:
        break
    print("Valor inválido")

while True:
    p100b = float(input("Digite a taxa de crescimento B: "))
    if p100b < 10:
        break
    print("Valor inválido")

anos = 0

while pa < pb:
    pa *= (1 + p100a)
    pb *= (1 + p100b)
    anos += 1

print(f"Será necessário {anos} anos")