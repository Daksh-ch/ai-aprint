products = [
 {"name":"Laptop", "price":50000, "stock":10},
 {"name":"Mouse", "price":500, "stock":100},
 {"name":"Keyboard", "price":1500, "stock":50}
]
total_inventory = 0
for product in products:
    print(product['name'] + " - " + str(product['price']) + " - stock:" + str(product['stock']))
    print(f"product['name] - {product['price']} - stock: {product['stock']}")
    total_inventory += product['price'] * product['stock']

print("Total Inventory Value: ", total_inventory)