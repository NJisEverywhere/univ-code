import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kadai.csv')

print('１．１行データを追加する。')
print('２．１行データを削除する。')
print('３．全データを表示する。')
print('４．全データの統計量を求める。')
print('５．名前を指定してその人のデータを表示する。')
print('６．指定した項目で並べ替えたものを表示する。')
print('７．指定したデータだけを表示する。（例:score1<40）')
print('8.列を指定して折れ線グラフにする。')
print('9.列を指定してヒストグラムを描画する。')
print('10列を2つ指定して散布図を描画する。')
print('11.列を指定して、10点刻みで円グラフを描画する。')
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
        print(df.describe())
        
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
            
    # 8. 列を指定して折れ線グラフにする。
    elif inp == '8':
        a = input('折れ線グラフにしたい列を指定してください。')
        plot_data=df[a].values.tolist()
        plt.plot(plot_data)
        plt.ylabel(a)
        plt.show
        
        
    elif inp == '9':
        a=input('ヒストグラムを描画したい列を指定してください。')
        plot_data=df[a].values.tolist()
        plt.hist(plot_data,bins=10)
        plt.show()
        
    elif inp == '10':
        a=input('散布図として描画する列を2つ指定してください。')
        b=input()
        plot_data=df[a].values.tolist()
        plot_data2=df[b].values.tolist()
        plt.scatter(plot_data, plot_data2)
        plt.xlabel(a)
        plt.ylabel(b)
        plt.show()
        
    elif inp == '11':
        a=input('円グラフを描画する列を指定してください。')
        labels = ["1~10","11~20", "21~30", "31~40", "41~50", "51~60", "61~70", "71~80", "81~90", "91~100"]
        plot_data=df[a].values.tolist()
        
        list0 = len(df[(df[a] >= 1) & (df[a] <= 10)])
        list1 = len(df[(df[a] >= 11) & (df[a] <= 20)])
        list2 = len(df[(df[a] >= 21) & (df[a] <= 30)])
        list3 = len(df[(df[a] >= 31) & (df[a] <= 40)])
        list4 = len(df[(df[a] >= 41) & (df[a] <= 50)])
        list5 = len(df[(df[a] >= 51) & (df[a] <= 60)])
        list6 = len(df[(df[a] >= 61) & (df[a] <= 70)])
        list7 = len(df[(df[a] >= 71) & (df[a] <= 80)])
        list8 = len(df[(df[a] >= 81) & (df[a] <= 90)])
        list9 = len(df[(df[a] >= 91) & (df[a] <= 100)])
        
        size = [list0, list1, list2, list3, list4, list5, list6, list7, list8, list9]
        
        plt.pie(size, labels=labels)
        
        plt.show()