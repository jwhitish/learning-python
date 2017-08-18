#filters a list input to return only even numbers

def purify(list):
  evens = []
  for i in list:
    if i % 2 == 0:
      evens.append(i)
  return evens
