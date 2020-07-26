import tkinter as tk
from tkinter import messagebox
from word import WordBase

class MainPanel():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GitHub Raibows©")
        self.root.geometry("500x380+550+300")
        self.root.resizable(0, 0)

        self.main_frame = tk.Frame(self.root, width=500, height=200)
        self.main_frame.place(x=0, y=0)

        self.answer = tk.Label(self.main_frame, font=('仿宋', 20), bg='#CCFFFF')
        self.answer.place(x=0, y=0, width=500, height=87)

        self.tip = tk.Label(self.main_frame,  text='接龙次数', font=('仿宋', 20), bg='#FF6633')
        self.tip.place(x=0, y=87, width=120, height=87)

        self.score = tk.Label(self.main_frame, font=('仿宋', 20), bg='#FFFF99', text='0')
        self.score.place(x=120, y=87, width=380, height=87)


        self.input = tk.Text(self.root, font=('仿宋', 24), bg='white', width=10, height=1)
        self.input.place(x=160, y=87*2)

        self.button_frame = tk.Frame(self.root, width=300, height=80)
        self.button_frame.place(x=100, y=280)
        self.submit = tk.Button(self.button_frame, font=('仿宋', 20),
                                bg='#66FF33', text='提交', command=self.submit_event)
        self.submit.grid(row=0, column=0)
        self.tip = tk.Button(self.button_frame, font=('仿宋', 20),
                                bg='yellow', text='提示', command=self.tip_event)
        self.tip.grid(row=0, column=1)
        self.restart = tk.Button(self.button_frame, font=('仿宋', 20),
                             bg='white', text='重新开始', command=self.restart_event)
        self.restart.grid(row=0, column=2)

        self.backend = WordBase()
        self.score_int = 0
        self.now_word = None
        self.tip_num = 3



    def submit_event(self):
        input = self.input.get('1.0', tk.END).strip('\n').strip(' ')
        self.input.delete('1.0', tk.END)
        if self.now_word and self.now_word[-1] != input[0]:
            messagebox.showerror(message=f"请遵守游戏规则，用{self.now_word[-1]}开头接龙", parent=self.root)
            return None
        st, ans = self.backend.deep_search(input)
        if st == 0:
            messagebox.showerror(message="请输入4字中文成语", parent=self.root)
        elif st == 1:
            messagebox.showinfo(message="恭喜你赢了", parent=self.root)
            self.restart_event()
        elif st == 2:
            self.score_int += 1
            self.now_word = ans
            self.score.config(text=f'{self.score_int}')
            self.answer.config(text=self.now_word)
        return None


    def restart_event(self):
        self.now_word = None
        self.score_int = 0
        self.tip_num = 3
        self.score.config(text=f'{self.score_int}')
        self.answer.config(text='')

    def tip_event(self):
        if self.now_word == None: return None
        if self.tip_num == 0:
            messagebox.showerror(message="提示次数已用光啦", parent=self.root)
        else:
            self.tip_num -= 1
            st, ans = self.backend.deep_search(self.now_word)
            if st == 2:
                messagebox.showinfo(message=f"请试试 {ans}", parent=self.root)
                self.input.insert('1.0', ans)
            else:
                messagebox.showerror(message="该答案我也无能为力！已帮您重启游戏", parent=self.root)
                self.restart_event()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    gui = MainPanel()
    gui.run()