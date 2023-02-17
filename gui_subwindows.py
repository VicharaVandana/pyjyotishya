from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk 

import mod_astrodata as data
from tkinter import messagebox

import dashas

CLOSE = False
OPEN = True
#colours for planet sign placement
BG_EXHALTED = "lime"
BG_OWNSIGN = "cyan"
BG_FRIENDSIGN = "yellow"
BG_NEUTRALSIGN = "white"
BG_ENEMYSIGN = "orange"
BG_DEBILITATED = "grey"

gui_D1_window_status = CLOSE
gui_D9_window_status = CLOSE
gui_D10_window_status = CLOSE
gui_D2_window_status = CLOSE
gui_D3_window_status = CLOSE
gui_D4_window_status = CLOSE
gui_D7_window_status = CLOSE
gui_D12_window_status = CLOSE
gui_D16_window_status = CLOSE
gui_D20_window_status = CLOSE
gui_D24_window_status = CLOSE
gui_D27_window_status = CLOSE
gui_D30_window_status = CLOSE
gui_D40_window_status = CLOSE
gui_D45_window_status = CLOSE
gui_D60_window_status = CLOSE
gui_planetTable_window_status = CLOSE
gui_VimDasha_window_status = CLOSE

#generic functions
#Gets Background colour for planet based on sign placement
def get_bgClr(planetData):
    bgColor = "black"   #for invalid planetdata
    if(planetData["name"] == "Sun"):
        if(planetData["sign"] == "Aries"):  #Exhalted Sign
            bgColor = (BG_EXHALTED)
        elif(planetData["sign"] == "Libra"):  #Debilitated Sign
            bgColor = (BG_DEBILITATED)
        elif(planetData["name"] == planetData["dispositor"]):  #Own Sign
            bgColor = (BG_OWNSIGN)
        elif(planetData["dispositor"] in planetData["friends"]):  #Friend Sign
            bgColor = (BG_FRIENDSIGN)
        elif(planetData["dispositor"] in planetData["nuetral"]):  #Neutral Sign
            bgColor = (BG_NEUTRALSIGN)
        elif(planetData["dispositor"] in planetData["enemies"]):  #Enemy Sign
            bgColor = (BG_ENEMYSIGN)
        else:  #Shouldnt reach here
            bgColor = (BG_NEUTRALSIGN)
    if(planetData["name"] == "Moon"):
        if(planetData["sign"] == "Taurus"):  #Exhalted Sign
            bgColor = (BG_EXHALTED)
        elif(planetData["sign"] == "Scorpio"):  #Debilitated Sign
            bgColor = (BG_DEBILITATED)
        elif(planetData["name"] == planetData["dispositor"]):  #Own Sign
            bgColor = (BG_OWNSIGN)
        elif(planetData["dispositor"] in planetData["friends"]):  #Friend Sign
            bgColor = (BG_FRIENDSIGN)
        elif(planetData["dispositor"] in planetData["nuetral"]):  #Neutral Sign
            bgColor = (BG_NEUTRALSIGN)
        elif(planetData["dispositor"] in planetData["enemies"]):  #Enemy Sign
            bgColor = (BG_ENEMYSIGN)
        else:  #Shouldnt reach here
            bgColor = (BG_NEUTRALSIGN)
    if(planetData["name"] == "Mars"):
        if(planetData["sign"] == "Capricorn"):  #Exhalted Sign
            bgColor = (BG_EXHALTED)
        elif(planetData["sign"] == "Cancer"):  #Debilitated Sign
            bgColor = (BG_DEBILITATED)
        elif(planetData["name"] == planetData["dispositor"]):  #Own Sign
            bgColor = (BG_OWNSIGN)
        elif(planetData["dispositor"] in planetData["friends"]):  #Friend Sign
            bgColor = (BG_FRIENDSIGN)
        elif(planetData["dispositor"] in planetData["nuetral"]):  #Neutral Sign
            bgColor = (BG_NEUTRALSIGN)
        elif(planetData["dispositor"] in planetData["enemies"]):  #Enemy Sign
            bgColor = (BG_ENEMYSIGN)
        else:  #Shouldnt reach here
            bgColor = (BG_NEUTRALSIGN)
    if(planetData["name"] == "Mercury"):
        if(planetData["sign"] == "Virgo"):  #Exhalted Sign
            bgColor = (BG_EXHALTED)
        elif(planetData["sign"] == "Pisces"):  #Debilitated Sign
            bgColor = (BG_DEBILITATED)
        elif(planetData["name"] == planetData["dispositor"]):  #Own Sign
            bgColor = (BG_OWNSIGN)
        elif(planetData["dispositor"] in planetData["friends"]):  #Friend Sign
            bgColor = (BG_FRIENDSIGN)
        elif(planetData["dispositor"] in planetData["nuetral"]):  #Neutral Sign
            bgColor = (BG_NEUTRALSIGN)
        elif(planetData["dispositor"] in planetData["enemies"]):  #Enemy Sign
            bgColor = (BG_ENEMYSIGN)
        else:  #Shouldnt reach here
            bgColor = (BG_NEUTRALSIGN)
    if(planetData["name"] == "Jupiter"):
        if(planetData["sign"] == "Cancer"):  #Exhalted Sign
            bgColor = (BG_EXHALTED)
        elif(planetData["sign"] == "Capricorn"):  #Debilitated Sign
            bgColor = (BG_DEBILITATED)
        elif(planetData["name"] == planetData["dispositor"]):  #Own Sign
            bgColor = (BG_OWNSIGN)
        elif(planetData["dispositor"] in planetData["friends"]):  #Friend Sign
            bgColor = (BG_FRIENDSIGN)
        elif(planetData["dispositor"] in planetData["nuetral"]):  #Neutral Sign
            bgColor = (BG_NEUTRALSIGN)
        elif(planetData["dispositor"] in planetData["enemies"]):  #Enemy Sign
            bgColor = (BG_ENEMYSIGN)
        else:  #Shouldnt reach here
            bgColor = (BG_NEUTRALSIGN)
    if(planetData["name"] == "Venus"):
        if(planetData["sign"] == "Pisces"):  #Exhalted Sign
            bgColor = (BG_EXHALTED)
        elif(planetData["sign"] == "Virgo"):  #Debilitated Sign
            bgColor = (BG_DEBILITATED)
        elif(planetData["name"] == planetData["dispositor"]):  #Own Sign
            bgColor = (BG_OWNSIGN)
        elif(planetData["dispositor"] in planetData["friends"]):  #Friend Sign
            bgColor = (BG_FRIENDSIGN)
        elif(planetData["dispositor"] in planetData["nuetral"]):  #Neutral Sign
            bgColor = (BG_NEUTRALSIGN)
        elif(planetData["dispositor"] in planetData["enemies"]):  #Enemy Sign
            bgColor = (BG_ENEMYSIGN)
        else:  #Shouldnt reach here
            bgColor = (BG_NEUTRALSIGN)
    if(planetData["name"] == "Saturn"):
        if(planetData["sign"] == "Libra"):  #Exhalted Sign
            bgColor = (BG_EXHALTED)
        elif(planetData["sign"] == "Aries"):  #Debilitated Sign
            bgColor = (BG_DEBILITATED)
        elif(planetData["name"] == planetData["dispositor"]):  #Own Sign
            bgColor = (BG_OWNSIGN)
        elif(planetData["dispositor"] in planetData["friends"]):  #Friend Sign
            bgColor = (BG_FRIENDSIGN)
        elif(planetData["dispositor"] in planetData["nuetral"]):  #Neutral Sign
            bgColor = (BG_NEUTRALSIGN)
        elif(planetData["dispositor"] in planetData["enemies"]):  #Enemy Sign
            bgColor = (BG_ENEMYSIGN)
        else:  #Shouldnt reach here
            bgColor = (BG_NEUTRALSIGN)
    if(planetData["name"] == "Rahu"):
        if(planetData["sign"] == "Taurus"):  #Exhalted Sign
            bgColor = (BG_EXHALTED)
        elif(planetData["sign"] == "Scorpio"):  #Debilitated Sign
            bgColor = (BG_DEBILITATED)
        elif(planetData["name"] == planetData["dispositor"]):  #Own Sign
            bgColor = (BG_OWNSIGN)
        elif(planetData["dispositor"] in planetData["friends"]):  #Friend Sign
            bgColor = (BG_FRIENDSIGN)
        elif(planetData["dispositor"] in planetData["nuetral"]):  #Neutral Sign
            bgColor = (BG_NEUTRALSIGN)
        elif(planetData["dispositor"] in planetData["enemies"]):  #Enemy Sign
            bgColor = (BG_ENEMYSIGN)
        else:  #Shouldnt reach here
            bgColor = (BG_NEUTRALSIGN)
    if(planetData["name"] == "Ketu"):
        if(planetData["sign"] == "Scorpio"):  #Exhalted Sign
            bgColor = (BG_EXHALTED)
        elif(planetData["sign"] == "Taurus"):  #Debilitated Sign
            bgColor = (BG_DEBILITATED)
        elif(planetData["name"] == planetData["dispositor"]):  #Own Sign
            bgColor = (BG_OWNSIGN)
        elif(planetData["dispositor"] in planetData["friends"]):  #Friend Sign
            bgColor = (BG_FRIENDSIGN)
        elif(planetData["dispositor"] in planetData["nuetral"]):  #Neutral Sign
            bgColor = (BG_NEUTRALSIGN)
        elif(planetData["dispositor"] in planetData["enemies"]):  #Enemy Sign
            bgColor = (BG_ENEMYSIGN)
        else:  #Shouldnt reach here
            bgColor = (BG_NEUTRALSIGN)
    #print(f'The planet:{planetData["name"]} has colour:{bgColor}')
    return(bgColor)



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
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
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
    return

