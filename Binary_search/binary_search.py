#二分探索
#leftとrightという2つの変数を使って、範囲を絞り込む。目的の値と一致したらその位置を返し、一致しない場合にはleftとrightの値を再設定する。=>探索範囲を絞り込んでいく。

def binary_search(data, value):
    left = 0   #探索する左端を設定
    right = len(data) - 1  #探索する範囲の右端を設定

    while left <= right:
        mid = (left + right) // 2  #探索する範囲の中央を計算
        if data[mid] == value:
            #目的の値が中央の値と一致した場合にはその位置を返す
            return mid
        elif data[mid] < value:
            #目的の値が中央よりも大きい場合には探索範囲の左を変える
            left = mid + 1
        else:
            #目的の値が中央より小さい場合には探索範囲の右を変える
            right = mid - 1
    #見つからなかった場合
    return -1

data = [10,20,30,40,50,60,70,80,90]
print(binary_search(data, 90))