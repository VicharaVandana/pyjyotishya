#standard modules import
from tkinter import *
from tkinter import messagebox

#local modules import
import mod_constants as c
import mod_lagna 
import mod_divisional as varga
import mod_astrodata as data
import mod_json as js
import mod_drawChart as dc
import dashas
import mod_pdfReport as pdfrep
import mod_yogadoshas as yd
import mod_bala as bala

userlist = []

# Function for checking the
# key pressed and updating
# the listbox
def update_cmbbox(event):
    global userlist 
    value = event.widget.get()      
    # get data from userlist
    if value == '':
        data = userlist
    else:
        data = []
        for item in userlist:
            if value.lower() in item.lower():
                data.append(item) 
    # update data in combobox
    populateCombobox(event.widget, data)
    return
   

#Get the userlist in Database [birthdatas.json]
def getUserList():
    global userlist
    js.load_birthdatas()
    userlist = list(data.birthdatas.keys())

def pupulateUserListinForm(usrInputTk):
    global userlist
    getUserList()
    populateCombobox(usrInputTk.cmbName, userlist)

#Update the combobox with the values in the list
def populateCombobox(cmbBoxTk, valList):
    #update the values in tk combobox
    cmbBoxTk.configure(values=valList)
    return

def FetchUserInputData_formBirthdata(usrInputTk):
    #populate the birthdatastr from user input
    PopulateBirthdatastr4mUserInput(usrInputTk)

    #validate the userinputs in birthdatastr dict and if something is wrong print the output
    validationRes = data.validate_birthdatastr2birthdata()
    #print(validationRes)
    if (validationRes == "SUCCESS"):
        #adding the userdata to database
        js.load_birthdatas()
        if(True == js.add_birthdata2DB(data.birthdata, data.birthdata["name"].lower())):    #New User Data so add to database
            js.dump_birthdatas_injson()
    
        #adding place to database
        js.load_places()
        myplace = data.birthdata["POB"]
        myplaceid = myplace["name"].lower()
        if(True == js.add_place2DB(myplace,myplaceid)): #new place
            js.dump_placedatas_injson()

        #computing the Lagna chart and other details on that
        data.clearAstroData(data.charts)
        dashas.clearDashaDetails()
        mod_lagna.compute_lagnaChart_custom(data.birthdata)
        varga.compute_Dx_4m_D1(data.charts,"D9")
        varga.compute_Dx_4m_D1(data.charts,"D10")
        varga.compute_Dx_4m_D1(data.charts,"D2")
        varga.compute_Dx_4m_D1(data.charts,"D3")
        varga.compute_Dx_4m_D1(data.charts,"D4")
        varga.compute_Dx_4m_D1(data.charts,"D7")
        varga.compute_Dx_4m_D1(data.charts,"D12")
        varga.compute_Dx_4m_D1(data.charts,"D16")
        varga.compute_Dx_4m_D1(data.charts,"D20")
        varga.compute_Dx_4m_D1(data.charts,"D24")
        varga.compute_Dx_4m_D1(data.charts,"D27")
        varga.compute_Dx_4m_D1(data.charts,"D30")
        varga.compute_Dx_4m_D1(data.charts,"D40")
        varga.compute_Dx_4m_D1(data.charts,"D45")
        varga.compute_Dx_4m_D1(data.charts,"D60")

        #COMPUTE BALAS FOR PLANETS
        bala.compute_VimshopakaBalas()
        bala.compute_shadbala()


        js.dump_astrodata_injson()
        #creating Lagna chart image
        js.load_drawChartConfig()
        dc.create_chartSVG(data.D1)
        dc.create_chartSVG(data.D9)
        dc.create_chartSVG(data.D10)
        dc.create_chartSVG(data.D2)
        dc.create_chartSVG(data.D3)
        dc.create_chartSVG(data.D4)
        dc.create_chartSVG(data.D7)
        dc.create_chartSVG(data.D12)
        dc.create_chartSVG(data.D16)
        dc.create_chartSVG(data.D20)
        dc.create_chartSVG(data.D24)
        dc.create_chartSVG(data.D27)
        dc.create_chartSVG(data.D30)
        dc.create_chartSVG(data.D40)
        dc.create_chartSVG(data.D45)
        dc.create_chartSVG(data.D60)

        dashas.Vimshottari(data.charts[usrInputTk.cmbVarga.get()])

        #update user details in the form
        UpdateUserDetaisinform(usrInputTk)

        #Compute Yogas and Doshas
        yd.ComputeYogaDoshas(data.charts)
        js.dump_astrodata_injson()

        #temporarily create PDF Report
        pdfrep.GeneratePDFReport(data.charts)

    else:   #if validation is not done then display the error
        messagebox.showerror('User Input Error', validationRes)
    return

