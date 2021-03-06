#深さ優先探索で探す
#深さ優先探索では、進めるところまで進んで、行き止まると戻って次の経路を探索する。

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

def search(x, y, depth):
    #ゴールに着くと終了
    if maze[x][y] == 1:
        print(depth)
        exit()
    
    #探索済みとしてセット
    maze[x][y] = 2

     #上下左右を探索する
    if maze[x - 1][y] < 2:
        search(x - 1, y, depth + 1)  #移動回数を増やして左を探索
    
    if maze[x + 1][y] < 2:
        search(x + 1, y, depth + 1)  #移動回数を増やして右を探索

    if maze[x][y - 1] < 2:
        search(x, y - 1, depth + 1)  #移動回数を増やして上を探索

    if maze[x][y + 1] < 2:
        search(x, y + 1, depth + 1)  #移動回数を増やして下を探索

    #探索前に戻す
    maze[x][y] = 0

#スタート位置から開始
search(1, 1, 0)
