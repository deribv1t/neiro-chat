from tkinter import *
from functools import partial
from tkinter import ttk
import socket
import threading
import tempfile, base64, zlib


def receive_messages(server_socket):
    """Поток для получения сообщений от сервера."""
    while True:
        try:
            messageServ = server_socket.recv(2048).decode().strip()
            if messageServ:
                message('sw',messageServ,'#2b5378')
        except ConnectionResetError:
            break

def send_messages(server_socket,message=None):
    """Основной поток для ввода и отправки сообщений."""
    hostname = socket.gethostname()
    localIp = socket.gethostbyname(hostname)
    message = localIp[-2:] + ': ' + message
    if message:
        server_socket.sendall((f"{message}\n").encode())

def main():
    global client_socket 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.0.116', 10000)#'192.168.0.116'
    client_socket.connect(server_address)

    recv_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    recv_thread.daemon = True
    recv_thread.start()

    # send_messages(client_socket)

def finish():
    client_socket.close()
    root.destroy()

# #954fa5  #6370f2
# (149, 79, 165), (99, 112, 242)
#rgb(43,83,120) - message serv

ICON = zlib.decompress(base64.b64decode("eJxjYGAEQgEBBiDJwZDBysAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="))

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, "wb") as icon_file:
    icon_file.write(ICON)


def update_scrollregion(event):
    bbox = canvas.bbox("all")
    canvas.configure(scrollregion=(bbox[0], bbox[1], bbox[2], bbox[3] + 120))
    canvas.itemconfig(canvas.find_withtag("all"), width=event.width)

def copy_text(label,event=None):
    root.clipboard_clear()
    root.clipboard_append(label["text"])
    root.update()

def show_menu(label,event):
    menu = Menu(root, tearoff=0)
    menu.add_command(label="Копировать", command=partial(copy_text,label))
    menu.post(event.x_root, event.y_root)
    

def message(pos,txt,background='#8f4bb0'):
    if txt == '' or txt ==' ':
     return
    
    # canvas.yview_moveto(1.0)
    if background == '#8f4bb0':
        frame = ttk.Frame(inner_frame)
        label = ttk.Label(frame,text=txt,background=background)
        
        label.configure(compound="center")
        label.bind("<Button-3>", partial(show_menu,label))

        frame.pack(fill=X,pady=8,anchor=pos)
        label.pack(side=BOTTOM,anchor=pos)

        send_messages(client_socket,txt)
    else:
        frame = ttk.Frame(inner_frame)
        label = ttk.Label(frame,text=txt,compound="center",background=background)
    
        label.bind("<Button-3>", partial(show_menu,label))

        frame.pack(fill=X,pady=8,anchor=pos)
        label.pack(side=BOTTOM,anchor=pos)

    entry.delete("1.0", "end")

def textEntry():
    txt = entry.get("1.0", "end-1c")
    return message('se',txt)

root = Tk()
root.geometry("900x700")
root.config(bg='#072b3d')
root.resizable(False, False)
root.title("Chat")
root.iconbitmap(default=ICON_PATH)
root.protocol("WM_DELETE_WINDOW", finish) 
style = ttk.Style()

style.configure("TLabel",foreground="white",font=('Open Sans',11),background='#8f4bb0',padding=8,border=0,wraplength=620)
style.configure("TFrame",background='#072b3d')
# style.configure("TButton",background='#000000',foreground="white",font=('Open Sans',13),border=4)

canvas = Canvas(root,bg='#072b3d',borderwidth=0, highlightthickness=0,width=900)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(fill="both",expand=True)

inner_frame = ttk.Frame(canvas)

canvas.create_window((0, 0), window=inner_frame, anchor="nw", width=canvas.winfo_width())

inner_frame.bind("<Configure>", update_scrollregion)
canvas.bind("<Configure>", update_scrollregion)

canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-e.delta/60), "units"))

btn = Button(root,text='Отправить', command=textEntry,background='#27a7e7',activebackground='#59a3ed',foreground="white",
             font=('Open Sans',14),border=3,relief=SUNKEN)
btn.pack(side=BOTTOM,padx=50,pady=10,anchor=SE)
btn.place(height=100,width=170,y=600,x=730)

entry = Text(
    root,
    font=('Open Sans',12),
    height=10,
    width=40,
    wrap="word",       
    padx=5,     
    pady=5,
    background='#17212B',
    foreground="white",
    insertbackground='white'
)
scrollbar = ttk.Scrollbar(root, command=entry.yview)
entry.pack(side=BOTTOM,padx=5)
entry.place(width=729,height=100,y=600,x=0)

main()
root.mainloop()
