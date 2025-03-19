lista=[]

while len(lista)<3:
    num=int(input('Número: '))
    lista.append(num)
print(f'maior: {max(lista)}\nmenor: {min(lista)}')