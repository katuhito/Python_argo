x = 10 #グローバル変数に値をセット

def check():
    a = 30 #ローカル変数に値をセット
    print(x) #グローバル変数出力
    print(a) #ローカル変数出力
    return

check() #check関数呼び出し
print(x) #グローバル変数出力
print(a) #ローカル変数　=> 関数内でしかアクセスできない