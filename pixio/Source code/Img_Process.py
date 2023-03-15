from ast import Name
from time import sleep
import PIL.Image
from PIL import ImageTk, ImageEnhance
from PIL import *
from pytesseract import pytesseract
from tkinter.font import BOLD
import requests
import time
import cv2 as cv
import os
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
import subprocess
import datetime
import webbrowser

def config_f2():
    global count
    if not count > len(f2_frames)-2:

        for frame in f2_frames:
            frame.pack_forget()

        count+=1
        frame=f2_frames[count]
        frame.pack()
        
def config_reverse():
    global count
    if not count==0:

        for frame in f2_frames:
            frame.pack_forget()

        count-=1
        frame=f2_frames[count]
        frame.pack()
    
#Functions<>
def tesserect():
    ask=messagebox.askyesno("Disclaimer","Make sure you have Tesserect engine installed at the following path\n'C:/Program Files/Tesseract-OCR/tesseract.exe'\n OR \n You can download it from 'Download' menu",icon="warning")
    if ask == 1:
     def time():
      x = datetime.datetime.now()
      return(x.strftime(f"%d %B %Y (%A)"))
     try:
      pytext=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
      pytesseract.tesseract_cmd=pytext
      image=cv.imread(f"C:\Sample\{lbx.get(ANCHOR)}.jpg")
      img=cv.cvtColor(image, cv.COLOR_BGR2RGB)
      text=pytesseract.image_to_string(img)
      file=open(f'C:\Sample\Image_to_Text\{lbx.get(ANCHOR)}.txt',"a")
      file.write(f"\n{time()} : \n\n{text[:-1]}\n")
      messagebox.showinfo("Sucess",f"The text file is saved as {lbx.get(ANCHOR)}\n   location : 'C:\Sample\Image_to_Text\{lbx.get(ANCHOR)}.txt'")
     except FileNotFoundError as e:
         print(e)
         print("ok")
    else :
        return
    
def down():
        webbrowser.open_new_tab(
            'https://github.com/UB-Mannheim/tesseract/wiki'
        )
def unsplash():
        webbrowser.open_new_tab(
            'https://unsplash.com/'
        )
def pexels():
        webbrowser.open_new_tab(
            'https://www.pexels.com/'
        )

def how():
        webbrowser.open_new_tab(
            'https://github.com/nirakar24/Pixio/blob/master/pixio/How%20it%20works/README.md'
        )

def ref():
    root.config(cursor="wait")
    root.update()
    time.sleep(0.5)
    root.config(cursor="")

def clr():
    lbx.delete(0,END)
    b5.config(image=up_img)

def delete():
    lbx.delete(ANCHOR)

def set_width():
    image=cv.imread(f"C:\Sample\{lbx.get(ANCHOR)}.jpg")
    dim=image.shape
    w=dim[1]
    wid_th.delete(0,END)
    wid_th.insert(0,w)

    return

def set_height():
    image=cv.imread(f"C:\Sample\{lbx.get(ANCHOR)}.jpg")
    dim=image.shape
    h=dim[0]
    heig_ht.delete(0,END)
    heig_ht.insert(0,h)

    return

def dimen():
    try:
     set_width()
     set_height()
     messagebox.showinfo("Dimensions",f"Width - {wid_th.get()}\tHeight - {heig_ht.get()}")
     return
    except AttributeError:
        messagebox.showerror("Error","Select the Image first")

def popup_menu(event):
    quick.tk_popup(event.x_root,event.y_root)

def resize(width,height):
    try:
      image=cv.imread(f"C:\Sample\{lbx.get(ANCHOR)}.jpg")
      width=int(wid_th.get())
      height=int(heig_ht.get())
      dim=(width,height)
      img=cv.resize(image,dim,interpolation=cv.INTER_AREA)
  
      cv.imshow("Resized image",img)
      key=cv.waitKey(0)
  
      if key==ord("s"):
           cv.imwrite(f"C:/Sample/{lbx.get(ANCHOR)}|.jpg",img)
    except ValueError:
        messagebox.showerror("Error",'Enter a "Integer Value"')
        wid_th.delete(0,END)
        heig_ht.delete(0,END)

