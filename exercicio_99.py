#coding: utf-8
def retangulo(_linha, _coluna):
    '''
        Função responsável por imprimir o retângulo
    '''
    for i in range(linha):
		for j in range(coluna):
			if i == 0 and j == 0:
				print("+"),
			elif i == 0 and j == coluna-1:
				print("+"),
			elif i == linha-1 and j == 0:
				print("+"),
			elif i == linha-1 and j == coluna-1:
				print("+"),
			elif i == 0 and j != 0:
				print("-"),
			elif i == linha-1 and j != 0:
				print("-"),	
			elif j == 0 and i != 0:
				print("|"),
			elif j == coluna-1 and i != 0:
				print("|"),
		 	else:
				print(" "),
		print("")

linha = input("Digite a quantidade de linhas: ")
coluna = input("Digite a quantidade de colunas: ")

if linha < 20 and linha >= 1 and coluna < 20 and coluna >= 1:
	retangulo(linha, coluna)
else:
	retangulo(20, 20) 
