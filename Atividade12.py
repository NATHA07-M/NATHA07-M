# Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.

p_produto=float(input("Digite o valor do produto:"))
p_desconto=(p_produto*5)/100
vlr_prod_desc=p_produto-p_desconto

print("o valor do produto com desconto e:",vlr_prod_desc)
