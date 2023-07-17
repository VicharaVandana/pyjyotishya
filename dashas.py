#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# dashas.py -- module for Dasha computation. All Dahsa data computed for given birth details handled here.
#   Dashas [Vimshottari etc]
# 
# Copyright (C) 2022 Shyam Bhat  <vicharavandana@gmail.com>
# Downloaded from "https://github.com/VicharaVandana/jyotishyam.git"
#
# This file is part of the "jyotishyam" Python library
# for computing Hindu jataka with sidereal lahiri ayanamsha technique 
# using swiss ephemeries
#

#import necessary modules
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import mod_astrodata as data
from mod_general import *

#necessary definitions and constructs for Dasha
dashaVimshottariSkeleton = {"Venus":{   "Nakshatras": ["Bharani", "Purva Phalguni", "Purva Ashadha"],
                                        "duration"  : 20, #20 years out of 120 years
                                        "percentage": (20.0/120),
                                        "prev-dasha": "Ketu",
                                        "next-dasha": "Sun"
                                    },
                            "Sun":  {   "Nakshatras": ["Kritika", "Uttara Phalguni", "Uttara Ashadha"],
                                        "duration"  : 6, #6 years out of 120 years
                                        "percentage": (6.0/120),
                                        "prev-dasha": "Venus",
                                        "next-dasha": "Moon"
                                    },
                            "Moon": {   "Nakshatras": ["Rohini", "Hasta", "Shravana"],
                                        "duration"  : 10, #10 years out of 120 years
                                        "percentage": (10.0/120),
                                        "prev-dasha": "Sun",
                                        "next-dasha": "Mars"
                                    },
                            "Mars": {   "Nakshatras": ["Mrigashira", "Chitra", "Dhanishta"],
                                        "duration"  : 7, #7 years out of 120 years
                                        "percentage": (7.0/120),
                                        "prev-dasha": "Moon",
                                        "next-dasha": "Rahu"
                                    },
                            "Rahu": {   "Nakshatras": ["Ardra", "Swati", "Shatabhishak"],
                                        "duration"  : 18, #18 years out of 120 years
                                        "percentage": (18.0/120),
                                        "prev-dasha": "Mars",
                                        "next-dasha": "Jupiter"
                                    },
                            "Jupiter": {"Nakshatras": ["Punarvasu", "Vishaka", "Purva Ashadha"],
                                        "duration"  : 16, #16 years out of 120 years
                                        "percentage": (16.0/120),
                                        "prev-dasha": "Rahu",
                                        "next-dasha": "Saturn"
                                    },
                            "Saturn": { "Nakshatras": ["Pushya", "Anurada", "Uttara Bhadrapada"],
                                        "duration"  : 19, #19 years out of 120 years
                                        "percentage": (19.0/120),
                                        "prev-dasha": "Jupiter",
                                        "next-dasha": "Mercury"
                                      },
                            "Mercury": {"Nakshatras": ["Ashlesha", "Jyeshta", "Revati"],
                                        "duration"  : 17, #17 years out of 120 years
                                        "percentage": (17.0/120),
                                        "prev-dasha": "Saturn",
                                        "next-dasha": "Ketu"
                                    },
                            "Ketu": {   "Nakshatras": ["Ashwini", "Magha", "Mula"],
                                        "duration"  : 7, #7 years out of 120 years
                                        "percentage": (7.0/120),
                                        "prev-dasha": "Mercury",
                                        "next-dasha": "Venus"
                                    }
                            }

#Takes Moon longitude in seconds, Dasha lord and Birth date and gives the start date of Dasha lords dasha
def computeStartDate_FirstDashaLord(lngsecondsMoon, dashaLord, birthDate):
    #lenth of a nakshatra in seconds is 13deg x 3600 + 20min x 60
    l_nakLenseconds = ((13*3600)+(20*60))
    #dasha lord dasha duration in days
    l_dashaDurationDays = 365.25 * dashaVimshottariSkeleton[dashaLord]["duration"]
    #How much moon has progressed into the nakshatra in seconds 
    l_deltalngseconds = lngsecondsMoon % l_nakLenseconds

    #calculate how many days have passed on birthday since dasha lord started his dasha
    l_elapsedDashaDurationDays = ((l_deltalngseconds * l_dashaDurationDays) / l_nakLenseconds)
    ##print(f'elapsed duration in days is {l_elapsedDashaDurationDays}')
    #Calculate the start date of dasha from subtracting elapsed date from birthday
    l_dashaStartDate = birthDate - timedelta(days=l_elapsedDashaDurationDays)

    return(l_dashaStartDate)

