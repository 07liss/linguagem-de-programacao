salario=int(input('salário inicial: '))
anos_empresa=int(input('anos na empresa: '))

def salario_novo(anos):

    if anos==1:
        return salario
    else: return salario_novo(anos-1)*2

print(salario_novo(anos_empresa))