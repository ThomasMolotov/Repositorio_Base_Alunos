import random

def somadados():
    d1 = random.randint(1,7)
    d2 = random.randint(1,7)
    soma = d1 + d2
    print(f"Lançou os dados: {d1} + {d2} = {soma}")
    return soma

def jogo():
    print("Começou!!")

    lancou = somadados()

    if lancou in (7, 11):
        print("Você ganhou!")
        return
    elif lancou in (2, 3, 12):
        print("Você perdeu")
        return
    else:
        ponto = lancou
        print(f"Seu ponto é {ponto}. Continue jogando até tirá-lo novamente.")

    while True:
        input("Precione Enter para lançar novamente")
        lance = somadados()

        if lance == ponto:
            print("Você tirou seu ponto novamente! Você ganhou!")
            break
        elif lance == 7:
            print("Você tirou 7 antes do ponto. Você perdeu!")
            break
        else:
            print("Continue jogando.")

jogo()