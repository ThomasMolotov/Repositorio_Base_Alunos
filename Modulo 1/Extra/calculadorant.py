def soma(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mult(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
escolhe = int(input("Digite 1 para somar os números \nDigite 2 para subtrair os números \nDigite 3 para multiplicar os números \nDigite 4 para dividir os números \nQual você deseja?: "))

if escolhe == 1:
    print(soma(n1,n2))
elif escolhe == 2:
    print(sub(n1,n2))
elif escolhe == 3:
    print(mult(n1,n2))
elif escolhe == 4:
    print(div(n1,n2))
else:
    print("Valor inválido, MORRA LEGAL")