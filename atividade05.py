
def pedir_nota(mensagem):
    nota = float(input(mensagem))
    while (nota < 0 or nota > 10) and nota != -1:
        nota = float(input('ERRO! Digite novamente una nota entre 0 e 10: '))
    return nota

prova1 = pedir_nota('Digite a nota da prova 1: ')
prova2 = pedir_nota('Digite a nota da prova 2: ')
prova_substitutiva = pedir_nota('Digite a nota da prova substitutiva.\n(caso não tenha feito digite -1): ')

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
