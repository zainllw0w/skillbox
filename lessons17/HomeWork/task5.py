text = 'abshabshabs'


start = text.index('h')
stop = text.index('h', start + 1)
rev = text[start:stop + 1]
print(text[:start] + rev[::-1] + text[stop + 1:])