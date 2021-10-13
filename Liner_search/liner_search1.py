#線形探索
#dataリストから40を探す

data = [50,30,90,10,20,70,60,40,80]
#処理状況を管理する（初期値はFalse）
found = False

for i in range(len(data)):
    #見つけたい値と一致したか？
    if data[i] == 40:
        print(i)
        #見つかったことを処理状況としてセット
        found = True
        break
# 見つからなかった場合
if not found:
    print('Not Found')
    

