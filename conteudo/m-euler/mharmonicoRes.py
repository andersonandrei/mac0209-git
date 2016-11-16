import matplotlib.pyplot as plt
import math

def analitica(A,B,t):
    k = 1
    m = 1
    a = -(math.sqrt(k/m))

    return A * math.cos(a*t) + B * math.sin(a*t)

def euler():
    aproxER = []
    real = []

    t = 0
    atualV = 0
    atualX = 1
    k = m = 1
    a = -(k/m)
    dt = 0.1
    res = 0.1

    for i in range(0,100):
        proxV = atualV + a*atualX*dt - res*atualX
        proxX = atualX + atualV*dt
        ana = analitica(1,1,dt*i)
        real.append(ana)
        aproxER.append(proxX)
        atualV = proxV
        atualX = proxX

    return aproxER

        
def main():
    aproxE = []
    real = []

    t = 0
    atualV = 0
    atualX = 1
    k = m = 1
    a = -(k/m)
    dt = 0.1
    res = 0.1

    for i in range(0,100):
        print(atualX)
        proxV = atualV + a*atualX*dt - res*atualX
        proxX = atualX + atualV*dt
        ana = analitica(1,1,dt*i)
        real.append(ana)
        print(proxX)
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

    
