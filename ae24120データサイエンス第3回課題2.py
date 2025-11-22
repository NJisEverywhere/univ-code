import numpy as np

a=np.array([])
print('10個の整数を入力してください。')
for i in range(10):
    inp=input()
    inp=int(inp)
    a=np.append(a,inp)
    
print('10個の整数の平均値、最大値、最小値はそれぞれ{}と{}と{}です。'.format(a.mean(),a.max(), a.min()))

class person:
    
    def __init__(self):
        self.name=''
        self.height=0
        self.weight=0
        
    def set(self, name, height, weight):
        self.name=name
        self.height=height
        self.weight=weight
        
    def print(self):
        print('名前 {},　身長 {}, 体重 {}'.format(self.name, self.height, self.weight))
        
    def bmi(self):
        return self.weight / (self.height*self.height)
    
    def info(self):
        print('名前：{}、身長：{}、体重：{}、BMI：{}'.format(self.name, self.height, self.weight, self.bmi()))
        
        
people = []
for i in range(5):
    print('{}人目のデータを入力してください。'.format(i+1))
    name=input('名前:')
    height=float(input('身長(m):'))
    weight=float(input('体重（kg）:'))
    
    p=person()
    p.set(name, height, weight)
    people.append(p)
    print()
    
for p in people:
    p.info()
    
    
    
