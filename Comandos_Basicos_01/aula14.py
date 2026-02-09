a = 'AAAAAA'
b = 'B'
c = 1.1
string = 'a={}, b={}, c={:.2f} {}'
string2 = 'a={1}, b={0}, c={2:.2f} {3}'
formato = string.format(a, b, c, 'extra')
formato2 = string2.format(a, b, c, 'extra')

print(formato)
print(formato2)