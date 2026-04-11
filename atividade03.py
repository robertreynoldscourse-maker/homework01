tempo = float(input('Digite o tempo de filiação em anos: '))
valor = float(input('Digite o valor movimentado nos últimos 6 meses: '))

if tempo >= 3 or valor >= 5000:
    print('O cliente tem direito ao benefício.')
else:
    print('O cliente ainda não atende aos criterios para o benefício.')