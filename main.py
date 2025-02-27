shops_and_products = {
    "Piekarnia" : ["Chleb", "Pączek", "Bułki"],
    "Warzywniak" : ["Marchew", "Seler", "Rukola"]
}
for shop, products in shops_and_products.items():
    products = [product.capitalize() for product in products]
    print(f"Idę do {shop.capitalize()} i kupuję tam następujące produkty: {products}")
print("W sumie kupię", sum([len(products) for products in shops_and_products.values()]), "produktów.")