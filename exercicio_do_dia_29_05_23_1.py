while True:
    print('Quanto é 2+2')
    opcoesDe_Respostas = input('1, 3, 4, 5: ')

    resposta_validas = None
    opcoesDe_Respostas_for_int = 0
    
    try:
        opcoesDe_Respostas_for_int = int (opcoesDe_Respostas)
        resposta_validas = True
    except:
        resposta_validas = None
        
    if resposta_validas is None:
        print('Digite algum número válido.')
        continue
    opcoesDe_Respostas = '1, 3, 4, 5'

    if opcoesDe_Respostas_for_int == 4:
            print('Você acertou')
            print(opcoesDe_Respostas_for_int)
            break
    else:
        print('Você errou')