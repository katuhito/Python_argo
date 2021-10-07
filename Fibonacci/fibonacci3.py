#メモ化によって処理を高速化
#再帰的処理

#辞書に終了条件の値を入れる
memo = {1:1, 2:1}

def fibonacci(n):
    if n in memo:
        return memo[n]  #辞書に登録されていれば、その値を返す

    #辞書に登録が無ければ、計算して辞書に登録する
    memo[n] = fibonacci(n - 2) + fibonacci(n -1)
    return memo[n]

print(fibonacci(30))

