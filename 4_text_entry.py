from tkinter import *

root = Tk()
root.title('GUI') # 프로그램 제목 지정
root.geometry('640x480') # GUI크기 # 가로 * 세로 + x좌표 + y좌표

txt = Text(root, width=30, height=5) # 텍스트 위젯 만드는것
txt.pack()
txt.insert(END,"글자 입력하쇼") # 텍스트 위젯에 글 넣기

e = Entry(root, width=30) # 한 줄짜리 텍스트 위젯 ex.id password
e.pack()
e.insert(0,"ㅇ")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop() # 창이 닫히지 않도록