def popup_window_D1_closed():
    global gui_D1_window_status
    global gui_D1
    gui_D1_window_status = CLOSE
    gui_D1.destroy()
    return

#functions for Navamsa chart gui window
def popup_window_D9(name,imagepath):
    global gui_D9_window_status
    global gui_D9
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D9_window_status == CLOSE): #open new window if not active window of lagna
        gui_D9 = Toplevel()
        gui_D9.protocol("WM_DELETE_WINDOW", popup_window_D9_closed)
        gui_D9.title(f'Navamsa chart of {name}.')
        gui_D9.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D9 = ImageTk.PhotoImage(image)
        label = Label(gui_D9, image = photo_D9)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D9_window_status = OPEN
    else:
        gui_D9.focus_force()    #Brings focus back to this window
        #gui_D9.bell()
    return

def popup_window_D9_closed():
    global gui_D9_window_status
    global gui_D9
    gui_D9_window_status = CLOSE
    gui_D9.destroy()
    return

#functions for Dasamsa chart gui window
def popup_window_D10(name,imagepath):
    global gui_D10_window_status
    global gui_D10
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D10_window_status == CLOSE): #open new window if not active window of lagna
        gui_D10 = Toplevel()
        gui_D10.protocol("WM_DELETE_WINDOW", popup_window_D10_closed)
        gui_D10.title(f'Dasamsa chart of {name}.')
        gui_D10.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D10 = ImageTk.PhotoImage(image)
        label = Label(gui_D10, image = photo_D10)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D10_window_status = OPEN
    else:
        gui_D10.focus_force()    #Brings focus back to this window
        #gui_D10.bell()
    return

