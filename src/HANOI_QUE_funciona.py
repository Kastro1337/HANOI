# -*- coding: utf-8 -*-
torre_A = [3,2,1]
torre_B = []
torre_C = []
def tabu():
    print('',torre_A,'\n',torre_B,'\n',torre_C)

while torre_C != [3,2,1]:
    tabu()
    torre_posicao = str(input('Selecione a torre para retirar uma peça: A , B , C \n '))
    if torre_posicao.lower() == 'a':
        mazzutti = torre_A.pop()
    elif torre_posicao.lower() == 'b':
        mazzutti = torre_B.pop()
    elif torre_posicao.lower() == 'c':
        mazzutti = torre_C.pop()
    else: print('Valor inválido, digite A, B ou C')

    peca_posicao = str(input('Pra onde você quer passar essa peça? A, B, C \n '))
    if peca_posicao.lower() == 'a':
        if torre_A != []:
            if mazzutti < torre_A[-1]:
                torre_A.append(mazzutti)
            else:
                print('Valor inválido. A peça à ser colocada é maior que aquela que se encontra no local.')
        else:
            torre_A.append(mazzutti)


            
    elif peca_posicao.lower() == 'b':
        if torre_B != []:
            if mazzutti < torre_B[-1]:
                torre_B.append(mazzutti)
            else:
                print('Valor inválido. A peça à ser colocada é maior que aquela que se encontra no local.')
        else:
            torre_B.append(mazzutti)


            
    elif peca_posicao.lower() == 'c':
        if torre_C != []:
            if mazzutti < torre_C[-1]:
                torre_C.append(mazzutti)
            else:
                print('Valor inválido. A peça à ser colocada é maior que aquela que se encontra no local.')
        else:
            torre_C.append(mazzutti)

print(tabu())
print("\n"*5,"VOCE GANHOU UHUUUUUL!!!!!!!")
