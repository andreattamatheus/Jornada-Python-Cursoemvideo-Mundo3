valores = list()
while True:
    num = valores.append(int(input('Digite um valor: ')))
    if num in valores:
        print('Valor duplicado, não será adicionado.')
        valores.remove(num)
        num = valores.append(int(input('Digite um valor: ')))
    opcao = input('Deseja continuar [S/N]').upper()
    if opcao == 'N':
        break
print(valores.sort())