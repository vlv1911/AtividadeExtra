# Recebe 4 notas de um estudante e no final mostra se está aprovado, em recuperação ou reprovado.

nota01 = float(input('Digite a note do primeiro bimestre: '))
nota02 = float(input('Digite a nota do segundo bimestre: '))
nota03 = float(input('Digite a nota do terceiro bimestre: '))
nota04 = float(input('Digite a nota do quarto bimestre: '))

media = (nota01 + nota02 + nota03 + nota04) / 4

print(f'A nota média foi: {(media)}')

if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')


