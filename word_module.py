'''
this is init program for loading from Chengyu.txt
'''
import csv, time
import re, random

Chinese_limit = r'([\u4e00-\u9fa5]){4}' #make sure user's input is Chinese words


def check_exist(word, word_database):
    for lines in word_database.values():
        for line in lines:
            if word == line[0]:
                return True
    return False


def write_back(word_database): #running when the program exits
    #update the data
    file = open('demo/simplified.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(file)
    for lines in word_database.values():
        for line in lines:
            writer.writerow(line)
    file.close()


def load_common_words(word_database):
    with open('demo/simplified.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for line in reader:
            if reader.line_num != 1:
                if line[1] not in word_database:
                    word_database[line[1]] = []
                word_database[line[1]].append(line)
    print('init successfully')


def deep_search(word_database, answers): #get optimal answer from answers list
    next_list_count = []
    for answer in answers:
        # print(answers)
        word_end = answer[2]
        nexts = word_database.get(word_end)
        temp_count = len(nexts) if nexts != None else 0
        next_list_count.append(temp_count)
    all = sum(next_list_count)
    select = random.randint(0, all-1)
    for index, item in enumerate(next_list_count):
        select -= item
        if select < 0:
            return answers[index], index


def get_answer(word_database, input_word):
    check = re.match(Chinese_limit, input_word)
    if check and check[0] == input_word:
        if not check_exist(input_word, word_database):
            with open('demo/simplified.csv', 'a+', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                word = input_word
                head = word[0]
                end = word[-1]
                frequency = 0
                now = time.strftime('%Y-%m-%d', time.localtime())
                row = [word, head, end, frequency, now]
                writer.writerow(row)
        answers = word_database.get(input_word[-1])
        if answers:
            optimal = deep_search(word_database, answers)
            optimal_pos = optimal[1]
            temp_frequency = int(word_database.get(input_word[-1])[optimal_pos][-2])
            temp_frequency += 1
            word_database.get(input_word[-1])[optimal_pos][-2] = temp_frequency#increment frequency
            return optimal[0]
        else:
            return None # no appropriate answer in word_database, computer lose
    else:
        return 'only allow Chinese word'


# unit test
# database = {}
# load_common_words(database)
# write_back(database)