def resize2(percent):
    try:
     image=cv.imread(f"C:\Sample\{lbx.get(ANCHOR)}.jpg")
     percent=int(per_cent.get())
     dim=image.shape
     w=int(dim[1])
     h=int(dim[0])
     wid=int(w*(percent/100))
     heit=int(h*(percent/100))
     dimen=(wid,heit)
     img=cv.resize(image,dimen,interpolation=cv.INTER_AREA)
     
     cv.imshow("Resized image",img)
     key=cv.waitKey(0)
 
     if key==ord("s"):
        cv.imwrite(f"C:/Sample/{lbx.get(ANCHOR)}|.jpg",img)

         

    except ValueError:
        messagebox.showerror("Error",'Enter a "Integer Value"')
        per_cent.delete(0,END)

def close():
    ask=messagebox.askyesno("Exit","Are you sure",icon="warning")
    if ask==1:
        root.destroy()
    else:
        return

def rm_bg():
    global response
    ask=messagebox.askyesno("Disclaimer","Are you connected to Internet?",icon="warning")
    if ask==1:
     try:
      root.config(cursor="wait")
      root.update()
      response = requests.post(
      'https://api.remove.bg/v1.0/removebg',
      files={'image_file': open(f"C:/Sample/{lbx.get(ANCHOR)}.jpg", 'rb')},
      data={'size': 'auto'},
      headers={'X-Api-Key': '3ak36v4yU49c5nHbWtrzkk7K'},
      )
      
      print(response.status_code)
      
      if response.status_code == requests.codes.ok:
          with open(f'C:\Sample\output\{lbx.get(ANCHOR)}.png', 'wb') as out:
              out.write(response.content)

      root.config(cursor="") 
      ask=messagebox.askyesno("Sucess","file is saved at this location\n'C:/Sample/Output/\n\nDo you want to see results?")
      if ask==1:
        path=f"C:/Sample/Output/{lbx.get(ANCHOR)}.png"
        if os.name=="nt":
            os.startfile(path)
      else:
        return

     except requests.exceptions.ConnectionError:
        try:
         response.close()
        except NameError:
            messagebox.showerror("Error","No Internet")
            root.config(cursor="")    
    else:
     return
    

def add_img():
    images = filedialog.askopenfilenames(initialdir="C:/Sample/",title="Select the image",filetypes=(("jpg files", "*.jpg"),))
    
    for img in images:
        img=img.replace("C:/Sample/","")
        img=img.replace(".JPG","")
        img=img.replace(".jpg","")
        lbx.insert(END,img)

def save():
    global pic
    savefile = filedialog.asksaveasfile(defaultextension=".jpg")
    outputImage.save(savefile)

def show():
    global pic
    pic=PIL.Image.open(f"C:\Sample\{lbx.get(ANCHOR)}.jpg")
    # pic=pic.resize((200,100))
    displayimage(pic)
    # cv.imshow("Picture",pic)

def show2(event):
    pic=PIL.Image.open(f"C:\Sample\{lbx.get(ANCHOR)}.jpg")
    # pic=pic.resize((200,100))
    displayimage(pic)

def aspect(img,new_height):
    wid,heit=img.size
    ratio=wid/heit
    new_width=int(ratio*new_height)
    resized_img = img.resize((new_width,new_height))
    return resized_img

def displayimage(img):
    img_dis= aspect(img,int(f4.winfo_height()))
    img_dis = ImageTk.PhotoImage(img_dis)
    b5.config(image=img_dis)
    b5.image = img_dis

def flipped(n):
    img=cv.imread(f"C:/Sample/{lbx.get(ANCHOR)}.jpg")
    img = cv.flip(img, n)     
    # cv.imshow("Flipped right",img)
    # cv.waitKey(0)
# Save the image to a temporary file
    cv.imwrite('temp.jpg', img)
    # img=cv.imshow("Flipped",img)
    if os.name == 'nt':  # Check if the OS is Windows
        subprocess.Popen(['explorer', 'temp.jpg'])

def brightness_callback(brightness_pos):
    brightness_pos = float(brightness_pos)
    #print(brightness_pos)
    global outputImage
    enhancer = ImageEnhance.Brightness(pic)
    outputImage = enhancer.enhance(brightness_pos)
    displayimage(outputImage)

def contrast(contra_pos):
    contra_pos = float(contra_pos)
    #print(contrast_pos)
    global outputImage
    enhancer = ImageEnhance.Contrast(pic)
    outputImage = enhancer.enhance(contra_pos)
    displayimage(outputImage)

def sharp(sharp_pos):
    sharp_pos = float(sharp_pos)
    #print(sharpness_pos)
    global outputImage
    enhancer = ImageEnhance.Sharpness(pic)
    outputImage = enhancer.enhance(sharp_pos)
    displayimage(outputImage)

