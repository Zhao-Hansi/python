"""
7. 词频统计
你想分析某个英语写作者的写作风格，你想先从他使用词语的频率入手。

功能描述： 分析仓库根目录的 words.txt 文件里的词频，按照出现频率由高到低排列结果，不区分大小写，过滤掉标点（可以使用正则表达式）。结果类似ok：234，play：122，funny：78
"""

import re

word_freq = {}

with open('words.txt', 'r', encoding='utf-8') as f:
    for line in f:
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            if word not in word_freq:
                word_freq[word] = 0
            word_freq[word] += 1

sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

for word, freq in sorted_word_freq:
    print(f'{word}: {freq}')