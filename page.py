import tkinter as tk, threading
import imageio
from tkinter import filedialog
from PIL import Image, ImageTk
import os



global UploadAction
global file,video


def fnm():
    global filename
    filename = filedialog.askopenfilename()
    return filename

def UploadAction(event=None):
    fname=fnm()
    print(fname)

def stream(label):
     os.system(filename)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('SubLip - Lip Reading System')
    root.minsize(1080,1000)
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    subMenu = tk.Menu(menubar, tearoff=0)
    
    menubar.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="Upload", command=UploadAction)
    subMenu.add_command(label="Exit", command=root.destroy)


    c = tk.Canvas(root,bg="blue",height=1000,width=500)

    img=Image.open('images/bck.jpg')
    img2=img.resize((2000,1000),Image.ANTIALIAS)
    fil =ImageTk.PhotoImage(img2)
    background_label = tk.Label(root, image=fil)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    w=h=50
    
    leftframe=tk.Frame(root)
    leftframe.pack(padx=50,pady=50)
    img=Image.open('images/browse.png')
    img2=img.resize((w,h),Image.ANTIALIAS)
    upload =ImageTk.PhotoImage(img2)
    btn1=tk.Button(leftframe,image=upload,text="Browse Video",command=UploadAction)
    btn1.pack()

    def func():
        my_label = tk.Label(root)
        my_label.pack()
        thread = threading.Thread(target=stream, args=(my_label,))
        thread.daemon = 1
        thread.start()
        btn2.config(state="disabled")
    
    def openProgram():
        os.system("python evaluation\predict.py evaluation\models\overlapped-weights368.h5 " + filename)
    


    midframe=tk.Frame(root)
    midframe.pack(padx=50,pady=50)
    img=Image.open('images/play.png')
    img2=img.resize((w,h),Image.ANTIALIAS)
    play =ImageTk.PhotoImage(img2)
    btn2=tk.Button(midframe,image=play,text="Play Video",command=func)
    #btn2.grid(row=0,column=1)
    btn2.pack()


    rightframe=tk.Frame(root)
    rightframe.pack(padx=50,pady=50)
    img=Image.open('images/read.png')
    img2=img.resize((w,h),Image.ANTIALIAS)
    read =ImageTk.PhotoImage(img2)
    btn3=tk.Button(rightframe,image=read,text="Lip read",command=openProgram)
    #btn3.grid(row=0,column=2)
    btn3.pack()
    root.mainloop()
    c.pack()
