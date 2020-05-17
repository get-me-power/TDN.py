from pykakasi import kakasi
import numpy as np

vowels = ['a', 'i', 'u', 'e', 'o']

text = input('漢字を入力: ')

kakasi = kakasi()
kakasi.setMode('J', 'a')
conv = kakasi.getConverter()

for vowel in vowels:
    text = conv.do(text).replace(vowel, '')
    print(text)

print('result :', text)
idjfajjdj
