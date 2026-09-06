word = input() + ' запретил букву'
alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
spi = ''
for j in range(len(alph)):
    if alph[j] in word:
        spi += alph[j]
    else:
        continue
for i in range(len(spi)):
        while spi[i] in word:
            if i == 0:
                print(word, spi[i])
            index = word.find(spi[i])
            word = word.replace(spi[i], '')
            print(word, spi[i+1])




word = input() + ' запретил букву'
alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
spi = ''
for i in range(len(alph)):
        while alph[i] in word:
            if alph[i] in word:
                if i == 0:
                    print(word, alph[i])
                index = word.find(alph[i])
                word = word.replace(alph[i], '')
                print(word, alph[i+1])
            else:
                continue