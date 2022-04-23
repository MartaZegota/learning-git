shopping_dict = {
    "piekarnia": ['chleb', 'pączek', 'bułki'],
    "warzywniak": ['marchew', 'seler', 'rukola']
}

shops = shopping_dict.keys()
products = shopping_dict.values()
product = []
shop = []

shop_dict = dict(shopping_dict)
for shop, product in shop_dict.items():
  print(f"Idę do {shop} i kupuję następujące {product}")
  for products in product:
      print(products.capitalize())