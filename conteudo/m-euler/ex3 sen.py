import matplotlib.pyplot as plt
import math

def main():
    aprox = []
    real = []
    dx = 0.1
    ant = x0 = 0

    for i in range (0,100):
        prox = ant + dx * math.cos(x0)
        aprox.append(prox)
        sen = math.sin(x0)
        real.append(sen)
        #print('%.3f ---- %.3f'%(prox,sen))
        x0+=dx
        ant = prox
        
    n = len(aprox)
    i=0
    while i<n:
        if aprox[i] - real[i] < 0:
            print('%.3f'%(-(aprox[i] - real[i])))
        else:
            print('%.3f'%(aprox[i] - real[i]))
        i+=1

    plt.plot(aprox, color = 'red', label = 'f(xn+dx) = f(xn-1) + dx*cos(xn-1)')
    plt.plot(real, color = 'blue', label = 'g(x) = sen(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc = 'upper left')
    plt.grid(True)
    plt.show()
    
main()
