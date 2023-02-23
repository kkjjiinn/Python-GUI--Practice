from tkinter import *

root = Tk()
root.title('GUI') # 프로그램 제목 지정
root.geometry('640x480') # GUI크기 # 가로 * 세로 + x좌표 + y좌표


chkvar = IntVar() # chkvar에 int형으로 값을 저장
checkbox = Checkbutton(root, text="안보기", variable=chkvar)
# checkbox.select() # 자동 선택 처리
# checkbox.deselect() # 선택 해제 처리
checkbox.pack()

chkvar2 = IntVar()
checkbox2 = Checkbutton(root, text="일주일동안 안봄", variable=chkvar2)
checkbox2.pack()




def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd) # root(위젯), 어떤 글자를, 어떤 동작을
btn.pack()


root.mainloop() # 창이 닫히지 않도록