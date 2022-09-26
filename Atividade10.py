'''
Faça um algoritmo que leia a largura e altura de uma parede, calcule e
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

'''

larg = float(input('largura da parede'))
alt = float(input('altura da parede:',))
area = larg * alt
print('sua parede tem a dimensao de {} x {} e sua area de {:.2f} m2. ' .format(larg,alt,area))
tinta = area / 2