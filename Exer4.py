from asyncio.windows_events import NULL


mediaSal = 0
somaSal = 0
soma = 0
mediaId = 0
qtdSal = 0

op ="s"
while op == "s" or op == "S":
    id = int(input("Digite sua idade: "))
    if id > 0:
        sal = float(input("Digite seu salário: "))
        mediaId += 1
        soma += id
        if id > 40:
           mediaSal += 1
           somaSal += sal
        if sal < 600:
           qtdSal += 1
        op = input("Quer continuar ? [S] [N]")
    else:
        break

mediaGrupo = soma/mediaId

if mediaSal != 0 and somaSal != 0:
    mediaSal40 = somaSal/ mediaSal
    
    print('A média de salário com idade acima de 40 anos é: %.2f' %(mediaSal40))


print('A média de idade do grupo é: ',int(mediaGrupo),'\nA quantidade de pessoas com o salário abaixo de R$ 600,00 é:', qtdSal)
  

    

