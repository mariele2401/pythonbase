while True:
    try:
        altura = float(input("Escreva sua altura:"))

        if altura <= 0:
            print("Apenas números maiores que zero")
            continue
        else:
            break
    except ValueError:
        print("Não aceitamos letras, apenas números")