def popup_window_D10_closed():
    global gui_D10_window_status
    global gui_D10
    gui_D10_window_status = CLOSE
    gui_D10.destroy()
    return

#functions for Hora chart gui window
def popup_window_D2(name,imagepath):
    global gui_D2_window_status
    global gui_D2
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D2_window_status == CLOSE): #open new window if not active window of lagna
        gui_D2 = Toplevel()
        gui_D2.protocol("WM_DELETE_WINDOW", popup_window_D2_closed)
        gui_D2.title(f'Hora chart of {name}.')
        gui_D2.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D2 = ImageTk.PhotoImage(image)
        label = Label(gui_D2, image = photo_D2)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D2_window_status = OPEN
    else:
        gui_D2.focus_force()    #Brings focus back to this window
        #gui_D2.bell()
    return

def popup_window_D2_closed():
    global gui_D2_window_status
    global gui_D2
    gui_D2_window_status = CLOSE
    gui_D2.destroy()
    return

#functions for Drekkana chart gui window
def popup_window_D3(name,imagepath):
    global gui_D3_window_status
    global gui_D3
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D3_window_status == CLOSE): #open new window if not active window of lagna
        gui_D3 = Toplevel()
        gui_D3.protocol("WM_DELETE_WINDOW", popup_window_D3_closed)
        gui_D3.title(f'Drekkana chart of {name}.')
        gui_D3.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D3 = ImageTk.PhotoImage(image)
        label = Label(gui_D3, image = photo_D3)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D3_window_status = OPEN
    else:
        gui_D3.focus_force()    #Brings focus back to this window
        #gui_D3.bell()
    return

