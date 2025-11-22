import pandas as pd

df = pd.read_csv('kadai.csv')

print('１．１行データを追加する。')
print('２．１行データを削除する。')
print('３．全データを表示する。')
print('４．全データの統計量を求める。')
print('５．名前を指定してその人のデータを表示する。')
print('６．指定した項目で並べ替えたものを表示する。')
print('７．指定したデータだけを表示する。（例:score1<40）')
print('０．終了する。')

while True:
    inp = input('命令を入力してください')
    if inp == '0':
        print('終了します。')
        break
    elif inp == '1':
        print('追加するデータを入力してください。')
        name=input('名前を入力してください。')
        score=[name]
        for i in range(5):
            s=int(input('点数を入力してください。'))
            score.append(s)
        df.loc[len(df)]=score
       
    elif inp == '2':
        a = input('何行目を削除しますか。')
        df=df.drop(a)
    
    elif inp == '3':
        print(df)
        
    elif inp == '4':
        print(df.discribe())
        
    elif inp == '5':
        a=input('データを表示したい人の名前を入力してください。')
        print(df(df.name==a))
        
    elif inp == '6':
        a=input('並べ替える列名を入力してください。')
        print(df.sort_value(by=a))
    elif inp == '7':
        print('条件を入力してください。')
        a=input('条件の列名を入力してください。')
        b=input('（不）等号を入力してください。')
        c=int(input('値を入力してください。'))
        if b=='=':
            print(df[df[a]==c])
        elif b=='>':
            print(df[df[a]>c])
        elif b=='<':
            print(df[df[a]<c])
        else :
            print('正しい入力ではありません。')
