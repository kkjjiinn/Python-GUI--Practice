from tkinter import *

root = Tk()
root.title('GUI') # 프로그램 제목 지정
root.geometry('640x480')

label1 = Label(root, text="안녕")
label1.pack()

photo = PhotoImage(file="gui_basic/적 캐릭터.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나")
    
    global photo2
    photo2 = PhotoImage(file="gui_basic/캐릭터.png")
    label2.config(text="투모로우")


btn = Button(root, text="클릭", command=change)
btn.pack()
root.mainloop() # 창이 닫히지 않도록