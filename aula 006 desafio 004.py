# - Desafio 004
# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.

x = input('Digite qualquer coisa: ')
print(x, 'É do tipo primitivo', type(x))
print(x, 'Possui apenas números?', x.isnumeric(), '!')
print(x, 'Possui apenas letras?',  x.isalpha(), '!')
print(x, 'Possui letra ou número?', x.isalnum())
print(x, 'Possui apenas letras maiúsculas?', x.isupper())
print(x, 'Possui apenas letras minúsculas?', x.islower())
