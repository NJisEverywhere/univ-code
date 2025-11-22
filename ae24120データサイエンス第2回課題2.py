list1=[]
for i in range(5):
    inp=input('１．整数を５つ入力してください。')
    inp=int(inp)
    list1.append(inp)
    
sum=0
for i in list1:
    sum+=i

avg=sum/5

max=list1[0]
for i in list1:
    if max<i:
        max=i

print('5つの整数の平均値は{}、最大値は{}'.format(avg,max))

list2=[]
for i in range(5):
    inp2=input('2.単語を5つ入力してください。')
    list2.append(inp2)

word=input('単語を1つ入力してください。')
hantei=0
for i in list2:
    if word==i:
        hantei=1

if hantei==1:
    print('入力された単語は最初の5つに含まれています。')
else:
    print('入力された単語は最初の5つに含まれていません。')
    

list3=[]
for i in range(2,1001):
    flag=True
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
    if flag==True:
        list3.append(i)

print('３．1000までの素数は、{}'.format(list3))