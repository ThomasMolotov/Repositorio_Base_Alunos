with open("dados.txt", "r") as arquivo:
    for i, linha in enumerate(arquivo, 1):
        print(f"Linha {i}: {linha.strip()}")