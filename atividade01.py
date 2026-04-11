nota1 = float(input('Digite a nota 1 do aluno: '))
nota2 = float(input('Digite a nota 2 do aluno: '))
nota3 = float(input('Digite a nota 3 do aluno: '))
nota4 = float(input('Digite a nota 4 do aluno: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média do aluno é: {media:.2f}')
match media:
    case media if media >= 7:
        print('Aprovado')
    case media if 5 <= media < 7:
        print('Recuperação')
    case media if media < 5:
        print('Reprovado')



