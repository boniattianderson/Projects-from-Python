while True:
    print('Quanto é 10/2')

    alternativas = input('4, 5, 2, 1: ')

    try:
        alternativas_For_int = int(alternativas)
    except:
        print('Digite números válidos')
        continue

    alternativas_for_input = {
        'alternativas': alternativas,
    }

    if alternativas_For_int == 2:
        print('Você acertou')
        print(alternativas_For_int)
        break
    else:
        print('Você errou')