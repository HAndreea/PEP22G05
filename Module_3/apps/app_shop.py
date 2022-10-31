shop1 = {"apples": 7.5, "plums": 8.3, "bread": 3.5}
shop2 = {"apples": 7.6, "plums": 8.1, "bread": 3.5}
shop3 = {"apples": 7.4, "plums": 8.9, "bread": 3.5}

shopping_cart = {"apples": 3, "plums": 5, "bread": 4}

shops = {'lid': shop1, 'kau': shop2, 'pro': shop3}

# Cheapest shop
shop1_total_price = 0
result = {}

for shop_name, shop in shops.items():
    for product, quantity in shopping_cart.items():
        price = quantity * shop[product]
        if(result.get(shop_name)):
        #if shop_name in result.keys():
            result.update({shop_name: result[shop_name] + price})
        else:
            result.update({shop_name: price})
print(result)

min_price = min(result.values())

for m in result.keys():
    if result[m] == min_price:
        print("magazin", m)

"""
shops_total_price = {}
shop1_price = 0
shop2_price = 0
shop3_price = 0



for key in shopping_cart.keys():
    shop1_price += shopping_cart[key] * shop1[key]
    shop2_price += shopping_cart[key] * shop2[key]
    shop3_price += shopping_cart[key] * shop3[key]

shops_total_price.update({shop1: shop1_price, shop2: shop2_price, shop3: shop3_price})

min  = shop1_price
for shops in shops_total_price.keys():
    if(shops_total_price[shops] < min):
        min = shops_total_price[shops]


print(shops_total_price)"""
