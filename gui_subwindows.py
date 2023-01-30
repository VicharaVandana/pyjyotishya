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
gui_D1planet_window_status = CLOSE
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

def popup_window_D1PlanetDetails():
    global gui_D1planet_window_status
    global gui_D1PlanetDetails
    if(data.isAstroDataComputed == False):
        messagebox.showerror('PreCalculation Request Error', "Planetary data is not computed yet. Please provide birth details and submit first!")
        return
    if (gui_D1planet_window_status == CLOSE): #open new window if not active window of lagna
        PopulatePlanetData(data.D1["planets"], data.lagna_ascendant)
        gui_D1PlanetDetails = Toplevel()
        gui_D1PlanetDetailstable = StaticTable(gui_D1PlanetDetails, D1PlanetsData)
        gui_D1PlanetDetails.protocol("WM_DELETE_WINDOW", popup_window_D1PlanetDetails_closed)
        gui_D1PlanetDetails.title(f'Planetary details of Lagna chart.')
        gui_D1planet_window_status = OPEN
    else:
        gui_D1PlanetDetails.focus_force()    #Brings focus back to this window
        #gui_D1PlanetDetails.bell()
    return

def popup_window_D1PlanetDetails_closed():
    global gui_D1planet_window_status
    gui_D1planet_window_status = CLOSE
    gui_D1PlanetDetails.destroy()
    return

if __name__ == "__main__":
    root = Tk()
    btn = Button(root, text="Open D1", command=lambda: popup_window_D1("Shyam Bhat", 'images/Lagna_chart.png'))
    btn.pack()
    root.mainloop()