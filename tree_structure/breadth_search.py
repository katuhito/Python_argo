#幅優先探索
#木構造(1~14までの要素)を上から順に処理（出力）する。
#ノードの位置(インデックス)をリストで保持する(0~14まで)
tree =[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]]

data = [0]  #初期化
while len(data) > 0:
    pos = data.pop(0)  #先頭から取り出し
    print(pos, end='')
    for i in tree[pos]:
        data.append(i)  #末尾に追加