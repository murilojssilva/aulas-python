#coding: utf-8
'''
    Exercício 111
'''
def mes_extenso(_data_padrao):
    '''
        Função que recebe uma data no formato datetime e converte para o texto por extenso.
    '''
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    aux = data_padrao.split("/")
    dia = int(aux[0])
    mes = int(aux[1])
    ano = int(aux[2])
    if ((1 < dia < 31) or (1 < mes < 12) or (0 > ano > 9999)):
        return "Data Inválida"
    return dia, " de ", meses[mes-1], " de ", ano

data_padrao = raw_input('Digite uma data no formato DD/MM/AAAA: ')
print(mes_extenso(data_padrao))
