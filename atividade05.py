prova1 = float(input('Digite a nota da prova 1: '))
while prova1<0 or prova1>10:
    print('ERRO! Digite uma nota entre 0 e 10.')
    prova1 = float(input('Digite novamente a nota da prova 1: '))

prova2 = float(input('Digite a nota da prova 2: '))
while prova2<0 or prova2>10:
    print('ERRO! Digite uma nota entre 0 e 10.')
    prova2 = float(input('Digite novamente a nota da prova 2: '))

prova_substitutiva = float(input('Digite a nota da prova substitutiva.\n(caso não tenha feito digite -1): '))
while (prova_substitutiva<0 or prova_substitutiva>10) and prova_substitutiva != -1:
    print('ERRO! Digite uma nota entre 0 e 10.')
    prova_substitutiva = float(input('Digite novamente a nota da prova substitutiva: '))

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

## lição aprendida: não é necessário fazer todos os casos do if, é dizer, se não é ou é cumprida uma
## condição somente pode-se trabalhar com uma das condições tendo em conta que as
## variáveis já foram declaradas e mantém seus valores.
