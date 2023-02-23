import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('GUI') # 프로그램 제목 지정
root.geometry('640x480') # GUI크기 # 가로 * 세로 + x좌표 + y좌표

values =[str(i) + "일" for i in range(1, 32)] # 1~31까지 숫자
combobox = ttk.Combobox(root,height=5, values=values)
combobox.pack()
combobox.set("A")# 최초 목록 제목 설정

readonlycombobox = ttk.Combobox(root,height=10, values=values, state="readonly") # 읽기 전용
readonlycombobox.current(0)# 0번째 인덱스 값 선택
readonlycombobox.pack()


def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonlycombobox.get())

btn = Button(root, text="선택", command=btncmd) # root(위젯), 어떤 글자를, 어떤 동작을
btn.pack()


root.mainloop() # 창이 닫히지 않도록