
str = "I have a dream that one day this nation will rise up and live out the true meaning of its creed, " \
      "I am a handsome man "

word_list = str.split()
word_upper = []
word_count = {}

for word in word_list:
    word_upper.append(word.upper())
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

max_word = max(word_count, key=word_count.get)

print("在字符串中出现次数最多的单词为：", max_word, "，出现了", word_count[max_word], "次")

print(word_upper)