def art():
    img=cv.imread(f"C:/Sample/{lbx.get(ANCHOR)}.jpg")
    img_resized=cv.resize(img,None,fx=1,fy=1)

    for i in range(3):
        img_clear=cv.medianBlur(img_resized,3)

    img_clear=cv.edgePreservingFilter(img_clear, sigma_s=5)

    img_filter=cv.bilateralFilter(img_clear,3,10,5)

    for i in range(2):
        img_filter=cv.bilateralFilter(img_filter,3,20,10)

    for i in range(3):
        img_filter=cv.bilateralFilter(img_filter,5,30,10)

    mask = cv.GaussianBlur(img_filter, (7,7), 2)
    img_sharp = cv.addWeighted(img_filter,1.5,mask,-0.5,0)
    img_sharp = cv.addWeighted(img_filter,1.4,mask,-0.2,10)

    cv.imwrite(f'C:\\Sample\\temp\\{lbx.get(ANCHOR)}.png',img_sharp)
    temp=f'C:\\Sample\\temp\\{lbx.get(ANCHOR)}.png'
    if os.name=="nt":
            os.startfile(temp)

#funtions</>

# colors
win="#F8F8F8"
ls="#D8D9F2"

#main window<>
root=Tk()

n=140
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
# root.maxsize(screen_width,screen_height)
# root.minsize(screen_width,screen_height)
root.title("Pixio")
root.iconbitmap("components\\editor.ico")
root.configure(bg=win)

#define images
original=PhotoImage(file="components\\original.png")
up_img=PhotoImage(file="components\\Upload.png")
res_ize=PhotoImage(file="components\\resize (W x H).png")
res_ize2=PhotoImage(file="components\\resize(%).png")
img_to_txt=PhotoImage(file="components\\image_to_text.png")
rem_bg=PhotoImage(file="components\\rm_bg.png")
dimen_sion=PhotoImage(file="components\\Dimensions.png")

