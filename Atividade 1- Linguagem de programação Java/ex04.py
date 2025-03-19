km=int(input('Quantos KMs você rodou?'))
dias=int(input('em quantos dias?'))
diarias=90*dias
if km>100:
    excedente=km-100
    total= excedente*12 + diarias
    print(f'o valor total é:{total}')

else: print(f'Total é {diarias}')