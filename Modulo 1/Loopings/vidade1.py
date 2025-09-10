while True:
        nota = int(input("Digite uma nota entre 0 e 10: "))
        if nota in range(1,11):
            print(f"Nota válida")
            break
        else:
            print("Valor inválido! A nota deve estar entre 0 e 10.")