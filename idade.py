while True:
    try:
        idade = int(input("Qual sua idade? "))
        if idade <= 0:
            print("A idade não aceita zero e números negativos.")
        else:
            break
    except ValueError:
        print("Idade inválida!Digite apenas números.")

print("Idade cadastrada:", idade)