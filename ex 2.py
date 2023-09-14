tipo=(input('\nTipo de combustivel "A" alcool ou "G" Gasolina: '))
litros=float(input('\nLitros de combustivel: '))

if tipo=='A'and litros<20:
    print(f'\nPreço alcool 3% desconto: {(litros*2.90)*0.97}')
elif tipo=='A' :
    print(f'\nPreço alcool 5% desconto: {(litros*2.90)*0.95}')

if tipo=='G'and litros<20:
    print(f'\nPreço Gasolina 4% desconto: {(litros*3.30)*0.96}')
elif tipo=='G' :
    print(f'\nPreço Gasolina 6% desconto: {(litros*3.30)*0.94}')