
def load_dict():
    d = {}
    with open("dict.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            eng, jp = line.split(",")
            d[eng] = jp
    return d



def save_dict(d):
    with open("dict.txt", "w", encoding="utf-8") as f:
        for eng, jp in d.items():
            f.write(eng + "," + jp + "\n")



def main():
    dic = load_dict()
    inp = ""

    while inp != "0":
        print("\n--- メニュー ---")
        print("1: 登録されている英単語をすべて表示")
        print("2: 英単語を検索")
        print("3: 新しい単語ペアを登録")
        print("4: 単語を削除")
        print("0: 終了")

        inp = input("命令を入力してください: ")

        if inp == "1":
            for k in dic.keys():
                print(k)

        elif inp == "2":
            word = input("英単語を入力してください: ")
            if word in dic:
                print(dic[word])
            else:
                print("登録されていません。")

        elif inp == "3":
            eng = input("英単語を入力してください: ")
            jp = input("日本語訳を入力してください: ")
            dic[eng] = jp

        elif inp == "4":
            eng = input("削除する英単語を入力してください: ")
            if eng in dic:
                del dic[eng]
            else:
                print("登録されていません。")

    save_dict(dic)


main()
