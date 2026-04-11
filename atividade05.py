prova1 = float(input('Digite a nota da prova 1: '))
prova2 = float(input('Digite a nota da prova 2: '))
prova_substitutiva = float(input('Digite a nota da prova substitutiva.\n(caso não tenha feito digite -1): '))

if prova_substitutiva != -1:
    if prova1 <= prova2 and prova_substitutiva >= prova1:
        prova1 = prova_substitutiva
    elif prova2 <= prova1 and prova_substitutiva >= prova2:
        prova2 =  prova_substitutiva

media = (prova1 + prova2)/2
print(f'A media do aluno é: {media}')
match media:
    case media if media >= 6:
        print('Aprovado')
    case media if 3 <= media < 6:
        print('Recuperação')
    case media if media < 3:
        print('Reprovado') 
