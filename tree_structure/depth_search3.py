#深さ優先探索（通りがけ順）
#2分木の左側の子ノードをたどった後に処理し、続いて右側の子ノードをたどる。

tree =[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]]

def search(pos):
    if len(tree[pos]) == 2:   #子が2つある場合
        search(tree[pos][0])
        print(pos, end='')   #左のノードと右のノードの間に出力
        search(tree[pos][1])
    elif len(tree[pos]) == 1:   #子が1つの場合
        search(tree[pos][0])
        print(pos, end='')   #左のノードを調べた後に出力
    else:   #配下のノードがないとき
        print(pos, end='')

search(0)
