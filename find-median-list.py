#takes the items in a list and returns the median value

def median(x):
  y=sorted(x)
  print y

  if len(y) % 2 == 0:           #even branch
    print "there are", len(y), "numbers"
    lower = (len(y) / 2) - 1
    upper = (len(y) / 2)
    print float(y[int(lower)])
    float_lower = float(y[int(lower)])
    print float(y[int(upper)])
    float_upper = float(y[int(upper)])
    middle = (float_upper + float_lower) / 2.0
    print middle

  else:                         #odd branch
    print y[len(y) / 2]
