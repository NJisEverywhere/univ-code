def maxandmin(a):
    M=a[0]
    m=a[0]
    for i in a:
        if i>M:
            M=i
        if i<m:
            m=i
    return M, m

a=[]
print('1.数値を5つ入力してください。')
for i in range(5):
    inp=input()
    inp=float(inp)
    a.append(inp)
    
maximam, minimam = maxandmin(a)
print('入力された整数の最大値と最小値はそれぞれ{},{}です。'.format(maximam, minimam))

def tikaiyatsu(a,b):
    diff=[]
    for i in a:
        if i>=b:
            d=i-b
            diff.append(d)
        else:
            d=b-i
            diff.append(d)
    count=0
    bango=0
    min=diff[0]
    for i in diff:
        if min>=i:
            min=i
            bango=count
        count+=1
    return a[bango]

a=[]
print('2.小数を5つ入力してください。')
for i in range(5):
    inp=input()
    inp=float(inp)
    a.append(inp)
b=input('小数を一つ入力してください。')
b=float(b)
answer=tikaiyatsu(a,b)
print('初めに入力された5つの数値の中で6つ目に入力された数値と最も近いものは{}です。'.format(answer))