#listbox
lbx=Listbox(root,border=7,width=int(screen_width//50),bg=ls,relief=FLAT,font=(BOLD,18),selectbackground="white",selectforeground="black",foreground="black") 
lbx.pack(side=RIGHT,fill=Y)

#Frames
f1=Frame(root,bg=win,height=20)
f1.pack(side=TOP,fill=X)
f3=Frame(root,bg=win,height=20)
f3.pack(side=BOTTOM,fill=BOTH)
f2_main=Frame(root,bg=win,height=45)
f2_main.pack(side=BOTTOM,fill=X,expand=True)
f2=Frame(f2_main,bg=win,height=45)
f2.pack(fill=X,expand=True)
f2_slider=Frame(f2_main,bg=win,height=45)
# f2_slider.pack(fill=X)
f4=Frame(root,bg=win,height=700)
f4.pack(fill=BOTH)
f4.pack_propagate(False)

# MULTIPLE frames
f2_frames=[f2,f2_slider]
count=0

#labels
l1=Label(f2,text="X",font=(16),bg=win)
l1.grid(row=3,column=1)


#Entry Widget
width=IntVar
height=IntVar
percent=IntVar

wid_th=Entry(f2,textvariable=width,width=5,bg=ls)
wid_th.grid(row=3,column=0,pady=5,padx=15)
heig_ht=Entry(f2,textvariable=height,width=5,bg=ls)
heig_ht.grid(row=3,column=2,pady=5,padx=13)
per_cent=Entry(f2,textvariable=percent,width=5,bg=ls)
per_cent.grid(row=3,column=3,padx=25,pady=10)

#sliders
brightnessSlider = Scale(f2_slider, label="Brightness", from_=0, to=10, orient=HORIZONTAL, length=250, troughcolor=ls,
                         resolution=0.1, command=brightness_callback, bg=win,sliderrelief=FLAT)
brightnessSlider.set(1)
brightnessSlider.configure(font=('consolas',10,'bold'),foreground='black')
# brightnessSlider.place(x=1070,y=15)
brightnessSlider.grid(row=0,column=0, padx=20,pady=50)
contrastSlider = Scale(f2_slider, label="Contrast", from_=0, to=10, orient=HORIZONTAL, length=250, troughcolor=ls,
                               command=contrast, resolution=0.1, bg=win,sliderrelief=FLAT,foreground="red")
contrastSlider.set(1)
contrastSlider.configure(font=('consolas',10,'bold'),foreground='black')
# contrastSlider.place(x=1070,y=90)
contrastSlider.grid(row=0,column=1, padx=20,pady=50)

sharpnessSlider = Scale(f2_slider, label="Sharpness", from_=0, to=10, orient=HORIZONTAL, length=250,troughcolor=ls,
                        command=sharp, resolution=0.1, bg=win, sliderrelief=FLAT)
sharpnessSlider.set(1)
sharpnessSlider.configure(font=('consolas',10,'bold'),foreground='black')
sharpnessSlider.grid(row=0,column=2, padx=20,pady=50)

#Buttons
b1=Button(f2,image=original,cursor="hand2",command=show,bg=win,border=0)
b1.grid(row=2,column=7,padx=15,pady=15)
b2=Button(f2,image=img_to_txt,cursor="hand2",command=tesserect,bg=win,border=0)
b2.grid(row=2,column=4,padx=25,pady=10)
b3=Button(f2,image=res_ize,cursor="hand2",command=lambda:resize(wid_th.get(),heig_ht.get()),bg=win,border=0)
b3.grid(row=2,column=0,pady=10,columnspan=3)
b4=Button(f2,image=rem_bg,cursor="hand2",command=rm_bg,bg=win,border=0)
b4.grid(row=2,column=5,padx=25,pady=10)
b5=Button(f4,image=up_img,cursor="hand2",command=add_img,borderwidth=0,bg=win,activebackground=win)
b5.pack()
b6=Button(f2,image=res_ize2,cursor="hand2",command=lambda:resize2(per_cent.get()),bg=win,border=0)
b6.grid(row=2,column=3,padx=20)
b7=Button(f2,image=dimen_sion,cursor="hand2",command=dimen,bg=win,border=0)
b7.grid(row=2,column=6,padx=25,pady=10)

#menubar
menubar=Menu(root,tearoff=0)
file=Menu(menubar,tearoff=0)
tools=Menu(menubar,tearoff=0)
resze=Menu(tools,tearoff=0)
color=Menu(menubar,tearoff=0)
download=Menu(menubar,tearoff=0)
How_it_works = Menu(menubar,tearoff=0)
images=Menu(download,tearoff=0)


menubar.add_cascade(label="File",menu=file)
menubar.add_cascade(label="Tools",menu=tools)
menubar.add_cascade(label="Color space",menu=color)
# menubar.add_cascade(label="More Images",menu=adjust)
menubar.add_cascade(label="Download",menu=download)
menubar.add_cascade(label="More",menu=How_it_works)

images.add_command(label="Unsplash",command=unsplash)
images.add_command(label="Pexels",command=pexels)
# adjust.add_command(label="new",command=lambda:config_f2(f2))

file.add_command(label="Add images",command=add_img)
file.add_command(label="Home",command=config_reverse)
file.add_command(label="Save",command=save)
file.add_command(label="Delete",command=delete)
file.add_command(label="Clear list",command=clr)
file.add_command(label="Refesh",command=ref)

resze.add_command(label="by W x H",command=lambda:resize(wid_th.get(),heig_ht.get()))
resze.add_command(label="by %",command=lambda:resize2(per_cent.get()))

tools.add_cascade(label="Resize",menu=resze)
tools.add_command(label="Sliders",command=config_f2)
tools.add_command(label="Remove Background",command=rm_bg)
tools.add_command(label="Image to text",command=tesserect)
tools.add_command(label="Dimensions",command=dimen)
tools.add_command(label="Water art",command=art)
tools.add_command(label="Rotate 360",command=lambda:flipped(0))
tools.add_command(label="Rotate 180",command=lambda:flipped(1))
tools.add_command(label="Rotate 270",command=lambda:flipped(-1))


download.add_command(label="Tesserect engine",command=down)
download.add_cascade(label="More Images",menu=images)

How_it_works.add_command(label="How it works?",command=how)

#quick_access menu
quick=Menu(root,tearoff=0)
quick.add_command(label="Remove Background",command=rm_bg)
quick.add_command(label="Dimensions",command=dimen)
quick.add_command(label="Image to Text",command=tesserect)
quick.add_separator()         
quick.add_command(label="Refresh",command=ref)
quick.add_command(label="Delete",command=delete)
quick.add_command(label="Clear list",command=clr)
quick.add_command(label="Save",command=save)
quick.add_separator()
quick.add_command(label="Exit",command=close)

root.config(menu=menubar)
root.bind("<Button-3>",popup_menu)
root.bind("<Return>",show2)

root.mainloop()
#main window</>