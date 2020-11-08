#coding: utf-8
'''Exercício 29'''
lado1 = input("Digite a medida do primeiro do triangulo: ")
lado2 = input("Digite a medida do segundo do triangulo: ")
lado3 = input("Digite a medida do terceiro lado do triangulo: ")

if lado1 + lado2 > lado3:
    if (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print ("Esse triangulo e isosceles.")
    elif (lado1 == lado2 and lado1 == lado3):
        print ("Esse triangulo e equilatero")
    else:
        print ("Esse triangulo e escaleno")
else:
    print ("Os valores fornecidos nao correspondem a um triangulo.")
