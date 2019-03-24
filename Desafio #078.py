valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor é {max(valores)} na posição {valores.index(max(valores))}.\nO menor valor é {min(valores)} na posição {valores.index(min(valores))}.')