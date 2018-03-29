#takes a list of lists and returns a pretty table of columns

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
  kMax = []
  colWidth = 0
  iMax = 0
  for i in data:        #checks sublist len
    for k in i:
      if len(i) > iMax:
        iMax = len(i)
  for i in data:        #creates list of max widths
    max = 0
    for k in i:
      if len(k) > max:
        max = len(k)
    kMax.append(max)
  for i in kMax:        #sets col widths
    if i > colWidth:
      colWidth = i
  x = 0
  while x < iMax:       #prints columns
    for i in data:
      print(str(i[x].rjust(colWidth))),
    print('')
    x += 1


printTable(tableData)
