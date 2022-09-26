'''
 
Desenvolva um programa que leia uma distância em metros e mostre os
valores relativos em outras medidas.
Ex:
Digite uma distância em metros: 185.72 A
distância de 85.7m corresponde a: 

'''

print("Digite uma distancia em metros")
metros = float(input ("Qual e a distancia em metros ?:"))

mult = metros * 100
print("A distancia e",mult,'cm')