def FetchPlacedata_updateFormfields(usrInputTk):
    placeId = usrInputTk.Place.get().lower().strip()
    l_place = js.get_placedata(placeId)
    if ("NOT_FOUND" == l_place):
        messagebox.showerror('Fetch Error', f'Given ID "{placeId}" doesnt exist in places database. So can not be fetched')
    else:   #place details fetched. Now update it in form
        usrInputTk.Place.delete(0,END)
        usrInputTk.Place.insert(0,l_place["name"])
        usrInputTk.lon.delete(0,END)
        usrInputTk.lon.insert(0,str(l_place["lon"]))
        usrInputTk.lat.delete(0,END)
        usrInputTk.lat.insert(0,str(l_place["lat"]))
        usrInputTk.timezone.delete(0,END)
        usrInputTk.timezone.insert(0,str(l_place["timezone"]))
    return

def ClearFormfields(usrInputTk):
    usrInputTk.cmbName.delete(0,END)
    usrInputTk.cmbGender.set('')
    usrInputTk.yyyy.delete(0,END)
    usrInputTk.mm.delete(0,END)
    usrInputTk.dd.delete(0,END)
    usrInputTk.hh.delete(0,END)
    usrInputTk.mn.delete(0,END)
    usrInputTk.ss.delete(0,END)
    usrInputTk.Place.delete(0,END)
    usrInputTk.lon.delete(0,END)
    usrInputTk.lat.delete(0,END)
    usrInputTk.timezone.delete(0,END)

    usrInputTk.udLagna["text"]=f'Lagna : '
    usrInputTk.udLagnesh["text"]=f'Lagnesh : '
    usrInputTk.udRashi["text"]=f'Rashi : '
    usrInputTk.udNakshatra["text"]=f'Nakshatra : '
    usrInputTk.udNakshatraLord["text"]=f'NakshatraLord : '
    usrInputTk.udMaasa["text"]=f'Maasa : '
    usrInputTk.udTithi["text"]=f'Tithi : '
    usrInputTk.udVaara["text"]=f'Vaara : '
    usrInputTk.udYoga["text"]=f'Yoga : '
    usrInputTk.udKarana["text"]=f'Karana : '
    usrInputTk.udRutu["text"]=f''

    data.isAstroDataComputed = False
    return

