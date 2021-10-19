#右手法による深さ優先探索
#迷路の右側に手をついて触りながら移動する方法であり、壁に突き当たった場合も、向きを左に変えることを繰り返すことで、進み続ける。
#プログラムでは、進行方向を保持しておき、その右側、前、左側、後ろの順番に調べながら進める方向に進む。
#また、未訪問の場所に進む場合は移動回数を増やし、訪問済みの場所に進む場合は移動回数を減らすことで、最短経路の長さを求めることができる。

maze = [
    [9,9,9,9,9,9,9,9,9,9,9,9],
    [9,0,0,0,9,0,0,0,0,0,0,9],
    [9,0,9,0,0,0,9,9,0,9,0,9],
    [9,0,9,9,0,9,0,0,0,9,0,9],
    [9,0,0,0,9,0,0,9,9,0,9,9],
    [9,9,9,0,0,9,0,9,0,0,0,9],
    [9,0,0,0,9,0,9,0,0,9,1,9],
    [9,0,9,0,0,0,0,9,0,0,9,9],
    [9,0,0,9,0,9,0,0,9,0,0,9],
    [9,0,9,0,9,0,9,0,0,9,0,9],
    [9,0,0,0,0,0,0,9,0,0,0,9],
    [9,9,9,9,9,9,9,9,9,9,9,9]
]

#右手法での移動方向（下、右、上、左）をセット
dir = [[1,0],[0,1],[-1,0],[0,-1]]
#スタート位置(x座標、ｙ座標、移動回数、方向)をセット
x, y, depth, d = 1, 1, 0, 0

while maze[x][y] != 1:
    #探索済みとしてセット
    maze[x][y] = 2

    #右手法で探索
    for i in range(len(dir)):
        #進行方向の右側から順に探す
        j = (d + i - 1) % len(dir)  #移動方向の個数で割って余りを求めることで、次の方向を決める
        if maze[x + dir[j][0]][y + dir[j][1]] < 2:
            #未訪問の場合は進めて移動回数を増やす
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth += 1
            break
        elif maze[x + dir[j][0]][y + dir[j][1]] == 2:
            #訪問済みの場合には進めて移動回数を減らす
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth -= 1
            break

print(depth)

