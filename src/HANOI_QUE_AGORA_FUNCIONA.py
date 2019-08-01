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
        orig = 'a'
    elif torre_posicao.lower() == 'b':
        orig = 'b'
    elif torre_posicao.lower() == 'c':
        orig = 'c'
    else: print('Valor inválido, digite A, B ou C')

    peca_posicao = str(input('Pra onde você quer passar essa peça? A, B, C \n ')).lower()

    if orig == 'a':
        retirado = torre_A.pop()
        if peca_posicao == 'a':
            torre_A.append(retirado)
        elif peca_posicao == 'b':
            if len(torre_B) == 0 or torre_B[-1] > retirado:
                torre_B.append(retirado)
            else:
                torre_A.append(retirado)
        elif peca_posicao == 'c':
            if len(torre_C) == 0 or torre_C[-1] > retirado:
                torre_C.append(retirado)
            else:
                torre_A.append(retirado)
                
    if orig == 'b':
        retirado = torre_B.pop()
        if peca_posicao == 'b':
            torre_B.append(retirado)
        elif peca_posicao == 'a':
            if len(torre_A) == 0 or torre_A[-1] > retirado:
                torre_A.append(retirado)
            else:
                torre_B.append(retirado)
        elif peca_posicao == 'c':
            if len(torre_C) == 0 or torre_C[-1] > retirado:
                torre_C.append(retirado)
            else:
                torre_B.append(retirado)

    if orig == 'c':
        retirado = torre_C.pop()
        if peca_posicao == 'c':
            torre_C.append(retirado)
        elif peca_posicao == 'a':
            if len(torre_A) == 0 or torre_A[-1] > retirado:
                torre_A.append(retirado)
            else:
                torre_C.append(retirado)
        elif peca_posicao == 'b':
            if len(torre_B) == 0 or torre_B[-1] > retirado:
                torre_B.append(retirado)
            else:
                torre_C.append(retirado)
    
                    
print(tabu())
print("\n"*5,"VOCE GANHOU UHUUUUUL!!!!!!!")
