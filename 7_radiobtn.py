from tkinter import *

root = Tk()
root.title('GUI') # 프로그램 제목 지정
root.geometry('640x480') # GUI크기 # 가로 * 세로 + x좌표 + y좌표

Label(root, text="메뉴 선택").pack()

burger_var = IntVar() #value값을 int(정수로 반환)
btn_burger1 = Radiobutton(root, text="A햄버거", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="B햄버거", value=2, variable=burger_var)
btn_burger3= Radiobutton(root, text="C햄버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료 선택").pack()
drink_var = StringVar()#value값을 str(문자열)로 반환
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select() # 기본값 선택
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="환타", value="", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get())# 햄버거 중 선택된 라디오 항목의 값 (value)를 출력
    print(drink_var.get())# 음료 중 선택된 라디오 항목의 값(value)를 출력

btn = Button(root, text="주문", command=btncmd) # root(위젯), 어떤 글자를, 어떤 동작을
btn.pack()


root.mainloop() # 창이 닫히지 않도록