words = input('Введите строку из нескольких слов, разделенных пробелом: ')
words_list = words.split()
print(words_list)

for i in range(0, len(words_list), 1):
    print(i+1, words_list[i][:10:])