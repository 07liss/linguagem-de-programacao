valor=int(input('Qual o valor das compras?'))

if valor>500:
    ultrapassagem=valor - 500
    correcao= ultrapassagem/2
    valor_corrigido= valor + correcao
    print(f'Valor com a correção: {valor_corrigido}')

else: print('Não há ultrapassagem de valor, logo não há impostos')