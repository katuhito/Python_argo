import sys   #エラー時に強制終了するためのモジュール

#釣り銭の金額を求める
insert_price = input('insert: ')
if not insert_price.isdecimal():
    print('整数を入力してください。')
    sys.exit()   #エラーがあれば強制終了

product_price = input('insert: ')
if not product_price.isdecimal():
    print('整数を入力してください。')
    sys.exit()   #エラーがあれば強制終了

change = int(insert_price) - int(product_price)
if change < 0:
    print('金額が不足しています')
    sys.exit()   #エラーがあれば強制終了

print('change: ' + str(change))

#紙幣と硬貨のリスト
coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r = change // i
    change %= i
    print(str(i) + ':' + str(r))
    