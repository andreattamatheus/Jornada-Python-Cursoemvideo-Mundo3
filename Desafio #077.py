palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in range (0,len(palavras)):
    print(f'\nA palavra {palavras[c]} tem as VOGAIS -> ',end='')
    if 'A' in palavras[c]:
        print('A',end=' ')
    if 'E' in palavras[c]:
        print('E',end=' ')
    if 'I' in palavras[c]:
        print('I',end=' ')
    if 'O' in palavras[c]:
        print('O',end=' ')
    if 'U' in palavras[c]:
        print('U',end=' ')