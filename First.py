def palindrom(text):
  s = [i[::-1] for i in text.split()]
  s = list(' '.join(s))
  s = [i for i in s if i.isalpha()]
  text = list(text)
  for i in range(len(text)):
    if not text[i].isalpha():
      s.insert(i, text[i])
  return ''.join(s)
string = 'a1bcd efg!h'
print(string, palindrom(string), sep = '\n')
