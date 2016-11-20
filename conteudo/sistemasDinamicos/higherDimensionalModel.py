import matplotlib.pyplot as plt

def hdm (antX):
    return (0.3 * antX)

def main():
    vetorA = []
    vetorB = []
    antX = 0.63135448
    antY = 0.18940634
    a = 1.4
    b = 0.3
    for i in range (1,10):
        proxX = antY + 1 - (a * antX * antX)
        proxY = hdm (antX)
        vetorA.append(proxY)
        antX = proxX
        antY = proxY

    antX = 0
    antY = 0
    for i in range (1,10):
        proxX = antY + 1 - (a * antX * antX)
        proxY = hdm (antX)
        vetorB.append(proxY)
        antX = proxX
        antY = proxY
        
    plt.plot(vetorA, color = 'red', label = 'x0 = 1.4 e y0 = 0.3')
    plt.plot(vetorB, color = 'blue', label = 'x0 = 1.4 e y0 = 0.3')
    plt.xlabel('x = tempo (s)')
    plt.ylabel('y = posição (m)')
    plt.grid(True)
    plt.show()
main ()
