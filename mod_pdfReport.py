from fpdf import FPDF
import  mod_astrodata as data
from mod_astrodata import birthdata as bd
from datetime import datetime as dt

global mychart
global reportLevel 
reportLevel = "BASIC"

data1 = [
    ["First name", "Last name", "Age", "City"],
    ["Jules", "Smith", "34", "San Juan"],
    ["Mary", "Ramos", "45", "Orlando"],
    ["Carlson", "Banks", "19", "Los Angeles"],
    ["Lucas", "Cimon", "31", "Saint-Mahturin-sur-Loire"],
    ["Shyam", "Bhat", "31", "Honavar"],
    ["The Great Alexandar of Greece", "Conquerror", "185", "Athens"]
]

def GetPlanetDataArray(planetdata, lagnadata):
    PlanetsData = []
    PlanetsData = [   ("Planet","Degrees","House","Sign","SignLord","Nak","Nak-Lord")  ]
    PlanetsData.append(("Asc",f'{round(lagnadata["pos"]["dec_deg"], 3)}',"1",str(lagnadata["sign"]),lagnadata["lagna-lord"],lagnadata["nakshatra"],lagnadata["nak-ruler"]))
    l_plt = "Sun"
    PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',str(planetdata[l_plt]["house-num"]),str(planetdata[l_plt]["sign"]),planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"]))
    l_plt = "Moon"
    PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',str(planetdata[l_plt]["house-num"]),str(planetdata[l_plt]["sign"]),planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"]))
    l_plt = "Mars"
    PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',str(planetdata[l_plt]["house-num"]),str(planetdata[l_plt]["sign"]),planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"]))
    l_plt = "Mercury"
    PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',str(planetdata[l_plt]["house-num"]),str(planetdata[l_plt]["sign"]),planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"]))
    l_plt = "Jupiter"
    PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',str(planetdata[l_plt]["house-num"]),str(planetdata[l_plt]["sign"]),planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"]))
    l_plt = "Venus"
    PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',str(planetdata[l_plt]["house-num"]),str(planetdata[l_plt]["sign"]),planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"]))
    l_plt = "Saturn"
    PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',str(planetdata[l_plt]["house-num"]),str(planetdata[l_plt]["sign"]),planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"]))
    l_plt = "Rahu"
    PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',str(planetdata[l_plt]["house-num"]),str(planetdata[l_plt]["sign"]),planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"]))
    l_plt = "Ketu"
    PlanetsData.append((l_plt,f'{round(planetdata[l_plt]["pos"]["dec_deg"], 3)}',str(planetdata[l_plt]["house-num"]),str(planetdata[l_plt]["sign"]),planetdata[l_plt]["dispositor"],planetdata[l_plt]["nakshatra"],planetdata[l_plt]["nak-ruler"]))
    return PlanetsData

def getWidthArray(data):
    rowCount = len(data)
    colCount = len(data[0])
    sizearray = []
    widtharray = []
    totSize = 0
    #compute max length word in each column
    for j in range(0,colCount):
        #for every column
        bigwordsize = len(data[0][j]) + 2
        for i in range(0,rowCount):
            currentwordsize = len(str(data[i][j]))
            if(currentwordsize > bigwordsize):
                bigwordsize = currentwordsize
        sizearray.append(bigwordsize)
        totSize = totSize + bigwordsize

    for item in sizearray:
        item_Percent = (item * 100)/totSize
        widtharray.append(int(item_Percent))
    return(widtharray)

