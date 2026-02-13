while True:
    try:
        valor = float(input("Solicite o valor do saque: "))

        if valor <= 0:
            print("O caixa só aceita números positivos!")
        elif valor > 1000:
            print("O caixa não permite saque maior que R$ 1000.")
        else:
            break # valor válido -> sai do loop

    except ValueError:
        print("Digite apenas números!")

print("Saque realizado:", valor)