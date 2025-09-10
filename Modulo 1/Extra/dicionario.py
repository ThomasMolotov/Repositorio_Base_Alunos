negritude = [{"nome": "Caique"}, {"nome": "Caio"}, {"nome": "Pedro"}, {"nome": "Rafa"}, {"nome": "Wender"}, {"nome": "Danielson"}]

while True:
    try:
        qual = int(input("[1] Caique \n[2] Caio \n[3] Pedro \n[4] Rafa \n[5] Wender \n[6] Danielson \n[7] Sair \nQual você quer ver o nome?: "))
        if qual == 1:
            print(negritude[0]["nome"])
        elif qual == 2:
            print(negritude[1]["nome"])
        elif qual == 3:
            print(negritude[2]["nome"])
        elif qual == 4:
            print(negritude[3]["nome"])
        elif qual == 5:
            print(negritude[4]["nome"])
        elif qual == 6:
            print(negritude[5]["nome"])
        elif qual == 7:
            print("NUM QUER MAIS? ENTÃO SE FODA")
            break
        else:
            print("ESSA PORRA NÃO ESTÁ NA LISTA")

    except:
        print("ESSA PORRA NÃO É NEM UM NÚMERO DIABO")