class PDF(FPDF):

    def header(self):
        # Logo
        self.image('./images/jyotishyamitra_logo.png', 185, 2, h=20, w=20)
        # Times bold 15
        self.set_font('Times', 'B', 15)
        # Title
        self.cell(170, 10, f'Jyotishyamitra Astrology Report for {mychart["user_details"]["name"]}',ln=True,border=True, align='C')
        # Line break
        #self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Times italic 8
        self.set_font('Times', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
        self.cell(0, 10, 'www.jyotishyamitra.in', 0, 0, 'R', link="https://www.jyotishyamitra.in")

    def loadAllCustomFonts(self):
        self.add_font("Lobster-Regular", "",
                        "./reports/fonts/Lobster-Regular.ttf",
                        uni=True)

    def writeTable(self,data,x,y):
        widtharray = getWidthArray(data)
        tabHead = ""
        tabBody = ""
        for rowNum in range(1,len(data)):
            tabBody = tabBody + f'''\n<tr><td>{'</td><td>'.join(data[rowNum])}</td></tr>'''

        for colNum in range(0,len(data[0])):
            tabHead = tabHead + f'''\n<th width="{widtharray[colNum]}%">{data[0][colNum]}</th>'''

        self.set_xy(x,y)
        self.write_html(
            f"""<table border="1" bgcolor="lime"><thead><tr>
            {tabHead}
        </tr></thead>
        <tbody>{tabBody}
        </tbody></table>""",
            table_line_separators=True,
        )                               

    def addFirstPageBasic(self):
        self.set_font('Times', 'BU', 16)
        self.cell(txt="Jataka Details", w=0, h=10, align='C')
        imageWidth = (self.w / 2.0) - 5
        #put Lagna chart 
        self.image("./images/Lagna_chart.png", x=5, y=30, w=imageWidth)
        #setting caption 
        self.set_font('Courier', 'BI', 10)
        self.set_xy(5,30+imageWidth)    #caption position
        self.cell(txt="Lagna Chart", w=imageWidth, h=3, align='C')

        #planetary data table
        self.ln(10)
        self.set_font('Times', 'BU', 14)
        self.cell(txt="Planetery Details of Lagna Chart", w=0, h=10, align='C')
        self.writeTable(GetPlanetDataArray(mychart["D1"]["planets"], mychart["D1"]["ascendant"]),5,30+imageWidth+5)

        #User details Box
        self.set_font('Courier', 'B', 12)
        userdetails = f'''Lagna : {mychart["D1"]["ascendant"]["sign"]} / {mychart["D1"]["ascendant"]["rashi"]}'
Lagnesh : {mychart["D1"]["ascendant"]["lagna-lord"]}'
Rashi : {data.lagna_moon["sign"]} / {data.lagna_moon["rashi"]}'
Nakshatra : {data.lagna_moon["nakshatra"]}'
NakshatraLord : {data.lagna_moon["nak-ruler"]}'
Maasa : {mychart["user_details"]["maasa"]}'
Tithi : {mychart["user_details"]["tithi"]}'
Vaara : {mychart["user_details"]["vaara"]}'
Yoga : {mychart["user_details"]["yoga"]}'
Karana : {mychart["user_details"]["karana"]}'
Rutu : {mychart["user_details"]["rutu"]}'''

        self.set_xy(18+imageWidth,30)
        self.multi_cell(w=(self.w - imageWidth - 23),h=6, txt=userdetails, align='L', border=True)

    def addVargaChartsinaPage(self):
        #title of the page
        self.set_font('Times', 'BU', 12)
        self.cell(txt="Shodasha Varga Charts", w=0, h=10, align='C')
        
        self.set_font('Times', 'BI', 10)
        imageWidth = (self.w / 3.0) - 5
        self.set_fill_color(255,255,0)  #yellow colour

        #first comes Lagna chart
        self.image("./images/Lagna_chart.png", x=5, y=35, w=imageWidth)
        #setting caption 
        self.set_xy(5,35+imageWidth)    #caption position
        self.cell(txt="D1 - Lagna Chart", w=imageWidth, h=3, align='C', ln=1)
        self.multi_cell(txt="Physical appearance, Health, Entire life",w=imageWidth, h=3, fill=1)

        #next comes Navamsa chart
        self.image("./images/Navamsa_chart.png", x=5+imageWidth+2, y=35, w=imageWidth)
        #setting caption 
        self.set_xy(5+imageWidth+2,35+imageWidth)    #caption position
        self.cell(txt="D9 - Navamsa Chart", w=imageWidth, h=3, align='C', ln=1)
        self.set_x(5+imageWidth+2)
        self.multi_cell(txt="Spouse, Marriage, Business, Second half of life",w=imageWidth, h=3, fill=1)

        #next comes Dasamsa chart
        self.image("./images/Dasamsa_chart.png", x=5+(2*imageWidth)+4, y=35, w=imageWidth)
        #setting caption 
        self.set_xy(5+(2*imageWidth)+4,35+imageWidth)    #caption position
        self.cell(txt="D10 - Dasamsa Chart", w=imageWidth, h=3, align='C', ln=1)
        self.set_x(5+(2*imageWidth)+4)
        self.multi_cell(txt="Matters of great importance, career, honor, awards, fame",w=imageWidth, h=3, fill=1)
    ###############################################################################
        #next comes Hora chart
        self.image("./images/Hora_chart.png", x=5, y=35 + imageWidth + 15, w=imageWidth)
        #setting caption 
        self.set_xy(5,35 + (2*imageWidth) + 15)    #caption position
        self.cell(txt="D2 - Hora Chart", w=imageWidth, h=3, align='C', ln=1)
        self.multi_cell(txt="Wealth, securities, assets",w=imageWidth, h=3, fill=1)

        #next comes Drekkana chart
        self.image("./images/Drekkana_chart.png", x=5+imageWidth+2, y=35 + imageWidth + 15, w=imageWidth)
        #setting caption 
        self.set_xy(5+imageWidth+2,35 + (2*imageWidth) + 15)    #caption position
        self.cell(txt="D3 - Drekkana Chart", w=imageWidth, h=3, align='C', ln=1)
        self.set_x(5+(1*imageWidth)+4)
        self.multi_cell(txt="Happiness through siblings",w=imageWidth, h=3, fill=1)

        #next comes Chaturtamsa chart
        self.image("./images/Chaturtamsa_chart.png", x=5+(2*imageWidth)+4, y=35 + imageWidth + 15, w=imageWidth)
        #setting caption 
        self.set_xy(5+(2*imageWidth)+4,35 + (2*imageWidth) + 15)    #caption position
        self.cell(txt="D4 - Chaturtamsa Chart", w=imageWidth, h=3, align='C', ln=1)
        self.set_x(5+(2*imageWidth)+4)
        self.multi_cell(txt="Fortune, Unmovable Assets",w=imageWidth, h=3, fill=1)

    ###############################################################################
        #next comes Saptamsa chart
        self.image("./images/Saptamsa_chart.png", x=5, y=35 + (2*imageWidth) + 30, w=imageWidth)
        #setting caption 
        self.set_xy(5,35 + (3*imageWidth) + 30)    #caption position
        self.cell(txt="D7 - Saptamsa Chart", w=imageWidth, h=3, align='C', ln=1)
        self.multi_cell(txt="sons, grandsons, children",w=imageWidth, h=3, fill=1)

        #next comes Dwadasamsa chart
        self.image("./images/Dwadasamsa_chart.png", x=5+imageWidth+2, y=35 + (2*imageWidth) + 30, w=imageWidth)
        #setting caption 
        self.set_xy(5+imageWidth+2,35 + (3*imageWidth) + 30)    #caption position
        self.cell(txt="D12 - Dwadasamsa Chart", w=imageWidth, h=3, align='C', ln=1)
        self.set_x(5+(1*imageWidth)+4)
        self.multi_cell(txt="Parents",w=imageWidth, h=3, fill=1)

        #next comes Shodasamsa chart
        self.image("./images/Shodasamsa_chart.png", x=5+(2*imageWidth)+4, y=35 + (2*imageWidth) + 30, w=imageWidth)
        #setting caption 
        self.set_xy(5+(2*imageWidth)+4,35 + (3*imageWidth) + 30)    #caption position
        self.cell(txt="D16 - Shodasamsa Chart", w=imageWidth, h=3, align='C', ln=1)
        self.set_x(5+(2*imageWidth)+4)
        self.multi_cell(txt="Benefits, and adversities through vehicles",w=imageWidth, h=3, fill=1)

        #add one more page as current page is full
        self.add_page()
        self.set_font('Times', 'BU', 12)
        self.cell(txt="Shodasha Varga Charts - Continued", w=0, h=10, align='C')
        
        self.set_font('Times', 'BI', 10)
    ###############################################################################
        #next comes Vimsamsa chart
        self.image("./images/Vimsamsa_chart.png", x=5, y=35, w=imageWidth)
        #setting caption 
        self.set_xy(5,35+imageWidth)    #caption position
        self.cell(txt="D20 - Vimsamsa Chart", w=imageWidth, h=3, align='C', ln=1)
        self.multi_cell(txt="Spiritual life, Ishta Devata, Sadhana",w=imageWidth, h=3, fill=1)

        #next comes Chaturvimsamsa chart
        self.image("./images/Chaturvimsamsa_chart.png", x=5+imageWidth+2, y=35, w=imageWidth)
        #setting caption 
        self.set_xy(5+imageWidth+2,35+imageWidth)    #caption position
        self.cell(txt="D24 - Chaturvimsamsa Chart", w=imageWidth, h=3, align='C', ln=1)
        self.set_x(5+(1*imageWidth)+4)
        self.multi_cell(txt="Learning, education",w=imageWidth, h=3, fill=1)

        #next comes Saptavimsamsa chart
        self.image("./images/Saptavimsamsa_chart.png", x=5+(2*imageWidth)+4, y=35, w=imageWidth)
        #setting caption 
        self.set_xy(5+(2*imageWidth)+4,35+imageWidth)    #caption position
        self.cell(txt="D27 - Saptavimsamsa Chart", w=imageWidth, h=3, align='C', ln=1)
        self.set_x(5+(2*imageWidth)+4)
        self.multi_cell(txt="Strength, and weakness",w=imageWidth, h=3, fill=1)
    ###############################################################################
        #next comes Trimsamsa chart
        self.image("./images/Trimsamsa_chart.png", x=5, y=35 + imageWidth + 15, w=imageWidth)
        #setting caption 
        self.set_xy(5,35 + (2*imageWidth) + 15)    #caption position
        self.cell(txt="D30 - Trimsamsa Chart", w=imageWidth, h=3, align='C', ln=1)
        self.multi_cell(txt="Evil effects",w=imageWidth, h=3, fill=1)

        #next comes Khavedamsa chart
        self.image("./images/Khavedamsa_chart.png", x=5+imageWidth+2, y=35 + imageWidth + 15, w=imageWidth)
        #setting caption 
        self.set_xy(5+imageWidth+2,35 + (2*imageWidth) + 15)    #caption position
        self.cell(txt="D40 - Khavedamsa Chart", w=imageWidth, h=3, align='C', ln=1)
        self.set_x(5+(1*imageWidth)+4)
        self.multi_cell(txt="Auspicious and inauspicious effec",w=imageWidth, h=3, fill=1)

        #next comes Akshavedamsa chart
        self.image("./images/Akshavedamsa_chart.png", x=5+(2*imageWidth)+4, y=35 + imageWidth + 15, w=imageWidth)
        #setting caption 
        self.set_xy(5+(2*imageWidth)+4,35 + (2*imageWidth) + 15)    #caption position
        self.cell(txt="D45 - Akshavedamsa Chart", w=imageWidth, h=3, align='C', ln=1)
        self.set_x(5+(2*imageWidth)+4)
        self.multi_cell(txt="Legacy, Poorva doshas, Pirti doshas",w=imageWidth, h=3, fill=1)

    ###############################################################################
        #next comes Shashtiamsa chart
        self.image("./images/Shashtiamsa_chart.png", x=5, y=35 + (2*imageWidth) + 30, w=imageWidth)
        #setting caption 
        self.set_xy(5,35 + (3*imageWidth) + 30)    #caption position
        self.cell(txt="D60 - Shashtiamsa Chart", w=imageWidth, h=3, align='C', ln=1)
        self.multi_cell(txt="Totality of results",w=imageWidth, h=3, fill=1)

    def createTitlePage(self):
        title = f'JyotishyaMitra Basic Report of \n {mychart["user_details"]["name"]}'
        self.set_font('Lobster-Regular', '', 25)
        self.set_text_color(255,0,0)
        self.ln(10)
        self.multi_cell(w=0,h=8, txt=title, align='C', border=False)
        self.ln(10)
        self.image('./images/jyotishyamitra.png',  x=40)
        self.ln(5)
        #section for User details -TOB, DOB, POB
        self.set_font('Times', '', 12)
        self.set_text_color(0,0,0)
        creationdetails = f'''Created on: {dt.now().strftime("%d/%b/%Y [%A] - %H:%M:%S")}'''
        userdetail = f'''Date of birth:  {bd["DOB"]["day"]}/{bd["DOB"]["month"]}/{bd["DOB"]["year"]}
Time Of birth:  {bd["TOB"]["hour"]} : {bd["TOB"]["min"]} : {bd["TOB"]["sec"]} 
Place of Birth:  {bd["POB"]["name"]}
{creationdetails}'''
        self.multi_cell(w=0,h=5, txt=userdetail, align='C', border=True)

    def addYogaDoshasSection(self):
        #title of the page
        self.set_font('helvetica', 'BU', 14)
        self.set_text_color(0,0,255)
        self.cell(txt="Yogas and Doshas in Native's Kundali", w=0, h=10, align='C')

        #Enlisting all the Yogas and doshas in natives kundali
        yogadoshastring = ">, <".join(mychart["yogadoshas"])
        self.ln(10)
        self.set_font('Times', 'I', 12)
        self.set_text_color(0,0,0)
        self.multi_cell(txt=f'''The Yoga/Doshas in {mychart["user_details"]["name"]}'s Kundali are: <{yogadoshastring}>''',w=0, h=5, border = True, align='L')
        self.ln(5)
        self.line(0, self.get_y(), self.w, self.get_y())
        self.ln(1)
        self.line(0, self.get_y(), self.w, self.get_y())
        self.ln(1)
        self.line(0, self.get_y(), self.w, self.get_y())


        #Adding Each Yoga/Dosha details
        self.set_font('Times', '', 10)
        imageWidth = (self.w / 2)
        for yogadosha in data.yogadoshas:
            #Put the image specific to yogadosha to left
            self.ln(10)
            self.image(f"./images/yogaImages/{yogadosha}_chart.png", x=5, w=imageWidth)
            imageEnd_ypos = self.get_y()
            ypos= imageEnd_ypos - imageWidth
            #print(data.yogadoshas[yogadosha]["name"])
            
            #put the yogadosha details right to the image
            #Title
            self.set_xy(3 + imageWidth, ypos)
            self.set_font('Times', 'BU', 16)
            self.set_text_color(220,0,0)
            self.cell(txt=yogadosha, w=0, h=10, align='C', ln=True, link=data.yogadoshas[yogadosha]["Source"])

            #Yoga dosha name
            self.set_font('Times', 'B', 14)
            self.set_text_color(0,0,0)
            ypos = self.get_y()
            self.set_xy(5 + imageWidth, ypos)
            xpos = self.get_x()
            ydname = f'''{data.yogadoshas[yogadosha]["type"]} : '''
            self.cell(txt=ydname, w=5, h=5, align='L', ln=False)

            xpos = self.get_x() + 12
            self.set_font('Times', 'I', 14)
            self.set_text_color(80,50,200)            
            self.set_xy(xpos, ypos)
            ydname = f'''{data.yogadoshas[yogadosha]["name"]} {data.yogadoshas[yogadosha]["type"]}'''
            self.multi_cell(txt=ydname, w=0, h=5, align='L')
            self.ln(5)

            #Yoga/Dosha Rule
            self.set_font('Times', 'B', 14)
            self.set_text_color(0,0,0)
            ypos = self.get_y()
            self.set_xy(5 + imageWidth, ypos)
            xpos = self.get_x()
            ydrule = f'''Rule : '''
            self.cell(txt=ydrule, w=0, h=5, align='L', ln=False)

            self.set_font('Times', 'I', 14)
            self.set_text_color(0,0,200)            
            self.set_xy(xpos, ypos)
            ydrule = f'''              {data.yogadoshas[yogadosha]["Rule"]}'''
            self.multi_cell(txt=ydrule, w=0, h=5, align='L')
            self.ln(5)

            #Yoga/Dosha Notes
            self.set_font('Times', 'B', 14)
            self.set_text_color(0,0,0)
            ypos = self.get_y()
            self.set_xy(5 + imageWidth, ypos)
            xpos = self.get_x()
            ydnote = f'''Note : '''
            self.cell(txt=ydnote, w=0, h=5, align='L', ln=False)

            self.set_font('Times', 'I', 14)
            self.set_text_color(155,0,155)            
            self.set_xy(xpos, ypos)
            ydnote = f'''              {data.yogadoshas[yogadosha]["Note"]}'''
            self.multi_cell(txt=ydnote, w=0, h=5, align='L')
            self.ln(5)

            #Yoga/Dosha Results
            #get the ypositionn whichever is lower as now results will be below image full pdf wide.
            if(imageEnd_ypos >= self.get_y()):
                ypos = imageEnd_ypos + 5
            else:
                ypos = self.get_y() + 5

            self.set_font('Times', 'B', 14)
            self.set_text_color(0,0,0)
            self.set_xy(5, ypos)
            xpos = self.get_x()
            ydresults = f'''Results : '''
            self.cell(txt=ydresults, w=0, h=5, align='L', ln=False)

            self.set_font('Times', 'I', 14)
            self.set_text_color(50,0,105)            
            self.set_xy(xpos, ypos)
            ydresults = f'''                 {data.yogadoshas[yogadosha]["Result"]}'''
            self.multi_cell(txt=ydresults, w=0, h=5, align='L')
            self.ln(5)

            #Dosha Remedies
            if(data.yogadoshas[yogadosha]["type"] == "Dosha"):
                ypos = self.get_y()
                self.set_font('Times', 'B', 14)
                self.set_text_color(0,0,0)
                self.set_xy(5, ypos)
                xpos = self.get_x()
                ydremedies = f'''Remedies : '''
                self.cell(txt=ydremedies, w=0, h=5, align='L', ln=False)

                self.set_font('Times', 'I', 14)
                self.set_text_color(51,102,0)            
                self.set_xy(xpos, ypos)
                ydremedies = f'''                    {data.yogadoshas[yogadosha]["Remedies"]}'''
                self.multi_cell(txt=ydremedies, w=0, h=5, align='L')
                self.ln(5)

            #End of Yoga Dosha so draw a line
            self.line(0, self.get_y(), self.w, self.get_y())

             


def GeneratePDFReport(charts):
    # Instantiation of inherited class
    global mychart
    global reportLevel
    mychart = charts.copy()
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.loadAllCustomFonts()
    pdf.add_page()
    pdf.set_font('Times', '', 12)    
    #Set Title page
    pdf.createTitlePage()

    if (reportLevel == "BASIC"):
        #generate basic report
        #Add a table
        pdf.add_page()
        pdf.addFirstPageBasic()

        #adding all varga charts
        pdf.add_page()
        pdf.addVargaChartsinaPage()

        #adding the Yogas 
        pdf.add_page()
        pdf.addYogaDoshasSection()
        
    
    pdf.output(f'./reports/{charts["user_details"]["name"]}_jyotishamitraReport.pdf', 'F')

if __name__ == '__main__':
    image_path = './images/Lagna_chart.svg'
    GeneratePDFReport(data.charts)
    #add_image(image_path)
    