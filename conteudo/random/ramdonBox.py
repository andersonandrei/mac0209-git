import random

def main ():
    n = 100
    box = []
    numEsq = 0
    numDir = 0
    rand = 0
    
    for i in range (0, 100):
        box.append(1)
        numEsq = numEsq + 1
    numDir = 100 - numEsq
    print ('Estado 0 : \n NumEsq = %d e NumDir = %d', numEsq, 20-numEsq)
    print 
    for i in range (0,100):
        rand = random.random()
        if (rand <= (numEsq / n)) :
           pos = random.randint (0,99)
           box[pos] = -1
           numDir += 1
           numEsq -= 1
        print('Estado %d: \n NumEsq = %d e NumDir = %d', i, numEsq, numDir)
    print ('Estado Final : \n NumEsq = %d e NumDir = %d', numEsq, numDir)

main()
