import math
import string


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    alphabet = string.ascii_uppercase


    # alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
    price_list = [{'name': 'A', 'price': 50,'on_offer': True,'offer_quantity':3,'offer_price':130},
                  {'name': 'B', 'price':30,'on_offer': True,'offer_quantity':2,'offer_price':45},
                  {'name': 'C', 'price': 20,'on_offer': False},
                  {'name': 'D', 'price': 15,'on_offer': False}]

    offers_list = [{'id':'0','type':'multibuy','offer_item':'A','offer_quantity': 3,'offer_price': 130},
                   {'id':'1','type':'multibuy','offer_item':'A','offer_quantity': 5,'offer_price': 200},
                   {'id': '2','type':'multibuy', 'offer_item': 'B', 'offer_quantity': 2, 'offer_price': 45},
                   {'id': '2', 'type': 'buy_one_get_another', 'offer_item': 'E', 'offer_quantity': 2, 'free_item': 'B'},
                   ]
    total_price = 0

    skus = ''.join(sorted(skus))

    count = 0
    offer_item_name = ''
    for sku in skus:
        print(sku)
        if sku not in alphabet:
            return -1

        price_list_item = next((item for item in price_list if item["name"] == sku), None)

        if price_list_item is not None:
            if price_list_item.get('on_offer') and price_list_item.get('offer_type') == 'multibuy':
                on_offer_items_count = skus.count(sku)
                offer_price = math.trunc(on_offer_items_count / price_list_item.get('offer_quantity')) * price_list_item.get('offer_price')
                non_offer_price = on_offer_items_count%price_list_item.get('offer_quantity') * price_list_item.get('price')
                print('offer_price',offer_price,'non_offer_price',non_offer_price)
                price = offer_price + on_offer_items_count%price_list_item.get('offer_quantity') * price_list_item.get('price')

                skus = list(filter(lambda a: a != sku, skus))
            elif price_list_item.get('on_offer') and price_list_item.get('offer_type') == 'free_item':
                on_offer_items_count = skus.count(sku)
                on_offer_items_count
            else:
                price = price_list_item.get('price')


        total_price += price
        print('total_price',total_price)
    return total_price



