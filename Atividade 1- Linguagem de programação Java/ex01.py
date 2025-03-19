lista=[]

while len(lista)<3:
    num=int(input('Digite um número: '))
    lista.append(num)

ponderada=(lista[0]*2 + lista[1]*2 + lista[2]*3)/7
ponderada2=(lista[0] + lista[1]*2 + lista[2]*2)/5
print(f'A média aritmética é {sum(lista)/3}\nA média ponderada com pesos 2, 2 e 3 é {round(ponderada, 2)} e a com pesos 1, 2 e 2 é {round(ponderada2, 2)} ')