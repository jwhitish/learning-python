#censors a 'word' out of a given sentence 'text' using asterisks in place of letters

def censor(text, word):
  censored = text.replace(word, (len(word) * '*'))
  return censored
