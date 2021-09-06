def palin(text):
    s = text.split()
    for i in range(len(s)):
        k = ''
        for j in s[i]:
            if j.isalpha():
                k += j
        s[i] = k[::-1]
    s = ''.join(s)

    for i in range(len(text)):
        if not text[i].isalpha():
            s = s[:i] + text[i] + s[i:]
    return s

string = 'a1bcd efg!h'
print(palin(string))