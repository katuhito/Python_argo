"""8クイーン"""
#チェスにおけるクイーンの動きは、将棋の飛車と角を合わせた動きと同じである。
#チェーン盤面に8つのクイーンを、お互いの利き範囲内に入らないように配置することが目的である。
#縦横の動きの判定は、同じ行と列に2つ以上のクイーンが配置されることはないため、それぞれの列においてクイーンを配置した行を保持することにする。
#=>1列目は1〜8行のいずれか、2行目は残りの7行のいずれか、というように考えると、8*7*6*5*4*3*2*1通りになる。この方法で全検索のパターン数を大幅に少なくする。
#斜めの利きの判定は、クイーンは左側から順に配置するので、それまでに配置したものが斜めの利きに入っているか調べる方法で、左上と左下を調べることで判定できる。
#左上については、1列左の1行上と、2列左の2行上を調べれば良いので、リストの位置とリストの値(行番号)
#左の列から順番に配置可能な位置をリストに追加していき、全て配置できれば完成である。リストに追加するときには、同じ行にならないようにすることと、斜めの利きに入らないように調べながら配置する。

N = 8

#斜めのチェック
def check(x, col):
    #配置済みの行を逆順に調べる
    for i, row in enumerate(reversed(col)):
        if(x + i + 1 == row) or (x - i - 1 == row):  #左上と左下にあるか
            return False
    return True

def search(col):
    if len(col) == N: #全て配置できれば出力
        print(col)
        return

    for i in range(N):
        if i not in col:  #同じ行は使わない
            if check(i, col):
                col.append(i)
                search(col) #再帰的に探索する
                col.pop()

search([])

