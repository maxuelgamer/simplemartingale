#Total Value
ValorTotal = float(input("Valor Total: "))
#Initial bet value
ValorInicial = float(input("Valor Inicial: "))
# Multiplier
MultiplicadorOnLoss = float(input("Multiplicador: "))
ValorResultante = ValorInicial
Soma = ValorTotal

for i in range(20):
    ValorResultante = ValorInicial*MultiplicadorOnLoss
    ValorInicial = ValorResultante
    Soma = ValorTotal-ValorResultante
    print(Soma, i+1)
    if Soma < 0:
        print("Você chegou na camada: ", i)
        print("Para chegar na camada ", i+1, " você precisaria de mais", -Soma," que daria um total de", ValorResultante)
        break
