ValorTotal = float(input("Valor Total:"))
ValorInicial = float(input("Valor inicial:"))
Porcentagem = float(input("Porcentagem na derrota:"))
ValorTotalParaSoma = ValorTotal

for i in range(20):
    ValorResultante = ValorInicial*Porcentagem
    print(ValorResultante)
    ValorTotalParaSoma = ValorTotalParaSoma-ValorResultante
    ValorInicial = ValorResultante
    if ValorTotalParaSoma < 0:
        print("Você chegou na camada "+str(i+1))
        break
