#線形探索を行う関数を定義する。
#線形探索は実際には関数として定義して使う。
#目的の値が見つかったのかどうかを変数で管理するのではなく、
#見つかった時点でその位置を返す関数を作成する。
#例えば、引数としてリストと求める値を渡してリストでの位置を返す関数を作る。
# 見つかった場合にはその位置を、見つからなかった場合には-1を返す。

#リストから求める値の位置を検索する関数を定義
def liner_search(data, value):
    for i in range(len(data)):
        #ほしい値が見つかった場合
        if data[i] == value:
            return i
    return -1

data = [50,30,90,10,20,70,60,40,80]
print(liner_search(data, 40))
