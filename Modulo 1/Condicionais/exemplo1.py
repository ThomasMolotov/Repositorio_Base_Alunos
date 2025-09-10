peganome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota 1 do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))
nota3 = float(input("Digite a nota 3 do aluno: "))
nota4 = float(input("Digite a nota 4 do aluno: "))

medio = (nota1 + nota2 + nota3 + nota4) / 4

print(f"Nome do aluno: {peganome} \nMédia final: {medio}")

if medio >= 5:
    print("Aprovado")
else:
    print("Reprovado")

if medio == 10:
    print("REBOLOU TUDÃO POR NOTA")

if medio == 2 and peganome == "BAZINGA":
    print("BAZINGA")