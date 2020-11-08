valor_hora = input("Digite o valor que você recebe por hora: ")
qtd_horas = input("Digite o número de horas trabalhadas por mês: ")

salario = valor_hora * qtd_horas

print ("a) Salário bruto: R$", salario) 
print ("b) Quanto pagou de Imposto de Renda: R$", salario * 0.11) 
print ("c) Quanto pagou ao INSS: R$", salario * 0.08)
print ("d) Quanto pagou ao sindicato: R$", salario * 0.05)
print ("e) O salário líquido (igual ao salário bruto menos os descontos): R$", salario * (1- (0.11 + 0.08 + 0.05)))