from sys import argv

def main():
    x, y = 0, 0
    dx = 0.01

    for n in xrange(int(argv[1])):
        y = y + 2 * x * dx
        x = x + dx

    print 'Numerical: %.4f' % (y)
    print 'Analitical: %.4f' % (x ** 2)

if __name__ == '__main__':
    main()
