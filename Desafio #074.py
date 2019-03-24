from random import randint
cont = 0
print('Os valores sorteados foram:',end=' ')
valores = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
while True:
    if cont < 5:
        print(valores[cont],end=' ')
        cont += 1
    else:
        break
print(f'\nO maior valor na tupla é {max(valores)}.')
print(f'O menor valor na tupla é {min(valores)}.')
