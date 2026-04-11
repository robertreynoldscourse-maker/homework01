valor_total = float(input('Digite o valor total da compra: '))
print(""" Escolha a forma de pagamento: 
              [1] À vista
              [2] Pix
              [3] Débito
              [4] Crédito
              [5] Cheque
            """)

opcao = int(input('Escolha a forma de pagamento: '))
desconto = 0
acrescimo = 0

match opcao:
    case 1:
        desconto = valor_total*0.10
        valor_final = valor_total - desconto
        print('A forma de pagamento escolhida é: À vista')
        print(f'O valor da compra é: {valor_total}')
        print(f'O valor final incluindo o desconto é: {valor_final}')
    case 2:
        valor_final = valor_total - desconto
        print('A forma de pagamento escolhida é: Pix')
        print(f'O valor da compra é: {valor_total}')
        print(f'O valor final incluindo o desconto é: {valor_final}')
    case 3:
        acrescimo = valor_total*0.05
        valor_final = valor_total + acrescimo
        print('A forma de pagamento escolhida é: Débito')
        print(f'O valor da compra é: {valor_total}')
        print(f'O valor final incluindo o acréscimo é: {valor_final}')
    case 4:
        acrescimo = valor_total*0.08
        valor_final = valor_total + acrescimo
        print('A forma de pagamento escolhido é: Crédito')
        print(f'O valor da compra é: {valor_total}')
        print(f'O valor final incluindo o acréscimo é: {valor_final}')
    case 5:
        acrescimo = valor_total*0.12
        valor_final = valor_total + acrescimo
        print('A forma de pagamento escolhido é: Cheque')
        print(f'O valor da compra é: {valor_total}')
        print(f'O valor final incluindo o acréscimo é: {valor_final}')
    case _:
        print('Opção Inválida.')