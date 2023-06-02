while True:
    print('Quanto é 5*5')

    alternativas = input('25, 55, 10, 51: ')

    try:
        alternativas_For_int = int(alternativas)
    except:
        print('Digite números válidos')
        continue

    alternativas_for_input = {
        'alternativas': alternativas,
    }

    if alternativas_For_int == 25:
        print('Você acertou')
        print(alternativas_For_int)
        break
    else:
        print('Você errou')