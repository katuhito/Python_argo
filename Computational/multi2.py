#体積を求める計算量
n = 10

# 縦の長さを1からnまで
for i in range(1, n):
    # 横の長さを1からnまで
    for j in range(1, n):
        #高さを1からnまで
        for k in range(1, n):
            # 体積を出力
            print(str(i) + '*' + str(j) + '*' + str(k) + '=' + str(i * j * k))