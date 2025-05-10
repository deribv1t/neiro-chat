from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tempfile, base64, zlib
import subprocess
import os


ICON = zlib.decompress(base64.b64decode("eJxjYGAEQgEBBiDJwZDBysAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="))

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, "wb") as icon_file:
    icon_file.write(ICON)

root = Tk()
root.geometry("900x700")
root.config(bg='#072b3d')
root.resizable(False, False)
root.title("Select Chat")
root.iconbitmap(default=ICON_PATH)


def human():
    file_path = r"dist\global_human.exe"
    if os.path.exists(file_path):
        try:
            subprocess.Popen(file_path)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")
    else:
        messagebox.showerror("Ошибка", "Файл не найден!")
    
    root.destroy()

def neiro_gemma():
    file_path = r'dist\chat_Gemma\chat_Gemma.exe'
    if os.path.exists(file_path):
        try:
            subprocess.Popen(file_path)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")
    else:
        messagebox.showerror("Ошибка", "Файл не найден!")
    root.destroy()

def neiro_DeepSeek():
    file_path = r"dist\chat_DS\chat_DS.exe"
    if os.path.exists(file_path):
        try:
            subprocess.Popen(file_path)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")
    else:
        messagebox.showerror("Ошибка", "Файл не найден!")
    root.destroy()

def neiro_Qwen():
    file_path = r"dist\chat_Qwen\chat_Qwen.exe"
    if os.path.exists(file_path):
        try:
            subprocess.Popen(file_path)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")
    else:
        messagebox.showerror("Ошибка", "Файл не найден!")
    root.destroy()

style = ttk.Style()
style.theme_use("clam")

style.map(
    "TButton",
    background=[
        ("pressed", "#0f618a"),
        ("active", "#168cc7")
    ],
    relief=[
        ('pressed', 'solid'),
        ('active', 'sunken')
    ]
)

style.configure("TLabel",
                foreground="White",
                font=('Open Sans',24),
                background='#072b3d',
                padding=8,
                border=4,
                bordermode=OUTSIDE)

style.configure("TButton",
                background='#27a7e7',
                foreground="black",
                font=('Open Sans',16),
                border=4,
                activebackground='#59a3ed',
                relief='flat',
                bordermode=OUTSIDE)

style.configure("TFrame",
                background='#072b3d',
                border=5,
                relief='sunken',
                bordermode=OUTSIDE)


left_frame = ttk.Frame(root,style='TFrame')
right_frame = ttk.Frame(root,style='TFrame')

left_title_frame = ttk.Frame(left_frame,style='TFrame')
right_title_frame = ttk.Frame(right_frame,style='TFrame')

left_left_frame = ttk.Frame(left_frame,style='TFrame')
left_right_frame = ttk.Frame(left_frame,style='TFrame')

label = ttk.Label(root,text='Выберите chat')

left_label = ttk.Label(left_title_frame, text="Чат с ИИ",style='TLabel')
right_label = ttk.Label(right_title_frame, text="Чат с классом",style='TLabel')

left_left_label1 = ttk.Label(left_left_frame,text='gemma3-1B',style='TLabel')
left_left_label2 = ttk.Label(left_left_frame,text='DeepSeek-8B',style='TLabel')
left_left_label3 = ttk.Label(left_left_frame,text='Qwen2.5-Coder-3B',style='TLabel')

btn = ttk.Button(right_frame,style="TButton",text='Вступить', command=human)

btn1 = ttk.Button(left_right_frame,style="TButton",text='Запустить', command=neiro_gemma)
btn2 = ttk.Button(left_right_frame,style="TButton",text='Запустить', command=neiro_DeepSeek)
btn3 = ttk.Button(left_right_frame,style="TButton",text='Запустить', command=neiro_Qwen)

label.pack(padx=50,pady=30,anchor=CENTER)

left_frame.pack(side="left", fill="both", expand=True)
right_frame.pack(side="right", fill="both", expand=True)

left_title_frame.pack(fill="x")
right_title_frame.pack(fill="x")

left_left_frame.pack(side="left", fill="both", expand=True)
left_right_frame.pack(side="right", fill="both", expand=True)

left_label.pack(side=TOP,pady=4)
right_label.pack(side=TOP,pady=4)

left_left_label1.pack(padx=10,pady=15)
left_left_label2.pack(padx=10,pady=15)
left_left_label3.pack(padx=10,pady=15)

btn.pack(anchor=CENTER,fill=BOTH,expand=True)

btn1.pack(padx=10,pady=22,anchor=CENTER)
btn2.pack(padx=10,pady=25,anchor=CENTER)
btn3.pack(padx=10,pady=20,anchor=CENTER)

root.mainloop()
