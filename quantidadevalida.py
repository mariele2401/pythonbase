while True:
    try:
        quantidade = float(input("Escreva quantidade de produto: "))
        if quantidade <= 0:
            print("Apenas numeros interos e positivos.")
        else:
            break
    except ValueError:
        print("Idade inválida!Digite apenas números.")

print("Quantidade final:", quantidade)
