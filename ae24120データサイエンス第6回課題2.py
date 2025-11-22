import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math


heikin=float(input('平均を入力してください。'))
bunsan=float(input('分散を入力してください。'))
hyoujun=math.sqrt(bunsan)

x=np.linspace(heikin-4*hyoujun, heikin+4*hyoujun, 100)
y=norm.pdf(x, heikin, hyoujun)

plt.plot(x,y)
plt.show()

for i in range(3):
    yr=norm.rvs(size=10**(i+2))
    plt.hist(yr, bins=30)
    plt.show()
    
    
import pandas as pd
from scipy import stats

df = pd.read_csv('potato.csv')

Aavg=df.A.mean()
Bavg=df.B.mean()
Cavg=df.C.mean()

Al=df.A.count()
Bl=df.B.count()
Cl=df.C.count()

A95=norm.isf(0.95,130,math.sqrt(9/Al))
B95=norm.isf(0.95,130,math.sqrt(9/Bl))
C95=norm.isf(0.95,130,math.sqrt(9/Cl))


if Aavg<=A95:
    print('Aは平均１３０とは言えない。')
else:
    print('Aは平均１３０といえる。')
    
if Bavg<=B95:
    print('Bは平均１３０とは言えない。')
else:
    print('Bは平均１３０といえる。')
    
if Bavg<=C95:
    print('Cは平均１３０とは言えない。')
else:
    print('Cは平均１３０といえる。')
    

A=[]
for i in df.A:
    if math.isnan(i)==False:
        A.append(i)
        
B=[]
for i in df.B:
    if math.isnan(i)==False:
        B.append(i)
        
C=[]
for i in df.C:
    if math.isnan(i)==False:
        C.append(i)
        

t,pAB=stats.ttest_ind(A,B,equal_var=False)
if pAB<=0.05:
    print('AとBは違いがある。')
else:
    print('AとBは同じ。')
    
    
t,pBC=stats.ttest_ind(B,C,equal_var=False)
if pAB<=0.05:
    print('BとCは違いがある。')
else:
    print('BとCは同じ。')
    
    
t,pCA=stats.ttest_ind(C,A,equal_var=False)
if pCA<=0.05:
    print('CとAは違いがある。')
else:
    print('CとAは同じ。')