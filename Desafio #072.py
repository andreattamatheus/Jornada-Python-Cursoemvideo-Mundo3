num = ('Zero','One','Two','Three','Four','Five','Six','Seven','Eigth','Nine','Ten','Eleven','Twelve','Thirteen',
       'Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty')
question = int(input('Type a number between 0 and 20: '))
while question < 0 or question > 20:
    question = int(input('Try Again.Type a number between 0 and 20: '))
print(f'You typed the number {num[question]}')
