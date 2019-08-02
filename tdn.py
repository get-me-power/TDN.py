from pykakasi import kakasi
boin = ['a', 'i', 'u', 'e', 'o']
text = input('漢字を入力: ')
kakasi = kakasi()
kakasi.setMode('J', 'a')
conv = kakasi.getConverter()
for i in range(len(boin)):
    text = conv.do(text).replace(boin[i],'')
    print(text)
print('result', text)