def popup_window_D3_closed():
    global gui_D3_window_status
    global gui_D3
    gui_D3_window_status = CLOSE
    gui_D3.destroy()
    return

#functions for Chaturtamsa chart gui window
def popup_window_D4(name,imagepath):
    global gui_D4_window_status
    global gui_D4
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D4_window_status == CLOSE): #open new window if not active window of lagna
        gui_D4 = Toplevel()
        gui_D4.protocol("WM_DELETE_WINDOW", popup_window_D4_closed)
        gui_D4.title(f'Chaturtamsa chart of {name}.')
        gui_D4.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D4 = ImageTk.PhotoImage(image)
        label = Label(gui_D4, image = photo_D4)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D4_window_status = OPEN
    else:
        gui_D4.focus_force()    #Brings focus back to this window
        #gui_D4.bell()
    return

def popup_window_D4_closed():
    global gui_D4_window_status
    global gui_D4
    gui_D4_window_status = CLOSE
    gui_D4.destroy()
    return

#functions for Saptamsa chart gui window
def popup_window_D7(name,imagepath):
    global gui_D7_window_status
    global gui_D7
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D7_window_status == CLOSE): #open new window if not active window of lagna
        gui_D7 = Toplevel()
        gui_D7.protocol("WM_DELETE_WINDOW", popup_window_D7_closed)
        gui_D7.title(f'Saptamsa chart of {name}.')
        gui_D7.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D7 = ImageTk.PhotoImage(image)
        label = Label(gui_D7, image = photo_D7)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D7_window_status = OPEN
    else:
        gui_D7.focus_force()    #Brings focus back to this window
        #gui_D7.bell()
    return

def popup_window_D7_closed():
    global gui_D7_window_status
    global gui_D7
    gui_D7_window_status = CLOSE
    gui_D7.destroy()
    return

#functions for Dwadasamsa chart gui window
def popup_window_D12(name,imagepath):
    global gui_D12_window_status
    global gui_D12
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D12_window_status == CLOSE): #open new window if not active window of lagna
        gui_D12 = Toplevel()
        gui_D12.protocol("WM_DELETE_WINDOW", popup_window_D12_closed)
        gui_D12.title(f'Dwadasamsa chart of {name}.')
        gui_D12.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D12 = ImageTk.PhotoImage(image)
        label = Label(gui_D12, image = photo_D12)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D12_window_status = OPEN
    else:
        gui_D12.focus_force()    #Brings focus back to this window
        #gui_D12.bell()
    return

def popup_window_D12_closed():
    global gui_D12_window_status
    global gui_D12
    gui_D12_window_status = CLOSE
    gui_D12.destroy()
    return

#functions for Shodasamsa chart gui window
def popup_window_D16(name,imagepath):
    global gui_D16_window_status
    global gui_D16
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D16_window_status == CLOSE): #open new window if not active window of lagna
        gui_D16 = Toplevel()
        gui_D16.protocol("WM_DELETE_WINDOW", popup_window_D16_closed)
        gui_D16.title(f'Shodasamsa chart of {name}.')
        gui_D16.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D16 = ImageTk.PhotoImage(image)
        label = Label(gui_D16, image = photo_D16)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D16_window_status = OPEN
    else:
        gui_D16.focus_force()    #Brings focus back to this window
        #gui_D16.bell()
    return

