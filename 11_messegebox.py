import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('GUI') # 프로그램 제목 지정
root.geometry('640x480') # GUI크기 # 가로 * 세로 + x좌표 + y좌표


def info():
    msgbox.showinfo("알림","정상입니다.")


def warn():
    msgbox.showwarning("경고","차단되었습니다.")


def error():
    msgbox.showerror("XX","에러입니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "OK or NO")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "다시 again?")

def yesno():
    msgbox.askyesno("예 / 아니오", "그래도 하겠습니까?") 

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="저장 안되었습니다. \n 그래도 종료할까요?")    
    # 네 : 저장 후 종료
    # 아니오 : 저장하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print("응답:", response) # True, False, None -> 1, 아니오 0, 그 외
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")   
    
    
    
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()













root.mainloop() # 창이 닫히지 않도록