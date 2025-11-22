from scipy import integrate 
from scipy import optimize
from scipy import linalg
import math

def f(x):
    return (x+3)-math.exp(x)

a=optimize.newton(f,2)
b=optimize.newton(f,-3)

if a>b:
    a2=b
    b2=a

ans=integrate.quad(f,a2,b2)
print(ans)

print('3×3の行列Aを入力してください。')

A=[]
for i in range(3):
    inp2=[]
    for j in range(3):
        inp2.append(int(input()))
    A.append(inp2)
        
print('1×3の行列Bを入力してください。')
B=[]
for i in range(3):
    B.append(int(input()))

if linalg.det(A)==0:
    print('解なし')
    print('行列Aの行列固有値と固有ベクトルは{}です。'.format(linalg.eig(A)))
    
else:
    print('AX=Bを満たすXの値は{}です。'.format(linalg.solve(A,B)))
    print('固有値と固有ベクトルは{}です。'.format(linalg.eig(A)))

