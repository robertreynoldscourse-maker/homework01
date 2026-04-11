quantidade_estoque = int(input('Digite a quantidade em estoque: '))
quantidade_solicitada = int(input('Digite a quantidade solicitada: '))
peso_pedido = float(input('Digite o peso do pedido: '))

if quantidade_solicitada <= quantidade_estoque and peso_pedido <= 50:
    print('O pedido pode ser liberado.')
else:
    print(f' O pedido não pode ser enviado.\n Lembre-se que a quantidade solicitada deve ser menor a {quantidade_estoque} e \n o peso não pode se exceder de 50 kg.')