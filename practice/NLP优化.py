"""
第一问：你能否把 NLP 例子中的 word count 实现一遍？不过这次，in.txt 可能非常非常大（意味着你不能一次读取到内存中），
而 output.txt 不会很大（意味着重复的单词数量很多）。
提示：你可能需要每次读取一定长度的字符串，进行处理，然后再读取下一次的。
但是如果单纯按照长度划分，你可能会把一个单词隔断开，所以需要细心处理这种边界情况。
"""
import re

CHUNK_SIZE = 100


def parse_to_word_list(text, last_word, word_list):
    text = re.sub(r'[^\w ]', ' ', last_word + text)
    text = text.lower()
    cur_word_list = text.split(' ')
    cur_word_list, last_word = cur_word_list[:-1], cur_word_list[-1]
    word_list += filter(None, cur_word_list)
    return last_word


def solve():
    with open('in.txt', 'r') as fin:
        word_list, last_word = [], ''
        while True:
            text = fin.read(CHUNK_SIZE)
            if not text:
                break  # 读取完毕，中断循环
            last_word = parse_to_word_list(text, last_word, word_list)

        word_cnt = {}
        for word in word_list:
            if word not in word_cnt:
                word_cnt[word] = 0
            word_cnt[word] += 1

        sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_word_cnt
