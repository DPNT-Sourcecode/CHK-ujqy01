import string


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # alphabet = string.ascii_uppercase
    alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
    price_list = [{'name': 'A', 'price': 50,'on_offer': True,'offer_quantity':3,'offer_price':130},
                  {'name': 'B', 'price':30,'on_offer': True,'offer_quantity':2,'offer_price':45},
                  {'name': 'C', 'price': 20,'on_offer': False},
                  {'name': 'D', 'price': 15,'on_offer': False}]
    total_price = 0
    skus = skus.split()

    skus.sort()
    print('')
    count = 0
    offer_item_name = ''
    for sku in skus:
        print(sku)
        if sku not in alphabet:
            return -1

        price_list_item = next((item for item in price_list if item["name"] == sku), None)

        if price_list_item is not None:
            if price_list_item.get('on_offer'):
                on_offer_items_count = skus.count(sku)
                price = on_offer_items_count / price_list_item.get('offer_quantity') * price_list_item.get('offer_price') + on_offer_items_count%price_list_item.get('offer_quantity') * price_list_item.get('price')
                skus = list(filter(lambda a: a != sku, skus))
            else:
                price = price_list_item.get('price')


        total_price += price
        print('total_price',total_price)
    return total_price






