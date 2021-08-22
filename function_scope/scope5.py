x = 10 #グローバル変数

def reset():
    global x  #グローバル変数として宣言される
    x = 30    #グローバル変数に代入される
    print(x)

reset()    #グローバル変数出力
print(x)   #グローバル変数出力
