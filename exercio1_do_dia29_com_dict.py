while True:
    print('Quanto é 2+2')

    alternativas = input('1, 3, 4, 5: ')

    try:
        alternativas_For_int = int(alternativas)
    except:
        print('Digite números válidos')
        continue

    alternativas_for_input = {
        'alternativas': alternativas,
    }

    if alternativas_For_int == 4:
        print('Você acertou')
        print(alternativas_For_int)
        break
    else:
        print('Você errou')