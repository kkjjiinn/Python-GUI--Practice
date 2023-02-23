import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('GUI') # 프로그램 제목 지정
root.geometry('640x480') # GUI크기 # 가로 * 세로 + x좌표 + y좌표

# 위 제목
Label(root, text="메뉴 선택").pack(side="top")
# 아래 버튼
Button(root, text="주문하기").pack(side="bottom")

# 버거 프레임
frame_burger = Frame(root, relief="solid", bd=1)# 테두리 외곽선 표시
frame_burger.pack(side="left",fill="both",expand=True) # 왼쪽, 꽉채우기, 중간까지 늘리기
Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="게살버거").pack()


# 음료 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both",expand=True) # 오른쪽, 꽉채우기, 중간까지 늘리기
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()



root.mainloop() # 창이 닫히지 않도록