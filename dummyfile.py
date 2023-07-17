from fpdf import FPDF

pdf = FPDF()

data = [
    ["First name", "Last name", "Age", "City"],
    ["Jules", "Smith", "34", "San Juan"],
    ["Mary", "Ramos", "45", "Orlando"],
    ["Carlson", "Banks", "19", "Los Angeles"],
    ["Lucas", "Cimon", "31", "Saint-Mahturin-sur-Loire"],
    ["Shyam", "Bhat", "31", "Honavar"],
    ["The Great Alexandar of Greece", "Conquerror", "185", "Athens"]
]

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
            currentwordsize = len(data[i][j])
            if(currentwordsize > bigwordsize):
                bigwordsize = currentwordsize
        sizearray.append(bigwordsize)
        totSize = totSize + bigwordsize

    for item in sizearray:
        item_Percent = (item * 100)/totSize
        widtharray.append(int(item_Percent))
    return(widtharray)

pdf.set_font_size(16)
pdf.add_page()
 
widtharray = getWidthArray(data)
tabHead = ""
tabBody = ""
for rowNum in range(1,len(data)):
    print(rowNum)
    tabBody = tabBody + f'''\n<tr><td>{'</td><td>'.join(data[rowNum])}</td></tr>'''

for colNum in range(0,len(data[0])):
    tabHead = tabHead + f'''\n<th width="{widtharray[colNum]}%">{data[0][colNum]}</th>'''

pdf.write_html(
    f"""<table border="1"><thead><tr>
    {tabHead}
</tr></thead>
<tbody>{tabBody}
</tbody></table>""",
    table_line_separators=True,
)
pdf.output('table_html.pdf')