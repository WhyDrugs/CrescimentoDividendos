def main():
    aporteInicial = float(input("Digite o Aporte Inicial: "))
    aporteMensal = float(input("Digite o Aporte Mensal: "))
    precoCota = float(input("Digite o Preço médio das Cotas: "))
    rendimentoCota = float(input("Digite o Rendimento médio por Cota: "))
    rendaMensalDesejada = float(input("Digite a Renda Mensal desejada: "))

    qtdCotas = 0
    qtdCotas = (aporteInicial//precoCota)
    caixa = (aporteInicial - (qtdCotas * precoCota))
    rendimentoMensal = qtdCotas * rendimentoCota


    print('Com o aporte inicial você comprou: {} cotas'.format(qtdCotas))
    print('Com o aporte inicial sobrou: {:.2f} em caixa'.format(caixa))
    print('Com o aporte Inicial tem rendimento mensal de: {:.2f}'.format(rendimentoMensal))

    indice = 0
    while (rendimentoMensal < rendaMensalDesejada):
        indice = indice + 1
        caixa = caixa + aporteMensal + rendimentoMensal 

        while(caixa >= precoCota):
            caixa = caixa - precoCota
            qtdCotas = qtdCotas + 1
    
        
        rendimentoMensal = qtdCotas * rendimentoCota
        print('Mês {}: cotas={},  caixa = {:.2f} e rendimento mensal = {:.2f}'.format(indice,qtdCotas,caixa,rendimentoMensal))



main()