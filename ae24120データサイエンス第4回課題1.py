class person:
    def __init__(self):
        self.name=''
        self.age=0
        
    def set(self, name, age):
        self.name=name
        self.age=age
        
    def info(self):
        print('名前：{}、年齢：{}'.format(self.name, self.age))
        
        
class student(person):
    def __init__(self):
        super().__init__()
        self.score=[]
        
    def set(self, name, age, score):
        super().set(name, age)
        self.score=score
        
    def showscore(self):
        print('点数：{}'.format(self.score))
        
    def fullinfo(self):
        self.info()
        self.showscore()
        
        
people = []
for i in range(3):
    print('{}人目の情報を入力してください。'.format(i+1))
    name=input('名前：')
    age=input('年齢：')
    
    score = []
    for j in range(5):
        t=int(input('{}教科目：'.format(j+1)))
        score.append(t)
        
    s=student()
    s.set(name, age, score)
    people.append(s)
    print()
    
a=1
for p in people:
    print('{}人目'.format(a))
    p.fullinfo()
    print()
    a+=1