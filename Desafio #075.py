first = int(input('Digite um valor: '))
second = int(input('Digite outro valor: '))
third = int(input('Digite outro valor: '))
fourth = int(input('Digite outro valor: '))
conjunto = (first,second,third,fourth)
print(f'O valor 9 apareceu {conjunto.count(9)} vezes.')
if conjunto.count(3) != 0:
    print(f'A primeira aparição do valor 3 é na {conjunto.index(3)+ 1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os números pares foram: ',end='')
for c in conjunto:
    if c % 2 == 0:
        print(c,end=' ')

