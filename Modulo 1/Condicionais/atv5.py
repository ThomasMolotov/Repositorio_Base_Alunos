noto1 = float(input("Primeira nota: "))
noto2 = float(input("Segunda nota: "))

medio = (noto1 + noto2) / 2

if medio == 10:
    print("Aprovado com Distinção")
elif medio >= 7:
    print("Aprovado")
else:
    print("Reprovado")