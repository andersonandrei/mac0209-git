
def main():
    aproxV = []
    realV = []

    aproxY = []
    realY = []

    dt = 0.1
    g = 9.80665
    antY = antV = cont = 0
    for i in range (0,10):
        proxV = antV - g*dt
        proxY = antY + dt * antV
        print('v = %.3f ---- y = %.3f ---- '%(proxV,proxY))
        aproxY.append(proxY)
        aproxV.append(proxV)

        cont +=0.1
        
        antV = proxV
        antY = proxY
        
    print(aproxV)
    print(aproxY)
main()