vimshottariDasha = []
mahadashaPlanetEntry = {
                        "name": "",
                        "startDate": datetime(year=1, month=1, day=1, hour=0, minute=0, second=0),
                        "endDate": datetime(year=1, month=1, day=1, hour=0, minute=0, second=0),
                        "entryString": "",
                        "level": "mahadasha",
                        "sublevel": "antardasha",
                        "antardasha" : []   #contains array of Antardasha planet entries
                        }
antardashaPlanetEntry = {
                        "name": "",
                        "startDate": datetime(year=1, month=1, day=1, hour=0, minute=0, second=0),
                        "endDate": datetime(year=1, month=1, day=1, hour=0, minute=0, second=0),
                        "entryString": "",
                        "level": "antardasha",
                        "sublevel": "paryantardasha",
                        "paryantardasha" : []   #contains array of paryantardasha planet entries
                        }
paryantardashaPlanetEntry = {
                        "name": "",
                        "startDate": datetime(year=1, month=1, day=1, hour=0, minute=0, second=0),
                        "endDate": datetime(year=1, month=1, day=1, hour=0, minute=0, second=0),
                        "entryString": "",
                        "level": "paryantardasha",
                        "sublevel": "sookshma-antardasha",
                        #"paryantardasha" : []   #contains array of paryantardasha planet entries
                        }
dashaStrings = []
dashaCodeLines = []

def clearDashaDetails():
    global dashaStrings
    global dashaCodeLines
    global vimshottariDasha
    global mahadashaPlanetEntry
    global antardashaPlanetEntry
    global paryantardashaPlanetEntry
    dashaStrings = []
    dashaCodeLines = []
    vimshottariDasha = []
    mahadashaPlanetEntry = {
                            "name": "",
                            "startDate": datetime(year=1, month=1, day=1, hour=0, minute=0, second=0),
                            "endDate": datetime(year=1, month=1, day=1, hour=0, minute=0, second=0),
                            "entryString": "",
                            "level": "mahadasha",
                            "sublevel": "antardasha",
                            "antardasha" : []   #contains array of Antardasha planet entries
                            }.copy()
    antardashaPlanetEntry = {
                            "name": "",
                            "startDate": datetime(year=1, month=1, day=1, hour=0, minute=0, second=0),
                            "endDate": datetime(year=1, month=1, day=1, hour=0, minute=0, second=0),
                            "entryString": "",
                            "level": "antardasha",
                            "sublevel": "paryantardasha",
                            "paryantardasha" : []   #contains array of paryantardasha planet entries
                            }.copy()
    paryantardashaPlanetEntry = {
                            "name": "",
                            "startDate": datetime(year=1, month=1, day=1, hour=0, minute=0, second=0),
                            "endDate": datetime(year=1, month=1, day=1, hour=0, minute=0, second=0),
                            "entryString": "",
                            "level": "paryantardasha",
                            "sublevel": "sookshma-antardasha",
                            #"paryantardasha" : []   #contains array of paryantardasha planet entries
                            }.copy()
    return
