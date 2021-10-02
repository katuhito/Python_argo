import math #pythonの数学モジュールを読み込み

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1): #平方根を計算する
        if n % i == 0: #割り切れるかどうかを判定
            return False #割り切れれば素数ではない
    return True #いずれの数でも割りきれなかったときはそれは素数である