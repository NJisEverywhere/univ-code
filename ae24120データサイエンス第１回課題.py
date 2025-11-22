import math

print('1.二つの整数を入力してください')

a=input()
b=input()
c=int(a)
d=int(b)

print('{}+{}={}'.format(c,d,c+d))
print('{}-{}={}'.format(c,d,c-d))
print('{}*{}={}'.format(c,d,c*d))
print('{}/{}={}'.format(c,d,c//d))


w=input('2.小数を入力してください。入力されたを小数をxとする。')
x=float(w)

print('sin（πｘ)*x^3={}'.format(math.sin(math.pi*x)*x**3))
