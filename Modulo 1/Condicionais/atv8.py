pro1 = float(input("Produto 1: R$"))
pro2 = float(input("Produto 2: R$"))
pro3 = float(input("Produto 3: R$"))

if pro1 < pro2 and pro1 < pro3:
    print(f"Leve o que custa: R${pro1}")
elif pro2 < pro1 and pro2 < pro3:
    print(f"Leve o que custa: R${pro2}")
elif pro3 < pro1 and pro3 < pro2:
    print(f"Leve o que custa: R${pro3}")