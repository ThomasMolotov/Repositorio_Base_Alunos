import random
import time

ndado = range(1,7)

def rola():
    dado = random.choice(ndado)
    return f"{dado}"

qdados = int(input("Quantos dados você rola? (até 5 dados): "))

if qdados == 1:
    for _ in range(1):
        print("Você rolou o dado...")
        time.sleep(0.5)
        print(f"caiu {rola()} no dado")
elif qdados == 2:
    for _ in range(1):
        print("Você rolou os dado...")
        time.sleep(0.5)
        print(f"caiu {rola()} no primeiro dado e \n{rola()} no segundo")
elif qdados == 3:
    for _ in range(1):
        print("Você rolou os dado...")
        time.sleep(0.5)
        print(f"caiu {rola()} no primeiro dado; \n{rola()} no segundo e \n{rola()} no terceiro")
elif qdados == 4:
    for _ in range(1):
        print("Você rolou os dado...")
        time.sleep(0.5)
        print(f"caiu {rola()} no primeiro dado; \n{rola()} no segundo; \n{rola()} no terceiro e \n{rola()} no quarto")
elif qdados == 5:
    for _ in range(1):
        print("Você rolou os dado...")
        time.sleep(0.5)
        print(f"caiu {rola()} no primeiro dado; \n{rola()} no segundo; \n{rola()} no terceiro; \n{rola()} no quarto e \n{rola()} no quinto")
else:
    print("Valor inválido, MORRA SEU BURRO")