def popup_window_D16_closed():
    global gui_D16_window_status
    global gui_D16
    gui_D16_window_status = CLOSE
    gui_D16.destroy()
    return   

#functions for Vimsamsa chart gui window
def popup_window_D20(name,imagepath):
    global gui_D20_window_status
    global gui_D20
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D20_window_status == CLOSE): #open new window if not active window of lagna
        gui_D20 = Toplevel()
        gui_D20.protocol("WM_DELETE_WINDOW", popup_window_D20_closed)
        gui_D20.title(f'Vimsamsa chart of {name}.')
        gui_D20.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D20 = ImageTk.PhotoImage(image)
        label = Label(gui_D20, image = photo_D20)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D20_window_status = OPEN
    else:
        gui_D20.focus_force()    #Brings focus back to this window
        #gui_D20.bell()
    return

def popup_window_D20_closed():
    global gui_D20_window_status
    global gui_D20
    gui_D20_window_status = CLOSE
    gui_D20.destroy()
    return   

#functions for ChaturVimsamsa chart gui window
def popup_window_D24(name,imagepath):
    global gui_D24_window_status
    global gui_D24
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D24_window_status == CLOSE): #open new window if not active window of lagna
        gui_D24 = Toplevel()
        gui_D24.protocol("WM_DELETE_WINDOW", popup_window_D24_closed)
        gui_D24.title(f'ChaturVimsamsa chart of {name}.')
        gui_D24.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D24 = ImageTk.PhotoImage(image)
        label = Label(gui_D24, image = photo_D24)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D24_window_status = OPEN
    else:
        gui_D24.focus_force()    #Brings focus back to this window
        #gui_D24.bell()
    return

def popup_window_D24_closed():
    global gui_D24_window_status
    global gui_D24
    gui_D24_window_status = CLOSE
    gui_D24.destroy()
    return   

#functions for SaptaVimsamsa chart gui window
def popup_window_D27(name,imagepath):
    global gui_D27_window_status
    global gui_D27
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D27_window_status == CLOSE): #open new window if not active window of lagna
        gui_D27 = Toplevel()
        gui_D27.protocol("WM_DELETE_WINDOW", popup_window_D27_closed)
        gui_D27.title(f'SaptaVimsamsa chart of {name}.')
        gui_D27.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D27 = ImageTk.PhotoImage(image)
        label = Label(gui_D27, image = photo_D27)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D27_window_status = OPEN
    else:
        gui_D27.focus_force()    #Brings focus back to this window
        #gui_D27.bell()
    return

def popup_window_D27_closed():
    global gui_D27_window_status
    global gui_D27
    gui_D27_window_status = CLOSE
    gui_D27.destroy()
    return   

#functions for Trimsamsa chart gui window
def popup_window_D30(name,imagepath):
    global gui_D30_window_status
    global gui_D30
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D30_window_status == CLOSE): #open new window if not active window of lagna
        gui_D30 = Toplevel()
        gui_D30.protocol("WM_DELETE_WINDOW", popup_window_D30_closed)
        gui_D30.title(f'Trimsamsa chart of {name}.')
        gui_D30.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D30 = ImageTk.PhotoImage(image)
        label = Label(gui_D30, image = photo_D30)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D30_window_status = OPEN
    else:
        gui_D30.focus_force()    #Brings focus back to this window
        #gui_D30.bell()
    return

def popup_window_D30_closed():
    global gui_D30_window_status
    global gui_D30
    gui_D30_window_status = CLOSE
    gui_D30.destroy()
    return   

#functions for Khavedamsa chart gui window
def popup_window_D40(name,imagepath):
    global gui_D40_window_status
    global gui_D40
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D40_window_status == CLOSE): #open new window if not active window of lagna
        gui_D40 = Toplevel()
        gui_D40.protocol("WM_DELETE_WINDOW", popup_window_D40_closed)
        gui_D40.title(f'Khavedamsa chart of {name}.')
        gui_D40.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D40 = ImageTk.PhotoImage(image)
        label = Label(gui_D40, image = photo_D40)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D40_window_status = OPEN
    else:
        gui_D40.focus_force()    #Brings focus back to this window
        #gui_D40.bell()
    return

