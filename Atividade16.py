'''
escreva um programa para calcular a reducao do tempo de vida de um fumente. pergunte a quantidade de cigarros fumados
por dias e quantos anos e por quantos anos ele ja fumou. 
considere que um fumante perde 10 min de vida a cada cigarro
calcule quantos dias de vida ele perdera 
'''
cigarrosdia = float(input('insira a quantidade de cigarros fumados por dia: '))
anoscigarros = float(input('por quantos anos ele fumou?'))
mnds = ((cigarrosdia/144)*(anoscigarros*365))
print('seu tempo foi reduzido por :', mnds)