def computeVimshottariDasha(lngsecondsMoon, nakshatraLord, birthDate):
    global dashaStrings
    global dashaCodeLines
    global vimshottariDasha
    global mahadashaPlanetEntry
    global antardashaPlanetEntry
    global paryantardashaPlanetEntry
    idcnt = 0
    l_DashaStartDate = computeStartDate_FirstDashaLord(lngsecondsMoon, nakshatraLord, birthDate)
    #print(f'start date is :{l_DashaStartDate}')
    l_firstPlanet = nakshatraLord
    l_wholeDuration = relativedelta(years=120)  #whole vimshottari dasha is for 120 years
    #compute Vimshottari table
    res_mahadasha = computeSubPeriods(l_DashaStartDate, l_firstPlanet, l_wholeDuration, "Mahadasha", birthDate)
    
    for item in res_mahadasha:
        mahadashaPlanetEntry["name"] = item["name"]
        mahadashaPlanetEntry["startDate"] = item["startDate"]
        mahadashaPlanetEntry["endDate"] = item["endDate"]
        mahadashaPlanetEntry["entryString"] = item["entryString"]
        dashaStrings.append(f'Dasha: {item["entryString"]} iid={idcnt}, open=False')
        dashaCodeLines.append(f'tree.insert("", END, text = "{item["entryString"]}", iid={idcnt}, open=False)')
        dashaIdx = idcnt
        antar_pos = 0
        idcnt = idcnt + 1
        #for Antardasha
        l_DashaStartDate = item["startDate"]
        l_firstPlanet = item["name"]
        l_wholeDuration = item["endDate"] - item["startDate"]
        res_antardasha = computeSubPeriods(l_DashaStartDate, l_firstPlanet, l_wholeDuration, "Antardasha", birthDate)
        for item2 in res_antardasha:
            antardashaPlanetEntry["name"] = item2["name"]
            antardashaPlanetEntry["startDate"] = item2["startDate"]
            antardashaPlanetEntry["endDate"] = item2["endDate"]
            antardashaPlanetEntry["entryString"] = item2["entryString"]
            dashaStrings.append(f'  AntarDasha: {item2["entryString"]} iid={idcnt}, open=False')
            dashaCodeLines.append(f'tree.insert("", END, text = "{item2["entryString"]}", iid={idcnt}, open=False)')
            antardashaIdx = idcnt
            dashaCodeLines.append(f'tree.move({antardashaIdx}, {dashaIdx}, {antar_pos}) ')
            paryantar_pos = 0
            idcnt = idcnt + 1
            antar_pos = antar_pos + 1
            #for Paryantardasha
            l_DashaStartDate = item2["startDate"]
            l_firstPlanet = item2["name"]
            l_wholeDuration = item2["endDate"] - item2["startDate"]
            res_paryantardasha = computeSubPeriods(l_DashaStartDate, l_firstPlanet, l_wholeDuration, "Antardasha", birthDate)
            for item3 in res_paryantardasha:
                paryantardashaPlanetEntry["name"] = item3["name"]
                paryantardashaPlanetEntry["startDate"] = item3["startDate"]
                paryantardashaPlanetEntry["endDate"] = item3["endDate"]
                paryantardashaPlanetEntry["entryString"] = item3["entryString"]
                dashaStrings.append(f'\tParyantarDasha: {item3["entryString"]} iid={idcnt}, open=False')
                dashaCodeLines.append(f'tree.insert("", END, text = "{item3["entryString"]}", iid={idcnt}, open=False)')
                paryantardashaIdx = idcnt
                dashaCodeLines.append(f'tree.move({paryantardashaIdx}, {antardashaIdx}, {paryantar_pos}) ')
                paryantar_pos = paryantar_pos + 1
                idcnt = idcnt + 1
                antardashaPlanetEntry["paryantardasha"].append(item3.copy())

            mahadashaPlanetEntry["antardasha"].append(item2.copy())

        vimshottariDasha.append(mahadashaPlanetEntry.copy())
        #print(item["entryString"])
    return


