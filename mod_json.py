import mod_constants as c
import mod_astrodata as data
import mod_drawChart as dc
import json

# astrodata.json related functions
def dump_astrodata_injson():
    with open('./json/astrodata.json', 'w') as json_astrodatafile:
        json.dump(dict(data.charts), json_astrodatafile, indent=4)
    return

# chartDraw_cfg.json related functions
def load_drawChartConfig():
    with open('./json/chartDraw_cfg.json', 'r') as json_birthfile:        
        dc.chartCfg = json.loads(json_birthfile.read()) 
    return

# birthdatas.json related functions
def load_birthdatas():
    with open('./json/birthdatas.json', 'r') as json_birthfile:        
        data.birthdatas = json.loads(json_birthfile.read()) 
    return

def get_birthdata(id):
    load_birthdatas()
    needed_birthdata = data.birthdatas.get(id, "NOT_FOUND")
    #check if the element with ID exists
    if ("NOT_FOUND" == needed_birthdata):
        #Element cannot be fetched
        print(f'Given ID {id} doesnt exist. So can not be fetched')
    return needed_birthdata
    
def dump_birthdatas_injson():
    with open('./json/birthdatas.json', 'w') as json_birthfile:
        json.dump(dict(data.birthdatas), json_birthfile, indent=4)
    return

def add_birthdata2DB(birthdata, id):
    #check if the element with ID already exists
    if ("NOT_FOUND" == data.birthdatas.get(id, "NOT_FOUND")):
        #New element - can be added
        data.birthdatas[id] = birthdata
        return True
    else:   #element already exist and so not possible to add
        print(f'Given ID {id} already exists. So can not be added')
        return False

# places.json related functions
def load_places():
    with open('./json/places.json', 'r') as json_placesfile:        
        data.places = json.loads(json_placesfile.read()) 
    return

def get_placedata(id):
    load_places()
    needed_placedata = data.places.get(id, "NOT_FOUND")
    #check if the element with ID exists
    if ("NOT_FOUND" == needed_placedata):
        #Element cannot be fetched
        print(f'Given ID {id} doesnt exist in places database. So can not be fetched')
    return needed_placedata

def dump_placedatas_injson():
    with open('./json/places.json', 'w') as json_placesfile:
        json.dump(dict(data.places), json_placesfile, indent=4)
    return

def add_place2DB(place, id):
    #check if the element with ID already exists
    if ("NOT_FOUND" == data.places.get(id, "NOT_FOUND")):
        #New element - can be added
        data.places[id] = place
        return True
    else:   #element already exist and so not possible to add
        print(f'Given ID {id} already exists in places database. So can not be added')
        return False

