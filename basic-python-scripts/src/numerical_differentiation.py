f = lambda x: 2 * x ** 5 - 3 * x ** 4 + 4 * x ** 3 - 5 * x ** 2 + 4 * x - 11
h = 0.05
x = 0.1
print("The actual value of f'''(0.1) is -7.92")
dff1 = (f(x + h) - f(x)) / (h)
dff2 = (f(x + 2 * h) - 2 * f(x + h) + f(x)) / (h ** 2)
dff3 = (f(x + 3 * h) - 3 * f(x + 2 * h) + 3 * f(x + h) - f(x)) / (h ** 3)
print('Solution by forward differences:')
print('f\'(%f) = %f' % (x, dff1))
print('f\'\'(%f) = %f' % (x, dff2))
print('f\'\'\' (%f) = %f' % (x, dff3))

print('Solution by central differences:')
dff4 = (f(x + h) - f(x - h)) / (2 * h)
dff5 = (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)
dff6 = (f(x + 2 * h) - 2 * f(x + h) + 2 * f(x - h) - f(x - 2 * h)) / (2 * h ** 3)

print('f\'(%f) = %f' % (x, dff4))
print('f\'\'(%f) = %f' % (x, dff5))
print('f\'\'\' (%f) = %f' % (x, dff6))

print('Solution by backward differences:')
dff7 = (f(x) - f(x - h)) / h
dff8 = (f(x) - 2 * f(x - h) + f(x - 2 * h)) / (h ** 2)
dff9 = (f(x) - 3 * f(x - h) + 3 * f(x - 2 * h) - f(x - 3 * h)) / (h ** 3)

print('f\'(%f) = %f' % (x, dff7))
print('f\'\'(%f) = %f' % (x, dff8))
print('f\'\'\' (%f) = %f' % (x, dff9))


