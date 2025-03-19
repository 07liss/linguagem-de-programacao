quant_turmas=int(input('quantidade de turmas: '))
quant_alunos=int(input('quantidade de alunos: '))
media= (quant_alunos+quant_turmas)/2

if media>40: print('Alguma turma ficará com mais de 40 alunos ou a média é maior que 40')
else: print(media)