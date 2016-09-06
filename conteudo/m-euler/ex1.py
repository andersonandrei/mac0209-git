import matplotlib.pyplot as plt

def f(x):
    return 2*x

def g(x):
    return x*x

def main():
    print('Método de euler pra aproximar os roles\n')
    cont = 0
    ant = x0 = 0
    aprox = []
    real = []
    for i in range (0,100):
        atual = ant + 0.1 * f(x0)
        if (cont == 10):
            print('%3.3f ------- %3.3f ------ %3.3f'%(x0,g(x0),atual))
            cont = 0
        else:
            cont+=1
        aprox.append(atual)
        real.append(g(x0))
        ant = atual
        x0+=0.1

    plt.plot(aprox,color = 'blue', label = 'f(xn+dx) = f(xn) + dx*2x')
    plt.plot(real,color = 'red', label = 'g(x) = x²')
    plt.title('Aproximação de x² pelo método de Euler')
    plt.xlabel('x')
    plt.ylabel('y = f(x)')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()
    return 0
