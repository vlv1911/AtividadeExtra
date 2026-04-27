# Calcula média entre avaliações, substituindo a menor nota pela nota da avaliação substitutiva:

nota01 = float(input('Digite a nota da avaliação 1: '))
nota02 = float(input('Digite a nota da avaliação 2: '))
substitutiva = float(input('Digite a nota da avaliação substitutiva: '))

if substitutiva != -1:
    if nota01 < nota02:
        nota01 = substitutiva
    else:
        nota02 = substitutiva

media = (nota01 + nota02) / 2

if media >= 6:
    print(f'Sua média foi: {media}. Aprovado.')
elif media >=3:
    print(f'Sua média foi: {media}. Em recuperação.')
else:
    print(f'Sua média foi: {media}. Reprovado.')