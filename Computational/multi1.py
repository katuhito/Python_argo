#かけ算の九九
n = 10

#1つめの数を1からnまで繰り返す
for i in range(1, n):
    #2つめの数を1からnまで繰り返す
    for j in range(1, n):
        # かけ算の答えを出力
        print(str(i) + '*' + str(j) + '=' + str(i * j))
        

