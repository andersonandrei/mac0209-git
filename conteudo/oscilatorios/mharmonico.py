import matplotlib.pyplot as plt
import math

def main():
    aproxX = []
    aproxV = []
    anaX = []
    atualX = 0
    atualV = 0
    dt = 0.1
    x = 0
    k = 1
    m = 1
    A = 1
    p = 1
    a = k/m

    for i in range (1,100):
        proxV = atualV + (-k/m)* x * dt
        proxX = atualX + atualV * dt
        dt += 0.1
        aproxX.append (proxX)
        aproxV.append (proxV)
        atualV = proxV
        atualX = proxX
        anaX.append (A * math.cos (math.sqrt(k/m) * i + p) )

    plt.plot (anaX, color = 'red', label = 'Analitica')
    plt.plot (aproxX, color = 'blue', label = 'Euler')
    plt.grid (True)
    plt.xlabel ('x = tempo (s)')
    plt.ylabel ('y = posição (m)')
    plt.show()

main()
    
