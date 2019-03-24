produtos = ('Caderno', 25.60,
            'Lápis', 0.50,
            'Caneta', 1.50,
            'Borracha', 2.40,
            'Tesoura', 3.50,
            'Cola', 2.50,
            'Corretivo', 4.20,
            'Apontador', 1.50,
            'Bolsa', 135.90)
print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*40)
for lista in range (0,len(produtos)):
    if lista % 2 == 0:
        print(f'{produtos[lista]:.<20}',end='')
    if lista % 2 == 1:
        print(f'R${produtos[lista]:>6}')