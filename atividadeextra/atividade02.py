# Controle de estoque: O pedido só pode ser liberado se duas condições forem atendidas.

qtd_estoque = int(input('Informe a quantidade disponível no estoque: '))
qtd_cliente = int(input('Informe a quantidade solicitada pelo cliente: '))
peso_ttl_pedido = int(input('Informe o peso total do pedido: '))

if qtd_estoque >= qtd_cliente and peso_ttl_pedido <= 50:
    print('O pedido pode ser liberado')
else:
    print('O pedido não pode ser enviado')