#Grade calculation software that takes a list of grades and outputs various statistics about those grades

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade,

def grades_sum(scores):
  total = 0
  for score in scores:
    total += score
  return total

def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for i in scores:
    variance += ((average - i) ** 2)
  avg_variance = variance / (float(len(scores)))
  return avg_variance

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)


#the resulting output of the above functions

print "Grades:", print_grades(grades)
print "Sum of grades:", grades_sum(grades)
print "The average grade is:", grades_average(grades)
print "The variance is:", grades_variance(grades)
print "The standard deviation is:", grades_std_deviation(variance)
