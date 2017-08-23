#turns a list of items into a coherent sentence

spam = ['apples', 'bananas', 'tofu', 'cats', 'sparrows']

def list2String(x):
  for i in x:
    if i == x[-1]:
      print(str("and " + i))
    else:
      print(str(i + ",")),

list2String(spam)
