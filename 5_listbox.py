from tkinter import *

root = Tk()
root.title('GUI') # 프로그램 제목 지정
root.geometry('640x480') # GUI크기 # 가로 * 세로 + x좌표 + y좌표

listbox = Listbox(root, selectmode="extended", height=0) # extended : 여러개 선택 가능, single : 한개만 선택가능
# height = 0 : 전체, height = 3 : 3개만 보여줌 
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "참외")

listbox.pack()



def btncmd():
    # 삭제
    listbox.delete(END) # 맨 뒤에 항목 삭제 0 : 맨 앞에 항목 삭제

    #갯수 확인
    print("리스트에는", listbox.size(), "개가 있어")

    #항목 확인 (시작 idx, 끝 idx)
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인 (위치로 반환 ex.1,2,3)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd) # root(위젯), 어떤 글자를, 어떤 동작을
btn.pack()


root.mainloop() # 창이 닫히지 않도록