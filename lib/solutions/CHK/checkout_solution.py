import string


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # alphabet = string.ascii_uppercase
    alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
    price_list = [{'name': 'A', 'price': 50},{'name': 'B', 'price':30},{'name': 'C', 'price': 20},{'name': 'D', 'price': 15}]
    total_price = 0
    skus = skus.split()
    for sku in skus:
        if sku not in alphabet:
            return -1
        price_list_item = next((item for item in price_list if item["name"] == sku), None)
        if price_list_item is not None:
            price = price_list_item.get('price',0)
        total_price += price
    return total_price





