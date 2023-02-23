from tkinter import *

root = Tk()
root.title('GUI') # 프로그램 제목 지정
root.geometry('640x480') # GUI크기 # 가로 * 세로 + x좌표 + y좌표


frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill='both')


listbox = Listbox(frame, selectmode="extended", height=10,yscrollcommand=scrollbar.set)
# ,yscrollcommand=scrollbar.set : 스크롤을 멈춘자리에 머무르게

for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # 스크롤바와 리스트 박스를 매핑








root.mainloop() # 창이 닫히지 않도록