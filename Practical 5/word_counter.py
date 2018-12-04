words = str(input("Enter a sentence: "))
word_count = words.split()
word_count.sort()
words_dict = {}
for word in word_count:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1
for word in words_dict:
    print(word, ":", words_dict[word])