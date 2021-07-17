#Total Value
ValorTotal = float(input("Valor Total: "))
#Initial bet value
ValorInicial = float(input("Valor Inicial: "))
# Multiplier
MultiplicadorOnLoss = float(input("Multiplicador: "))
ValorResultante = ValorInicial
Soma = ValorTotal

for i in range(20):
    Soma = ValorTotal - ValorResultante
    print("{:.2f}".format(Soma), i+1)
    if Soma <=0:
        print("Você chegou na camada: ", i)
        break
    ValorResultante = ValorInicial*MultiplicadorOnLoss
    ValorInicial = ValorResultante
    Soma = ValorTotal-ValorResultante
