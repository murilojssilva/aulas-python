#coding: utf-8
'''Exercício 23'''
salario = input("Digite o valor do salario do funcionario: ")

print ("a) O salario antes do reajuste: R$", salario)
if salario < 280:
    print ("b) O percentual de aumento aplicado foi de 20%")
    print ("c) O valor de aumento foi de R$", ((salario * 1.2) - salario))
    salario *= 1.2
elif salario == 280 or salario < 700:
    print ("b) O percentual de aumento aplicado foi de 15%")
    print ("c) O valor de aumento foi de R$", ((salario * 1.15) - salario))
    salario *= 1.15
elif salario == 700 or salario < 1500:
    print ("b) O percentual de aumento aplicado foi de 10%")
    print ("c) O valor de aumento foi de R$", ((salario * 1.1) - salario))
    salario *= 1.1
elif salario >= 1500:
    print ("b) O percentual de aumento aplicado foi de 5%")
    print ("c) O valor de aumento foi de R$", ((salario * 1.05) - salario))
    salario *= 1.05

print ("d) O novo salario, apos o aumento: R$", salario)
