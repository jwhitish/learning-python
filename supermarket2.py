shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

#calculate total shopping bill, reduce stock, print bill
def compute_bill(food):
  total = 0
  for key in food:
    if stock[key] > 0:
      total += prices[key]
      stock[key] -= 1
  print total
