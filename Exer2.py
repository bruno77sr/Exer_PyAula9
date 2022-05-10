qtdA = 0
qtdB = 0
soma = 0


for alunos in range(10): #10 como exemplo
    idade = int(input("Digite a sua idade: "))

    #item a
    if idade >= 16:
        qtdA +=1
    else:
        qtdB +=1
        soma += idade

print('Eleitor', qtdA, '\nMédia Não eleitor: ',soma/qtdB)