notas = [0, ]

for i in range(1, 5):
    notan = float(input(f"Digite a {i}° nota do aluno: "))
    notas.append(notan)

media = (notas[1] + notas[2] + notas[3] + notas[4]) / i

print(f"1° nota: {notas[1]}\n2° nota: {notas[2]}\n3° nota: {notas[3]}\n4° nota: {notas[4]}\nA média é: {media}")