#returns input string without vowels

def anti_vowel(text):
  vowels = "aeiouAEIOU"
  new = []
  for i in text:
    if i not in vowels:
      new.append(i)
  end = ''.join(new)
  print end
