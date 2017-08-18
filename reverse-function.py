#creates a function that returns the reverse of the text entered
#commented out lines are for debugging

def reverse(text):
  str_text = str(text)
  list_text = []

  for i in str_text:
    list_text.append(i)
  #print list_text

  rev_text = []

  key = len(list_text) - 1
  while key > -1:
    for i in list_text:
      rev_text.append(list_text[key])
      key -= 1
  #for i in rev_text:
    #print i,
  end = ''.join(rev_text)
  print end


text = 'Python!'
reverse(text)
