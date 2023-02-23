from tkinter import *

root = Tk()
root.title('GUI') # 프로그램 제목 지정

btn1 = Button(root, text="버튼1") # GUI안에 '버튼1'을가진 버튼 추가
btn1.pack() # 버튼 실행

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

# padx : 버튼 크기 크게, pady : 높낮이 조절 글자 수에 따라 조절 가능한 여백
# width,height : 너비, 높이 고정되어있음 


btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="gui_basic/적 캐릭터.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("버튼 클릭")
btn7 = Button(root, text="동작", command=btncmd )
btn7.pack()

root.mainloop() # 창이 닫히지 않도록