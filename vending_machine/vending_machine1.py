insert_price = input('insert: ')   #投入する金額を受け取る(input関数)

product_price = input('product: ')   #商品の金額を受け取る

change = int(insert_price) - int(product_price)   #おつりの計算

print('change: ' + str(change))

