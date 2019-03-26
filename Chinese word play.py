'''
this is a program that could append new idiom automatically
and play Chinese string up puzzle
'''
import random
import time

def calculate_time(func):
    def wrapper():
        x1 = time.clock()
        func()
        x2 = time.clock()
        print(x2-x1)
    return wrapper

fin=open('chengyu.txt','a+',encoding='utf-8')
ciku=dict()
def initialidiom():
    x=0
    fin.seek(0)
    for line in fin:
        if x%2==0:
            word=line[1:5]
            if word[0] not in ciku:
                ciku[word[0]]=[]
                ciku[word[0]].append(word)
            else:
                if word not in ciku[word[0]]:
                    ciku[word[0]].append(word)
        x+=1
    print('initial successfully!')
def getans(a):
    if a[-1] in ciku:
        length=len(ciku[a[-1]])
        search_time=0
        while(1):
            pos=random.randint(0,length-1)
            search_time+=1
            if (ciku[a[-1]][pos][0] in ciku) or search_time>=3:
                break
        return ciku[a[-1]][pos]
    else:
        return -1
def lookup(a):
    tag=0
    key=a[0]
    if key in ciku:
        if a not in ciku[key]:
            ciku[key].append(a)
            fin.write('\n\n '+a)
            tag=1
    else:
        ciku[a[0]]=[]
        ciku[a[0]].append(a)
        fin.write('\n\n '+a)
        tag=1
    if tag==1:
        #fin.close()
        print('append successfully')


def runidiom():
    initialidiom()
    time=0
    ciyu=input()
    lookup(ciyu)
    answer=getans(ciyu)
    while answer!=-1:
        print('{}  当前接龙次数{}'.format(answer,time+1))
        time+=1
        ciyu=input()
        '''
        while ciyu[0]!=answer[-1]:
            print('please obey the rule')
            ciyu=input()
        '''
        while answer[-1] not in ciyu:
            print('please obey the rule')
            ciyu=input()
        lookup(ciyu)
        answer=getans(ciyu)
    print('you win!')
    fin.close()


runidiom()