def FetchBirthdata_updateFormfields(usrInputTk):
    userId = usrInputTk.cmbName.get().lower().strip()
    l_birthdata = js.get_birthdata(userId)
    if ("NOT_FOUND" == l_birthdata):
        messagebox.showerror('Fetch Error', f'Given ID "{userId}" doesnt exist in birthdatas database. So can not be fetched')
    else:   #user birth details fetched. Now update it in form
        usrInputTk.cmbName.delete(0,END)
        usrInputTk.cmbName.insert(0,l_birthdata["name"])

        if(l_birthdata["Gender"] == "Male"):
            usrInputTk.cmbGender.current(0)
        elif(l_birthdata["Gender"] == "Female"):
            usrInputTk.cmbGender.current(1)
        else:
            usrInputTk.cmbGender.current(2)

        usrInputTk.yyyy.delete(0,END)
        usrInputTk.yyyy.insert(0,l_birthdata["DOB"]["year"])
        usrInputTk.mm.delete(0,END)
        usrInputTk.mm.insert(0,l_birthdata["DOB"]["month"])
        usrInputTk.dd.delete(0,END)
        usrInputTk.dd.insert(0,l_birthdata["DOB"]["day"])
        usrInputTk.hh.delete(0,END)
        usrInputTk.hh.insert(0,l_birthdata["TOB"]["hour"])
        usrInputTk.mn.delete(0,END)
        usrInputTk.mn.insert(0,l_birthdata["TOB"]["min"])
        usrInputTk.ss.delete(0,END)
        usrInputTk.ss.insert(0,l_birthdata["TOB"]["sec"])
        usrInputTk.Place.delete(0,END)
        usrInputTk.Place.insert(0,l_birthdata["POB"]["name"])
        usrInputTk.lon.delete(0,END)
        usrInputTk.lon.insert(0,str(l_birthdata["POB"]["lat"]))
        usrInputTk.lat.delete(0,END)
        usrInputTk.lat.insert(0,str(l_birthdata["POB"]["lon"]))
        usrInputTk.timezone.delete(0,END)
        usrInputTk.timezone.insert(0,str(l_birthdata["POB"]["timezone"]))
    return

def UpdateUserDetaisinform(usrInputTk):
    #updating User details
    usrInputTk.udLagna["text"]=f'Lagna : {data.lagna_ascendant["sign"]} / {data.lagna_ascendant["rashi"]}'
    usrInputTk.udLagnesh["text"]=f'Lagnesh : {data.lagna_ascendant["lagna-lord"]}'
    usrInputTk.udRashi["text"]=f'Rashi : {data.lagna_moon["sign"]} / {data.lagna_moon["rashi"]}'
    usrInputTk.udNakshatra["text"]=f'Nakshatra : {data.lagna_moon["nakshatra"]}'
    usrInputTk.udNakshatraLord["text"]=f'NakshatraLord : {data.lagna_moon["nak-ruler"]}'
    usrInputTk.udMaasa["text"]=f'Maasa : {data.charts["user_details"]["maasa"]}'
    usrInputTk.udTithi["text"]=f'Tithi : {data.charts["user_details"]["tithi"]}'
    usrInputTk.udVaara["text"]=f'Vaara : {data.charts["user_details"]["vaara"]}'
    usrInputTk.udYoga["text"]=f'Yoga : {data.charts["user_details"]["yoga"]}'
    usrInputTk.udKarana["text"]=f'Karana : {data.charts["user_details"]["karana"]}'
    usrInputTk.udRutu["text"]=f'{data.charts["user_details"]["rutu"]}'
    return

#Read all values in Birth Details in MainWindow and prepare the birthdata dictionary
def PopulateBirthdatastr4mUserInput(usrInputTk):
    data.birthdatastr["name"] = usrInputTk.cmbName.get()
    data.birthdatastr["Gender"] = usrInputTk.cmbGender.get()
    data.birthdatastr["DOB"]["year"] = usrInputTk.yyyy.get()
    data.birthdatastr["DOB"]["month"] = usrInputTk.mm.get()
    data.birthdatastr["DOB"]["day"] = usrInputTk.dd.get()
    data.birthdatastr["TOB"]["hour"] = usrInputTk.hh.get()
    data.birthdatastr["TOB"]["min"] = usrInputTk.mn.get()
    data.birthdatastr["TOB"]["sec"] = usrInputTk.ss.get()
    data.birthdatastr["POB"]["name"] = usrInputTk.Place.get()
    data.birthdatastr["POB"]["lon"] = usrInputTk.lat.get()
    data.birthdatastr["POB"]["lat"] = usrInputTk.lon.get()
    data.birthdatastr["POB"]["timezone"] = usrInputTk.timezone.get()
    #data.birthdata["TOB"]["hour"] = usrInputTk.hh.delete(0,END)
    ##data.birthdata["TOB"]["hour"] = usrInputTk.hh.insert(0,"14")
    #print(data.birthdata)
    return