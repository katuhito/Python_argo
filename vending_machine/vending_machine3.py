#釣り銭の金額を求める
insert_price = input('insert: ')
product_price = input('insert: ')
change = int(insert_price) - int(product_price)
print('change: ' + str(change))

#紙幣と硬貨のリスト
coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r = change // i
    change %= i
    print(str(i) + ':' + str(r))
    