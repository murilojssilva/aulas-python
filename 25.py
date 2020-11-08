area = input("Digite a area da loja de tintas (em metros quadrados): ")

qtdlatas = area//108

qtdgaloes = area//21.6

if area%108 > 0:
    print ("a) Comprar apenas latas de 18 litros: ",qtdlatas + 1," latas, com o total de R$", (qtdlatas + 1)*80)
else:
    print ("a) Valor da área não corresponde a um valor valido.")

if area%21.6 > 0:
    print ("b) Comprar apenas latas de 3,6 litros:",qtdgaloes + 1," latas, com o total de R$", (qtdgaloes + 1)*25)
else:
    print ("b) Valor da area não corresponde a um valor valido.")

if area>0:
    margem = area * 1.1
    print "Area com a folga: %.2f metros quadrados." % margem

    if margem%108 > 0:
        qtdlatas2 = margem//108
        sobra = (margem/108 - margem//108)*108
        qtdgaloes2 = sobra//21.6
        if sobra%21.6 > 0:    
            qtdgaloes2 = qtdgaloes2 + 1
        
    precolatas2 = qtdlatas2*80    
    precogaloes2 = qtdgaloes2*25
    precototal = precolatas2 + precogaloes2    
    print "c) Misturar latas e galoes, de forma que o preco seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto e, considere latas cheias: "
    print "%i latas e %i galoes, com o valor de: R$%.2f" % (qtdlatas2, qtdgaloes2, precototal)
else:
    print ("c) Valor da area não corresponde a um valor valido.")