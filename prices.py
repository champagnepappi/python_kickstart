prices = { "banana": 4,
          "apple": 3,
          "orange: 2"}

stock = {
    "banana": 8,
    "apple": 1,
    "orange": 0
}

for key in prices:
    print key
    print "price: %s" %prices[key]
    print "stock: %s" %stock[key]
