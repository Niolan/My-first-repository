def palindrom(text):
  s = [i[::-1] for i in text.split()]
  s = list(' '.join(s))
  s = [i for i in s if i.isalpha()]
  text = list(text)
  for i in range(len(text)):
    if not text[i].isalpha():
      s.insert(i, text[i])
  return ''.join(s)


if __name__ == '__main__':
    cases = [
        ('abed efgh', 'deba hgfe' ),
        ('a1bcd efg!h', 'd1cba hgf!e'),
        ('', ''),
]
for text, reversed_text in cases:
    #print(f'{text}, Эталон: {reversed_text}, Функция: {palindrom(text)}')
    assert palindrom(text) == reversed_text, 'The text was reversed incorrect!'