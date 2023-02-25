import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('GUI') # 프로그램 제목 지정

# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일 선택",filetypes=(("PNG 파일", "*.png"),("모든 파일", "*.*")),initialdir="c:/")# 최초에 C:/ 경로로 보여줌, 최초에 사용자가 지정한 경로보여줌

    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)


# 선택 추가
def del_file():
    print(list_file.curselection())

    for index in reversed(list_file.curselection()): # revesed : 원래 내용은 그대로 둔채 순서만 바꾼 뒤 함수에 넣어줌
        list_file.delete(index)

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == None: # 사용자가 취소 누를때
        return
    # print(folder_selected)
    txt_dest_path.delete(0, END) # 삭제를 0부터 끝까지
    txt_dest_path.insert(0, folder_selected)

# 시작
def start():
    #각 옵션들 값을 확인
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    #파일 목록 확인
    if list_file.size() == 0: # 파일이 0개 선택되었을때
        msgbox.showwarning("경고","이미지 파일 추가하세요") # 경고 문구
        return

    #저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요") # 경고 제목, 경고 내용
        return



# 파일 프레임 (파일 추가, 선택 삭제 버튼)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) # 가로로 펼쳐짐

btn_add_file = Button(file_frame, padx=5, pady=5, width=10, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=10, text="선택삭제",command=del_file)
btn_del_file.pack(side = "right")


# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y") # 위치 : 오른쪽, 사이즈 : 위아래로 꽉참

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview) # 리스트바와 스크롤바를 연동 y축으로


# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame) # Entry : (0,END)  text : (1.0, END)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경(안쪽 pad길이)

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)
#---------------------------------------------레이아웃 전--------------------------------------------

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

#1. 가로 넓이 옵션

# 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8) # 옵션 프레임 안에 넣겠다
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10) # state="readonly" 사용자가 임의로 변경하지 못하게 읽기전용
cmb_width.current(0) # 첫번째 자동 선택
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
#간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8) # 옵션 프레임 안에 넣겠다
lbl_space.pack(side="left", padx=5, pady=5)

#간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10) # state="readonly" 사용자가 임의로 변경하지 못하게 읽기전용
cmb_space.current(0) # 첫번째 자동 선택
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
# 파일 포맷 옵션 레이블
cmb_format = Label(frame_option, text="간격", width=8) # 옵션 프레임 안에 넣겠다
cmb_format.pack(side="left", padx=5, pady=5)

#파일 포맷 옵션 콤보

opt_format = ["PNG", "JPG", "BMP"]
opt_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10) # state="readonly" 사용자가 임의로 변경하지 못하게 읽기전용
opt_format.current(0) # 첫번째 자동 선택
opt_format.pack(side="left", padx=5, pady=5)


# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x")

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)


btn_close = Button(frame_run, padx=5, pady=5, text="정지", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)







root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop() # 창이 닫히지 않도록