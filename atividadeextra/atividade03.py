# Verificação de acesso a benefício em uma cooperativa de crédito:

tp_filiacao = int(input('Informe o tempo de filiação, em anos: '))
vl_mov = float(input('Informe o valor movimentado nos ultimos 6 meses: '))

if tp_filiacao > 3 or vl_mov > 5000.00:
    print('O cooperado tem direito ao benefício especial')
else:
    print('O cooperado não tem direito ao benefício especial')