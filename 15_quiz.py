import os
from tkinter import *

root = Tk()
root.title('제목 없음 = Windows 메모장') # 프로그램 제목 지정
root.geometry('640x480') # GUI크기 # 가로 * 세로 + x좌표 + y좌표

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): # 파일 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력


def save_file():
    with open(filename, "w",encoding="utf8" ) as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장



menu = Menu(root) #메뉴바를 화면에 나타나게 (화면에 보이진 않음)

# 파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command = save_file)
menu_file.add_separator() # 구역 나누기
menu_file.add_command(label="끝내기", command=root.quit)

menu.add_cascade(label="파일", menu=menu_file) # 메뉴바

# 편집 메뉴(빈 값)
menu.add_cascade(label="편집")

# 서식 메뉴 추가 (radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="서식", menu=menu_lang)

# 보기 메뉴
menu.add_cascade(label="보기")

#도움말

menu.add_cascade(label="도움말")


# 스크롤바

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")


# 메모장 쓰기
txt = Text(root,yscrollcommand=scrollbar.set) # 텍스트 위젯 만드는것
txt.pack(fill="both", expand=True) # 텍스트를 GUI크기 맞게 확장
scrollbar.config(command=txt.yview) # 스크롤바와 txt를 매핑














root.config(menu=menu) # 이게 있어야 메뉴바가 나옴
root.mainloop() # 창이 닫히지 않도록