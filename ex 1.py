"""  - Tendo como dados de entrada a altura e o sexo de uma pessoa (M masculino e F feminino), construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: 
para homens: (72.7*h)-58
para mulheres: (62.1*h)-44.7 """

sexo= input('\nDigite "m" para masculino ou "f" para feminino: ')

altura=float(input('\nEntre com a altura: '))

if sexo=='m':
    print(f'Peso ideal: {(72.7*altura)-58:.2f}')
    print('\n')
else:
    sexo=='m'
    print(f'Peso ideal: {(62.1*altura)-44.7:.2f}')
    print('\n')



