def f(x):
    return ((2 * x * x) - (5 * x) + 3) / 5


def g(x):
    return (2 * x * x + 3) / 5


def fixedPointIteration(x0, e, n):
    print('FIXED POINT ITERATION')
    tries = 1
    flag = 1
    condition = True
    i = 0
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x-0.5%d = %0.6f and f(x-%d) = %0.6f' % (tries, x1, f(x1)))

        x0 = x1

        tries = tries + 1

        if tries > n:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
n = input('Maximum tries: ')

x0 = float(x0)
e = float(e)

n = int(n)

fixedPointIteration(x0, e, n)
