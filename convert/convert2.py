#convert1.pyを関数化する
#初期値を設定
n = 18

#関数を定義
def convert(n, base):
    result = ''

    while n > 0:
        result = str(n % base) + result
        n //= base
    return result

print(convert(n, 2))
print(convert(n, 3))
print(convert(n, 8))