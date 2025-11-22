a=input('1.二つの整数を入力してください。')
b=input()
a=int(a)
b=int(b)

if a>b:
    print('{}より{}のほうが大きい'.format(b,a))
elif b>a:
    print('{}より{}のほうが大きい'.format(a,b))
else :
    print('{}と{}は等しい'.format(a,b))
    

num=1
count=0
sum=0
print('2.')
while num!=0:
    num=input('整数を入力してください。（0を入力で終了）') 
    num=int(num)
    sum+=num
    count+=1
count=count-1
print('入力された整数の平均は{}'.format(sum/count))    
