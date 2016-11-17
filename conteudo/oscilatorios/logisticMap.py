import matplotlib.pyplot as plt

def main ():
    vetor = []
    atual = 0.99
    prox = 0
    r = 0.76

    for i in range (1,100):
        prox = 4 * r * atual * (1 - atual)
        vetor.append(prox)
        atual = prox
    plt.plot (vetor, color = 'red')
    plt.show()

#Para executar os exemplo do livro:
#        a) r = 0.2 e atual = 0.5
#        b) r = 0.7 e atual = 0.1

main()
    
