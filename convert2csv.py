import csv
import time

'''
covert .txt to csv format
'''


file = open('chengyu.txt', 'r', encoding='utf-8')
afile = open('demo/simplified.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(afile)
writer.writerow(['Word', 'Head', 'End', 'Frequency', 'AppendTime'])
flag = 0
for line in file:
    if flag % 2 == 0:
        word = line[1:5]
        head = word[0]
        end = word[-1]
        frequency = 0
        now = time.strftime('%Y-%m-%d', time.localtime())
        row = [word, head, end, frequency, now]
        writer.writerow(row)
    flag += 1

file.close()
afile.close()
