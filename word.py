import re
import random

def read_database(path:str):
    words = {}
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            temp = Word(line.strip('\n'))
            if temp.head not in words:
                words[temp.head] = [temp]
            else:
                words[temp.head].append(temp)
    return words


class Word():
    def __init__(self, word:str):
        self.word = word
        self.head = word[0]
        self.tail = word[-1]
        self.next_num = 0

    def __repr__(self):
        return self.word

class WordBase():
    def __init__(self, path=None):
        self.path = r"database.cwp" if not path else path
        self.check_Chinese_regex = r"([\u4e00-\u9fa5]){4}"
        self.words = read_database(self.path)
        self.build_next_candidates()
        random.seed(667)


    def build_next_candidates(self):
        for ws in self.words.values():
            for w in ws:
                w.next_num = len(self.words[w.tail]) if self.words.get(w.tail) else 0

    def deep_search(self, input_word:str):
        if not re.match(self.check_Chinese_regex, input_word):
            return 0, None
        input_word = Word(input_word)
        if input_word.tail not in self.words:
            return 1, None
        candidates = self.words[input_word.tail]
        weights = [w.next_num+1 for w in candidates]
        word = random.choices(candidates, weights)[0]
        return 2, word.word




if __name__ == '__main__':
    pass