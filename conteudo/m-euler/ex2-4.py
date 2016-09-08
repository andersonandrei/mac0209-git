# Aqui teremos F = -mg por Euler e Euler - Cromer

import matplotlib.pyplot as plt

def eulerC(aproxEC):
    g = 9.85
    dt = 0.01
    atualV = atualY = 0

    for i in range (1,10) :
        proxV = atualV - g*dt
        proxY = atualY + proxV*dt
        aproxEC.append(proxY)
        print('%.3f'%(proxY))
        atualV = proxV
        atualY = proxY
    return aproxEC

def eulerR(aproxR):
    g = 9.85
    m = 2
    dt= 0.1
    a = g/m
    atualV = atualY = 0

    for i in range (0,10):
        proxV = atualV + 0.5*a*dt
        dt+=0.5*dt
        proxY = atualY + proxV*0.5*dt
        aproxR.append(proxY)
        atualV = proxV
        atualY = proxY
    return aproxR

def euler(aproxE):
    g = 9.85
    dt = 0.01
    atualV = atualY = 0

    for i in range (1,10) :
        proxV = atualV - g*dt
        proxY = atualY + atualV*dt
        aproxE.append(proxY)
        print('%.3f'%(proxY))
        atualV = proxV
        atualY = proxY
    return aproxE

def iterativo(aproxI):
    dt = 0.01
    g = 9.85
    atualV = atualY = 0
    for i in range (1,10):
        proxV = atualV - g * dt
        proxY = atualY + atualV * dt - (g * (dt*dt))/2
        aproxI.append(proxY)
        atualV = proxV
        atualY = proxY
    return aproxI

def main():
    aproxE = []
    aproxEC = []
    aproxI = []
    aproxR = []
    real = []
    aproxE = euler(aproxE)
    aproxEC = eulerC(aproxEC)
    aproxR = eulerR(aproxR)
    real = iterativo(real)
    print(aproxE)
    print(aproxEC)
    print(aproxR)
    print(real)
    plt.plot(real, color = 'green', label = 'Iterativo')
    plt.plot(aproxE, color = 'red', label = 'Euler')
    plt.plot(aproxR, color = 'pink', label = 'Euler-Rich')
    plt.plot(aproxEC, color = 'blue', label = 'Euler - Cromer')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Comparação entre o método de Euler e Euler-Cromer')
    plt.legend(loc = 'lower left')
    plt.grid(True)
    plt.show()

main()