def popup_window_D40_closed():
    global gui_D40_window_status
    global gui_D40
    gui_D40_window_status = CLOSE
    gui_D40.destroy()
    return   

#functions for Akshavedamsa chart gui window
def popup_window_D45(name,imagepath):
    global gui_D45_window_status
    global gui_D45
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D45_window_status == CLOSE): #open new window if not active window of lagna
        gui_D45 = Toplevel()
        gui_D45.protocol("WM_DELETE_WINDOW", popup_window_D45_closed)
        gui_D45.title(f'Akshavedamsa chart of {name}.')
        gui_D45.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D45 = ImageTk.PhotoImage(image)
        label = Label(gui_D45, image = photo_D45)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D45_window_status = OPEN
    else:
        gui_D45.focus_force()    #Brings focus back to this window
        #gui_D45.bell()
    return

def popup_window_D45_closed():
    global gui_D45_window_status
    global gui_D45
    gui_D45_window_status = CLOSE
    gui_D45.destroy()
    return   

#functions for Shashtiamsa chart gui window
def popup_window_D60(name,imagepath):
    global gui_D60_window_status
    global gui_D60
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D60_window_status == CLOSE): #open new window if not active window of lagna
        gui_D60 = Toplevel()
        gui_D60.protocol("WM_DELETE_WINDOW", popup_window_D60_closed)
        gui_D60.title(f'Shashtiamsa chart of {name}.')
        gui_D60.geometry('500x500')
        image = Image.open(imagepath)
        copy_of_image = image.copy()
        photo_D60 = ImageTk.PhotoImage(image)
        label = Label(gui_D60, image = photo_D60)
        label.bind('<Configure>', lambda event, arg=(copy_of_image,label): resize_image(event, arg))
        label.pack(fill=BOTH, expand = YES)
        gui_D60_window_status = OPEN
    else:
        gui_D60.focus_force()    #Brings focus back to this window
        #gui_D60.bell()
    return

def popup_window_D60_closed():
    global gui_D60_window_status
    global gui_D60
    gui_D60_window_status = CLOSE
    gui_D60.destroy()
    return   

#Window for Vimshottari Dasha
def popup_window_VimDasha():
    global gui_VimDasha_window_status
    global gui_VimDasha
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_VimDasha_window_status == CLOSE): #open new window if not active window of lagna
        gui_VimDasha = Toplevel()
        gui_VimDasha.protocol("WM_DELETE_WINDOW", popup_window_VimDasha_closed)
        name = "Shyam Bhat"
        gui_VimDasha.title(f'Vimshottari Dasha {name}.')
        gui_VimDasha.geometry('750x350') 
        #grid layout  
        gui_VimDasha.rowconfigure(0, weight=1)  
        gui_VimDasha.columnconfigure(0, weight=1)  
        
        #Tree view  
        tree = ttk.Treeview(gui_VimDasha)  
        tree.heading('#0', text = 'Vimshottari Dasha')#, anchor=W) 

        for line in dashas.dashaCodeLines:
            exec(line)

        tree.pack(fill="both", expand=True)
        gui_VimDasha_window_status = OPEN
    else:
        gui_VimDasha.focus_force()    #Brings focus back to this window
        #gui_VimDasha.bell()

def popup_window_VimDasha_closed():
    global gui_VimDasha_window_status
    global gui_VimDasha
    gui_VimDasha_window_status = CLOSE
    gui_VimDasha.destroy()

#Window for table
class StaticTable:	
	def __init__(self,root,tabData):
		# code for creating table
		for i in range(len(tabData)):
			for j in range(len(tabData[0])-3): 
				if(i==0): #title row
					fontstyle = ('Arial',13,'bold')
				else: #data row
					fontstyle = ('Arial',13)
				self.e = Entry(root, width=10, fg=tabData[i][-2], justify=CENTER, bg=tabData[i][-3],
							font=fontstyle)
				
				self.e.grid(row=i, column=j)
				self.e.insert(END, tabData[i][j])

