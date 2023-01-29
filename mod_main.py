#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# mod_main.py -- main module. All chart, vimshottari and bala calculations 
# are triggered from here
#
# Copyright (C) 2022 Shyam Bhat  <vicharavandana@gmail.com>
# Downloaded from "https://github.com/VicharaVandana/jyotishyam.git"
#
# This file is part of the "jyotishyam" Python library
# for computing Hindu jataka with sidereal lahiri ayanamsha technique 
# using swiss ephemeries
#

import mod_constants as c
import mod_lagna as mod_lagna
import mod_astrodata as data
import mod_json as js
import mod_drawChart as dc
import dashas
import dymmy as dummy

import json



def compute_astrodata_charts(focususer):
    data.birthdata = js.get_birthdata(focususer)
    #print(data.birthdata)
    mod_lagna.compute_lagnaChart_custom(data.birthdata)
    js.load_drawChartConfig()
    dc.create_chartSVG(data.D1)

def compute_astrodata_charts2():
    focususer = "shyam bhat"
    data.birthdata = js.get_birthdata(focususer)
    #print(data.birthdata)
    mod_lagna.compute_lagnaChart_custom(data.birthdata)
    js.load_drawChartConfig()
    dc.create_chartSVG(data.D1)

if __name__ == "__main__":
    #print(data.lagna_ascendant)
    #data.birthdata = js.get_birthdata("Shyam-Self")
    #mod_lagna.compute_lagnaChart()
    #print("Updated lagna")
    #print(data.lagna_ascendant)
    print("START")
    compute_astrodata_charts2()
    dashas.Vimshottari()
    f = open("./json/vimshottari.txt", "w")
    for item in dashas.dashaStrings:
        f.write(item)
        f.write("\n")
    f.close()

    f = open("vimshottaricode.txt", "w")
    for item in dashas.dashaCodeLines:
        f.write(item)
        f.write("\n")
    f.close()

    dummy.updatetable(dashas.dashaCodeLines)
    #with open('./json/vimshottari.json', 'w') as jsonfile:
        #json.dump((dashas.vimshottariDasha), jsonfile, indent=4)
    
    #js.load_places()
    #compute_astrodata_charts("Shyamu")
    #myplace = data.birthdata2["POB"]
    #myplaceid = myplace["name"].lower()
    #js.add_place2DB(myplace,myplaceid)
    #js.dump_placedatas_injson()
    #print(data.lagna_planets["Sun"])
    #print(data.D1["houses"])
    js.dump_astrodata_injson()
    #js.load_drawChartConfig()
    #dc.printconfig()
    #dc.create_chartSVG(data.D1)
    #js.load_birthdatas()
    #print(js.add_birthdata2DB(data.birthdata, "Deepa Bhat"))
    #print(data.birthdatas)
    #js.dump_birthdatas_injson()
    print("END")
    

