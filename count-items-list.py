#returns the number of 'item' in a list called 'sequence'
def count(sequence, item):
  count = 0
  for i in sequence:
    if i == item:
      count += 1
  return count
