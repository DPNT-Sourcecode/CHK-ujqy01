import string


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # alphabet = string.ascii_uppercase
    alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
    price_list = [{'name': 'A', 'price': 50},{'B':30},{'C':20},{'D':15}]

    skus = skus.split()
    for sku in skus:
        if sku not in alphabet:
            return -1
        next((item for item in price_list if item["name"] == sku), None)

    return 0



