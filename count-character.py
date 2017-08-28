#enter a sentence and the number of times each character is repeated will be returned as a dictionary

message = str(input('Enter a sentence: '))

count = {}

for character in message:
  count.setdefault(character, 0)
  count[character] = count[character] + 1

#print(count)

for k, v in count.items():
  print('Letter: ' + str(k) + '\n' 'Times Used: ' + str(v))