#Takes the start date and time and starting planets and whole duration and computes a set
#the set of sub periods of planets in that duration like planet name, its start date, end date, duration and age
def computeSubPeriods(startdate,firstPlanet,wholeDuration, level, birthday):
    l_dashaStartDate = startdate
    l_dashaEndDate = l_dashaStartDate + wholeDuration
    l_120thpart = ((l_dashaEndDate - l_dashaStartDate)/120)
    l_focusplanet = firstPlanet
    l_planetStartDate = l_dashaStartDate
    l_SubPeriods = []
    l_planetEntry = {
                        "name": "",
                        "startDate": l_dashaStartDate,
                        "endDate": l_dashaEndDate,
                        "entryString": ""
                    }
    #print(f'{level}s under planet {firstPlanet}')
    for lplanetnum in range(9):   #for all nine planets
        l_planetDuration = (dashaVimshottariSkeleton[l_focusplanet]["duration"] * l_120thpart)
        l_planetEndDate = (l_planetStartDate + l_planetDuration)
        l_durDays = int(str(l_planetDuration).split("days")[0].strip())
        startAge = relativedelta(l_planetStartDate, birthday)
        endAge = relativedelta(l_planetEndDate, birthday)
        if((startAge.years <= 0) and (startAge.months <= 0) and (startAge.days <= 0)):
            startAge.years = 0
            startAge.months = 0
            startAge.days = 0
        if((endAge.years >= 0) and (endAge.months >= 0) and (endAge.days >= 0)):
            l_planetEntry["name"] = l_focusplanet
            l_planetEntry["startDate"] = l_planetStartDate
            l_planetEntry["endDate"] = l_planetEndDate
            l_planetEntry["entryString"] = f'{l_focusplanet} - ({str(l_planetStartDate)[:-4]}) to ({str(l_planetEndDate)[:-4]}) ({l_durDays} days) Age[({endAge.years}year {endAge.months}month {endAge.days}days)]'
            l_SubPeriods.append(l_planetEntry.copy())
            #print(f'{l_focusplanet} - ({l_planetStartDate}) to ({l_planetEndDate}) ({l_durDays} days) Age[({endAge.years}year {endAge.months}month{endAge.days}days)]')
        #setup needed for moving to next planet in chain
        l_planetStartDate = l_planetEndDate
        l_focusplanet = dashaVimshottariSkeleton[l_focusplanet]["next-dasha"]
    return(l_SubPeriods)

def Vimshottari(division):
    moonlngsec = (((signnum(division["planets"]["Moon"]["sign"])-1) * 30 * 3600) + 
                  ((division["planets"]["Moon"]["pos"]["deg"]) * 3600) + 
                  ((division["planets"]["Moon"]["pos"]["min"]) * 60) + 
                  (division["planets"]["Moon"]["pos"]["sec"]))

    nakshatraLord = division["planets"]["Moon"]["nak-ruler"]

    bdaytime = datetime(year=data.birthdata["DOB"]["year"], 
                        month=data.birthdata["DOB"]["month"], 
                        day=data.birthdata["DOB"]["day"], 
                        hour=data.birthdata["TOB"]["hour"], 
                        minute=data.birthdata["TOB"]["min"], 
                        second=data.birthdata["TOB"]["sec"])

    computeVimshottariDasha(moonlngsec, nakshatraLord, bdaytime)
    #print(vimshottariDasha)
    return

if __name__ == "__main__":
    moonlngsec = (((signnum(data.lagna_moon["sign"])-1) * 30 * 3600) + 
                  ((data.lagna_moon["pos"]["deg"]) * 3600) + 
                  ((data.lagna_moon["pos"]["min"]) * 60) + 
                  (data.lagna_moon["pos"]["sec"]))

    nakshatraLord = data.lagna_moon["nak-ruler"]

    bdaytime = datetime(year=data.birthdata["DOB"]["year"], 
                        month=data.birthdata["DOB"]["month"], 
                        day=data.birthdata["DOB"]["day"], 
                        hour=data.birthdata["TOB"]["hour"], 
                        minute=data.birthdata["TOB"]["min"], 
                        second=data.birthdata["TOB"]["sec"])

    starttime = datetime(year=1989, month=11, day=11, hour=13, minute=8, second=48)
    #duration = relativedelta(years=dashaVimshottariSkeleton["Mars"]["duration"])
    #print(f'Duration of 7 years is {duration}')
    computeVimshottariDasha(moonlngsec, nakshatraLord, bdaytime)
    print(vimshottariDasha)
    #res = computeSubPeriods(starttime, "Mars", duration, "Antardasha", bdaytime)
    #for item in res:
        #print(item["entryString"])
    #print(debilitationSign_of_planet)

