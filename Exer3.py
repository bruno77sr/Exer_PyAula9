op = "s"

while op == "s":
    sexo = input("Digite seu sexo: (H - M): \nDigite:")
    alt = float(input("Digite sua altura: "))

    if sexo == "h":
        calc = alt * 72.7 - 58
        print("Seu peso ideal é: ", calc)
    else:
        calc = alt * 62.1 - 44.7
        print("Seu peso ideal é: ", calc)
    
    op = input("Quer continuar ? s ou n ")