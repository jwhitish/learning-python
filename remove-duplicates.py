#remove duplicates from a list

def remove_duplicates(list):
  new_list = []
  for i in list:
    if i in new_list:
      pass
    else:
      new_list.append(i)
  print new_list
