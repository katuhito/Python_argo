#フィボナッチ数列6番目の場合

def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    #再帰的処理
    return fibonacci(n -2) + fibonacci(n - 1)

print(fibonacci(6))
