import matplotlib.pyplot as plt
import math

def analitica(A,B,t):
    k = 1
    m = 1
    a = -(math.sqrt(k/m))

    return A * math.cos(a*t) + B * math.sin(a*t)
        
def main():
    aproxE = []
    real = []

    t = 0
    atualV = atualX = 0
    k = m = 1
    x=2
    a = (k/m)
    dt = 0.1
    atualV = atualX = 0

    for i in range(0,100):
        proxV = atualV + a*x*dt
        proxX = atualX + atualV*dt
        ana = analitica(10,10,dt*i)
        real.append(ana)
        aproxE.append(proxX)
        atualV = proxV
        atualX = proxX

    plt.plot(real, color = 'red', label = 'Analitica')
    plt.plot(aproxE, color = 'blue', label = 'Método de Euler')
    plt.grid(True)
    plt.xlabel('x = Tempo (s)')
    plt.ylabel('y = Posição (m)')
    plt.legend(loc = 'upper left')
    plt.show()

main()

    