D1PlanetsData = [ ]
def PopulatePlanetData(planetdata, lagnadata):
    global D1PlanetsData
    D1PlanetsData = [   ("Planet","Degrees","House","Sign","SignLord","Nak","Nak-Lord","black", "white", "Heading")  ]
    D1PlanetsData.append(("Asc",f'{round(lagnadata["pos"]["dec_deg"], 3)}',1,lagnadata["sign"],lagnadata["lagna-lord"],lagnadata["nakshatra"],lagnadata["nak-ruler"],"white", "black", "Heading"))
    l_plt = "Sun"
    D1PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',planetdata[l_plt]["house-num"],planetdata[l_plt]["sign"],planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"],get_bgClr(planetdata[l_plt]), "black", "Heading"))
    l_plt = "Moon"
    D1PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',planetdata[l_plt]["house-num"],planetdata[l_plt]["sign"],planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"],get_bgClr(planetdata[l_plt]), "black", "Heading"))
    l_plt = "Mars"
    D1PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',planetdata[l_plt]["house-num"],planetdata[l_plt]["sign"],planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"],get_bgClr(planetdata[l_plt]), "black", "Heading"))
    l_plt = "Mercury"
    D1PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',planetdata[l_plt]["house-num"],planetdata[l_plt]["sign"],planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"],get_bgClr(planetdata[l_plt]), "black", "Heading"))
    l_plt = "Jupiter"
    D1PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',planetdata[l_plt]["house-num"],planetdata[l_plt]["sign"],planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"],get_bgClr(planetdata[l_plt]), "black", "Heading"))
    l_plt = "Venus"
    D1PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',planetdata[l_plt]["house-num"],planetdata[l_plt]["sign"],planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"],get_bgClr(planetdata[l_plt]), "black", "Heading"))
    l_plt = "Saturn"
    D1PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',planetdata[l_plt]["house-num"],planetdata[l_plt]["sign"],planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"],get_bgClr(planetdata[l_plt]), "black", "Heading"))
    l_plt = "Rahu"
    D1PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',planetdata[l_plt]["house-num"],planetdata[l_plt]["sign"],planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"],get_bgClr(planetdata[l_plt]), "black", "Heading"))
    l_plt = "Ketu"
    D1PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',planetdata[l_plt]["house-num"],planetdata[l_plt]["sign"],planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"],get_bgClr(planetdata[l_plt]), "black", "Heading"))
    return

def popup_window_D1PlanetDetails(usrInputTk):
    global gui_planetTable_window_status
    global gui_D1PlanetDetails
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_planetTable_window_status == CLOSE): #open new window if not active window of lagna
        #PopulatePlanetData(data.D1["planets"], data.lagna_ascendant)
        PopulatePlanetData(data.charts[usrInputTk.cmbVarga.get()]["planets"], data.charts[usrInputTk.cmbVarga.get()]["ascendant"])
        gui_D1PlanetDetails = Toplevel()
        gui_D1PlanetDetailstable = StaticTable(gui_D1PlanetDetails, D1PlanetsData)
        gui_D1PlanetDetails.protocol("WM_DELETE_WINDOW", popup_window_D1PlanetDetails_closed)
        gui_D1PlanetDetails.title(f'Planetary details of Lagna chart.')
        gui_planetTable_window_status = OPEN
    else:
        gui_D1PlanetDetails.focus_force()    #Brings focus back to this window
        #gui_D1PlanetDetails.bell()
    return

def popup_window_D1PlanetDetails_closed():
    global gui_planetTable_window_status
    gui_planetTable_window_status = CLOSE
    gui_D1PlanetDetails.destroy()
    return

if __name__ == "__main__":
    root = Tk()
    btn = Button(root, text="Open D1", command=lambda: popup_window_D1("Shyam Bhat", 'images/Lagna_chart.png'))
    btn.pack()
    root.mainloop()