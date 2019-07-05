import tkinter as tk
from tkinter.messagebox import askyesno
import word_module

window = tk.Tk()
var_answer = tk.StringVar()
var_count = tk.IntVar()
counts = 0
database = {}
user_next_head = None

def lose():
    global database
    global user_next_head
    global counts
    # word_module.write_back(database)
    counts = 0
    user_next_head = None
    var_answer.set('You Lose !')
    var_count.set(counts)


def close_windows():
    global database
    ans = askyesno(title='Warning', message='Close this game ?')
    if ans:
        word_module.write_back(database)
        window.destroy()
    else:
        return

def show_answer():
    global user_next_head
    global counts
    global database
    input = e.get()
    if input == '':
        var_answer.set('please obey the rule')
        return
    if input[0] != user_next_head and user_next_head != None:
        var_answer.set('please obey the rule')
        return
    answer = word_module.get_answer(database, input)
    if answer:
        if answer == 'only allow Chinese word':
            var_answer.set(answer)
        else:
            counts += 1
            user_next_head = answer[2]
            var_answer.set(answer[0])
            var_count.set(counts)
    else:
        counts = 0
        user_next_head = None
        var_answer.set('You Win !')
        var_count.set(counts)



window.title('Github @Raibows')
window.geometry('500x320')
l = tk.Label(window, textvariable=var_answer, bg='green', font=('Arial', 18),
             width=20, height=2)
count = tk.Label(window, textvariable=var_count, bg='red', font=('Arial', 24),
                 width=4, height=2)
b = tk.Button(window, text='submit', width=15, height=2, command=show_answer)
lose = tk.Button(window, text='I\'m fucked', width=15, height=2, command=lose)
e = tk.Entry(window)



def init_window():
    global database
    word_module.load_common_words(database)
    l.pack()
    count.pack()
    e.pack()
    b.pack()
    lose.pack()
    window.protocol('WM_DELETE_WINDOW', close_windows)
    window.mainloop()