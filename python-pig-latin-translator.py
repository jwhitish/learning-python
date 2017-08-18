#suffix variable
pyg = 'ay'

#user input
original = raw_input('Enter a word: ')

#check for real word
if len(original) > 0 and original.isalpha():
  #translate to new word
  word = original.lower()
  first = word[0]
  new_word = word[1:] + first + pyg
  print new_word
else:
  print 'empty'
