import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('GUI') # 프로그램 제목 지정
root.geometry('640x480') # GUI크기 # 가로 * 세로 + x좌표 + y좌표


# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # 언제끝날지 모른다 : indeterminate
# progressbar.start(10) # 10 ms마다 움직임
# progressbar.pack()






# def btncmd():
#     progressbar.stop()# 작동 중지

# btn = Button(root, text="선택", command=btncmd) # root(위젯), 어떤 글자를, 어떤 동작을
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101): # 1~100
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # progress bar의 값 설정
        progressbar2.update() # for문 동작때 마다 GUI업데이트
        print(p_var2.get())



btn = Button(root, text="시작", command=btncmd2) # root(위젯), 어떤 글자를, 어떤 동작을
btn.pack()








root.mainloop() # 창이 닫히지 않도록