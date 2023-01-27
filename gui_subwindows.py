from tkinter import *
from PIL import Image, ImageTk

CLOSE = False
OPEN = True
gui_D1_window_status = CLOSE

def resize_image(event, arg):
    (copy_of_image,label) = arg
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

#functions for Lagna chart gui window
def popup_window_D1(name,imagepath):
    global gui_D1_window_status
    global gui_D1
    if (gui_D1_window_status == CLOSE): #open new window if not active window of lagna
        gui_D1 = Toplevel()
        gui_D1.protocol("WM_DELETE_WINDOW", popup_window_D1_closed)
        gui_D1.title(f'Lagna chart of {name}.')
        gui_D1.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D1 = ImageTk.PhotoImage(image)
        label = Label(gui_D1, image = photo_D1)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D1_window_status = OPEN
    else:
        gui_D1.focus_force()    #Brings focus back to this window
        #gui_D1.bell()

def popup_window_D1_closed():
    global gui_D1_window_status
    gui_D1_window_status = CLOSE
    gui_D1.destroy()


if __name__ == "__main__":
    root = Tk()
    btn = Button(root, text="Open D1", command=lambda: popup_window_D1("Shyam Bhat", 'images/Lagna_chart.png'))
    btn.pack()
    root.mainloop()