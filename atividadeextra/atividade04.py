# Programa que solicite o valor da compra, forma de pagamento e apresente desconto ou não, dependendo da forma escolhida:

vl_compra = float(input('Informe o valor da compra: '))

print("""
Escolha a forma de pagamento:

1 - A vista (10% de desconto)
2 = Pix (sem alteração no valor)
3 - Débito (acréscimo de 5%)
4 - Crédito (acréscimo de 8%)
5 - Cheque (acréscimo de 12%)
""")

opcao = int(input('Escolha uma forma de pagamento: '))

acrescimo = 0
desconto = 0

match opcao:
    case 1:
        desconto = vl_compra * 0.1
        print('\n---Pagamento a vista---')
        print(f'O valor original da compra é de: {vl_compra}')
        print(f'O valor a ser pago é: {vl_compra - desconto}')
    case 2:
        print('\n---Pagamento via Pix---')
        print(f'O valor original da compra é de: {vl_compra}')
        print(f'O valor a ser pago é: {vl_compra}')
    case 3:
        acrescimo = vl_compra * 0.05
        print('\n---Pagamento no Débito---')
        print(f'O valor original da compra é de: {vl_compra}')
        print(f'O valor a ser pago é: {vl_compra + acrescimo}')
    case 4:
        acrescimo = vl_compra * 0.08
        print('\n--- Pagamento no Crédito---')
        print(f'O valor original da compra é de: {vl_compra}')
        print(f'O valor a ser pago é: {vl_compra + acrescimo}')
    case 5:
        acrescimo = vl_compra * 0.12
        print('\n--- Pagamento em cheque---')
        print(f'O valor original da compra é de: {vl_compra}')
        print(f'O valor a ser pago é: {vl_compra + acrescimo}')
    case _:
        print('Opção inválida. Tente novamente')




        

