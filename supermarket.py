#merchant stock program
#price dictionary and stock count
prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

#prints item stock and pricing
for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]
  print

#prints value of all inventory combined
total = 0

for key in prices:
  total += prices[key] * stock[key]
print total
