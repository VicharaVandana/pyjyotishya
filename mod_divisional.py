#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# mod_divisional.py -- module Divisional. All computations for Divisional chart [D2 to D60 chart - Total 15 divisional charts]
#
# Copyright (C) 2023 Shyam Bhat  <vicharavandana@gmail.com>
# Downloaded from "https://github.com/VicharaVandana/jyotishyam.git"
#
# This file is part of the "jyotishyam" Python library
# for computing Hindu jataka with sidereal lahiri ayanamsha technique 
# using swiss ephemeries
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import mod_astrodata as data
import mod_constants as c
import mod_general as gen
from mod_lagna import *

#Below function computes Navamsa longitude from lagna longitude
def navamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes navamsha position in sign and degree minute and seconds format only in tuple
    longi_sec = (((sign - 1) * 30 * 3600) +
                (pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = ((3 * 3600) + (20 * 60)) #one navamsa is 3 degree 20 minutes
    #check which navamsha does our planet falls in
    navSign = 1 + int(longi_sec/amsa) % 12
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 3deg20min so normalized is for 30deg
    navDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    navMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    navSec = round(longi_pending_sec_normalized,2)
    longi_nav_sec = (((navSign - 1) * 30 * 3600) +
                (navDeg * 3600) + (navMin * 60) + navSec)
    return(longi_nav_sec, navSign, navDeg, navMin, navSec)

#Below function computes Dasamsa longitude from lagna longitude
def dasamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes navamsha position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (3 * 3600) #one dasamsa is 3 degree 
    #check which dasamsa compartment does our planet falls in
    dasamsaCompartment = 1 + int(longi_sec/amsa) % 12
    #if lagna sign is even then dasamsa sign starts from 9th sign from lagna sign else from same sign
    if(sign % 2 == 0):  #even sign
        baseSign = gen.compute_nthsign(sign,9)
    else:
        baseSign = sign
    dasSign = gen.compute_nthsign(baseSign,dasamsaCompartment)
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 3deg20min so normalized is for 30deg
    dasDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    dasMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    dasSec = round(longi_pending_sec_normalized,2)
    longi_nav_sec = (((dasSign - 1) * 30 * 3600) +
                (dasDeg * 3600) + (dasMin * 60) + dasSec)
    return(longi_nav_sec, dasSign, dasDeg, dasMin, dasSec)

def prepDivisionalchartElements(division):
    #prepare Ascendant
    division["ascendant"] = {   "name"        : "Ascendant",
                                "symbol"       : "Asc",
                                "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
                                "nakshatra"    : "Ashwini" ,
                                "pada"         : 1,
                                "nak-ruler"    : "Ketu",
                                "nak-diety"    : "Ashwini kumaras",
                                "sign"         : "Aries",
                                "rashi"        : "Mesha",
                                "lagna-lord"   : "Mars",
                                "sign-tatva"   : c.FIRE,
                                "lagnesh-sign" : "Aries",
                                "lagnesh-rashi": "Mesha",
                                "lagnesh-disp" : "Mars",
                                "status"       : c.INIT
                                }.copy()
    division["planets"] = {}
    division["vargottamas"] = []    #only for non D1 divisional charts
    division["houses"] = []
    division["classifications"] = { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }.copy()
    division["planets"]["Sun"] = {  "name"         : "Sun",
                                    "symbol"       : "Su",
                                    "retro"        : 0,    #initialized retro as 0
                                    "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
                                    "nakshatra"    : "Ashwini" ,
                                    "pada"         : 1,
                                    "nak-ruler"    : "Ketu",
                                    "nak-diety"    : "Ashwini kumaras",
                                    "sign"         : "Aries",
                                    "rashi"        : "Mesha",
                                    "dispositor"   : "Mars",
                                    "tattva"       : c.FIRE,
                                    "sign-tatva"   : c.FIRE,
                                    "house-rel"    : c.EXHALTED,
                                    "house-nature" : c.DHARMA,
                                    "planet-nature": c.PAAPAGRAHA,
                                    "gender"       : c.MALE,
                                    "category"     : c.DEVA,
                                    "house-num"    : 1,
                                    "friends"      : ["Moon", "Mars", "Jupiter"],
                                    "enemies"      : ["Venus", "Saturn", "Rahu", "Ketu"],
                                    "nuetral"      : ["Mercury"],
                                    "varna"        : c.KSHATRIYA,
                                    "guna"         : c.SATVA,
                                    "Aspects"      : {"planets":[], "houses":[], "signs":[]},
                                    "Aspected-by"  : [],
                                    "conjuncts"    : [],
                                    "status"       : c.INIT
                                    }.copy()
    division["planets"]["Moon"] = {"name"         : "Moon",
             "symbol"       : "Mo",
             "retro"        : 0,    #initialized retro as 0
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.WATER,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.FRIENDSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PUNYAGRAHA,
             "gender"       : c.FEMALE,
             "category"     : c.DEVA,
             "house-num"    : 1,
             "friends"      : ["Sun", "Mercury"],
             "enemies"      : [],
             "nuetral"      : ["Mars", "Venus", "Jupiter", "Saturn", "Rahu", "Ketu"],
             "varna"        : c.VAISHYA,
             "guna"         : c.SATVA,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }.copy()
    division["planets"]["Mars"] = {"name"        : "Mars",
             "symbol"       : "Ma",
             "retro"        : 0,    #initialized retro as 0
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.FIRE,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.OWNSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PAAPAGRAHA,
             "gender"       : c.MALE,
             "category"     : c.DEVA,
             "house-num"    : 1,
             "friends"      : ["Sun", "Moon", "Jupiter"],
             "enemies"      : ["Mercury"],
             "nuetral"      : ["Saturn", "Venus", "Rahu", "Ketu"],
             "varna"        : c.KSHATRIYA,
             "guna"         : c.TAMAS,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }.copy()
    division["planets"]["Mercury"] = {"name"     : "Mercury",
             "symbol"       : "Me",
             "retro"        : 0,    #initialized retro as 0
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.EARTH,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.NEUTRALSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PAAPAGRAHA,
             "gender"       : c.NEUTER,
             "category"     : c.NEUTRAL,
             "house-num"    : 1,
             "friends"      : ["Sun", "Venus", "Rahu"],
             "enemies"      : ["Moon", "Ketu"],
             "nuetral"      : ["Saturn", "Mars", "Jupiter"],
             "varna"        : c.SHUDRA,
             "guna"         : c.RAJAS,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }.copy()
    division["planets"]["Jupiter"] = {"name"     : "Jupiter",
             "symbol"       : "Ju",
             "retro"        : 0,    #initialized retro as 0
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.FIRE,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.FRIENDSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PUNYAGRAHA,
             "gender"       : c.MALE,
             "category"     : c.DEVA,
             "house-num"    : 1,
             "friends"      : ["Moon", "Mars", "Sun", "Ketu"],
             "enemies"      : ["Venus", "Mercury", "Rahu"],
             "nuetral"      : ["Saturn"],
             "varna"        : c.BRAHMIN,
             "guna"         : c.SATVA,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }.copy()
    division["planets"]["Venus"] = {"name"       : "Venus",
             "symbol"       : "Ve",
             "retro"        : 0,    #initialized retro as 0
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.AIR,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.NEUTRALSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PUNYAGRAHA,
             "gender"       : c.FEMALE,
             "category"     : c.DANAVA,
             "house-num"    : 1,
             "friends"      : ["Saturn", "Mercury", "Rahu", "Ketu"],
             "enemies"      : ["Sun", "Moon"],
             "nuetral"      : ["Mars", "Jupiter"],
             "varna"        : c.BRAHMIN,
             "guna"         : c.RAJAS,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }.copy()
    division["planets"]["Saturn"] = {"name"      : "Saturn",
             "symbol"       : "Sa",
             "retro"        : 0,    #initialized retro as 0
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.AIR,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.DEBILITATED,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PAAPAGRAHA,
             "gender"       : c.FEMALE,
             "category"     : c.DANAVA,
             "house-num"    : 1,
             "friends"      : ["Venus", "Mercury", "Rahu", "Ketu"],
             "enemies"      : ["Sun", "Moon", "Mars"],
             "nuetral"      : ["Jupiter"],
             "varna"        : c.SHUDRA,
             "guna"         : c.TAMAS,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }.copy()
    division["planets"]["Rahu"] = {"name"        : "Rahu",
             "symbol"       : "Ra",
             "retro"        : 1,    #initialized retro as 1
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.AIR,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.OWNSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PAAPAGRAHA,
             "gender"       : c.MALE,
             "category"     : c.DANAVA,
             "house-num"    : 1,
             "friends"      : ["Venus", "Mercury", "Ketu", "Saturn"],
             "enemies"      : ["Sun", "Moon", "Mars"],
             "nuetral"      : ["Jupiter"],
             "varna"        : c.SHUDRA,
             "guna"         : c.TAMAS,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }.copy()
    division["planets"]["Ketu"] = {"name"        : "Ketu",
             "symbol"       : "Ke",
             "retro"        : 1,    #initialized retro as 1
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.AIR,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.OWNSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PAAPAGRAHA,
             "gender"       : c.FEMALE,
             "category"     : c.DANAVA,
             "house-num"    : 1,
             "friends"      : ["Venus", "Mercury", "Rahu", "Saturn"],
             "enemies"      : ["Sun", "Moon", "Mars"],
             "nuetral"      : ["Jupiter"],
             "varna"        : c.SHUDRA,
             "guna"         : c.TAMAS,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }.copy()
    return

#Takes charts as input. For ascendant and all 9 planets, computes Divisional chart.
#input D1 of Charts and updates DX of charts - All the fields (x can be any division like 9 for navamsa, 10 for dasamsa etc)
def compute_Dx_4m_D1(charts, Dx):
    l_D1 = charts["D1"]
    l_Dx = charts[Dx]
    prepDivisionalchartElements(l_Dx)
    
    #for computing Navamsa Lagna
    #Gather inputs
    D1lagnaSign = (gen.signnum(l_D1["ascendant"]["sign"]))
    D1lagnaPosDeg = (l_D1["ascendant"]["pos"]["deg"])
    D1lagnaPosMin = (l_D1["ascendant"]["pos"]["min"])
    D1lagnaPosSec = (l_D1["ascendant"]["pos"]["sec"])
    #compute Navamsa of Ascendant
    if(Dx == "D9"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = navamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D10"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = dasamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    else:
        div_fullLongi_sec = (((D1lagnaSign - 1) * 30 * 3600) +
                (D1lagnaPosDeg * 3600) + (D1lagnaPosMin * 60) + D1lagnaPosSec)
        (divSign, divDeg, divMin, divSec) = (D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)

    lagna = divSign
    #update Navamsa lagna in charts
    l_Dx["ascendant"]["sign"] = gen.signs[divSign-1]
    l_Dx["ascendant"]["pos"]["deg"] = divDeg
    l_Dx["ascendant"]["pos"]["min"] = divMin
    l_Dx["ascendant"]["pos"]["sec"] = divSec
    l_Dx["ascendant"]["pos"]["dec_deg"] = ((divDeg*3600) + (divMin*60) + divSec)/3600
    l_Dx["ascendant"]["rashi"]      = gen.rashis[divSign-1]
    l_Dx["ascendant"]["lagna-lord"] = gen.signlords[divSign-1]
    l_Dx["ascendant"]["sign-tatva"] = gen.signtatvas[divSign-1]

    #update nakshatra related data for ascendant
    nak_pad = nakshatra_pada(div_fullLongi_sec / 3600)  #argument must be full longitude in degrees
    l_Dx["ascendant"]["nakshatra"] = nak_pad[0]
    l_Dx["ascendant"]["pada"] = nak_pad[1]
    l_Dx["ascendant"]["nak-ruler"] = gen.ruler_of_nakshatra[nak_pad[0]]
    l_Dx["ascendant"]["nak-diety"] = gen.diety_of_nakshatra[nak_pad[0]]

    #update for every planet
    for planetname in l_Dx["planets"]:
        #Gather inputs
        D1PlanetSign = (gen.signnum(l_D1["planets"][planetname]["sign"]))
        D1PlanetPosDeg = (l_D1["planets"][planetname]["pos"]["deg"])
        D1PlanetPosMin = (l_D1["planets"][planetname]["pos"]["min"])
        D1PlanetPosSec = (l_D1["planets"][planetname]["pos"]["sec"])
        #compute Navamsa of Ascendant
        #(div_fullLongi_sec, divSign, divDeg, divMin, divSec) = navamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        if(Dx == "D9"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = navamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D10"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = dasamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        else:
            div_fullLongi_sec = (((D1PlanetSign - 1) * 30 * 3600) +
                    (D1PlanetPosDeg * 3600) + (D1PlanetPosMin * 60) + D1PlanetPosSec)
            (divSign, divDeg, divMin, divSec) = (D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)

        #Updating the attributes
        if(D1PlanetSign == divSign):
            l_Dx["vargottamas"].append(planetname)

        l_Dx["planets"][planetname]["retro"] = l_D1["planets"][planetname]["retro"]
        currentsign = gen.signs[divSign-1]
        l_Dx["planets"][planetname]["sign"] = currentsign
        l_Dx["planets"][planetname]["pos"]["deg"] = divDeg
        l_Dx["planets"][planetname]["pos"]["min"] = divMin
        l_Dx["planets"][planetname]["pos"]["sec"] = divSec
        l_Dx["planets"][planetname]["pos"]["dec_deg"] = ((divDeg*3600) + (divMin*60) + divSec)/3600
        l_Dx["planets"][planetname]["rashi"]      = gen.rashis[divSign-1]
        l_Dx["planets"][planetname]["sign-tatva"] = gen.signtatvas[divSign-1]
        dispositor = gen.signlords[divSign-1]
        l_Dx["planets"][planetname]["dispositor"] = dispositor
        l_Dx["planets"][planetname]["house-num"] = gen.housediff(lagna, divSign)
        #update nakshatra related data for ascendant
        nak_pad = nakshatra_pada(div_fullLongi_sec / 3600)  #argument must be full longitude in degrees
        l_Dx["planets"][planetname]["nakshatra"] = nak_pad[0]
        l_Dx["planets"][planetname]["pada"] = nak_pad[1]
        l_Dx["planets"][planetname]["nak-ruler"] = gen.ruler_of_nakshatra[nak_pad[0]]
        l_Dx["planets"][planetname]["nak-diety"] = gen.diety_of_nakshatra[nak_pad[0]]

        exhaltsign = gen.exhaltationSign_of_planet[planetname] 
        debilitsign = gen.debilitationSign_of_planet[planetname]
        friends = l_Dx["planets"][planetname]["friends"]
        enemies = l_Dx["planets"][planetname]["enemies"]
        neutral = l_Dx["planets"][planetname]["nuetral"]
        if(currentsign == exhaltsign):  #first check for exhaltation
            l_Dx["planets"][planetname]["house-rel"] = c.EXHALTED
        elif(currentsign == debilitsign): #next check for debilitated 
            l_Dx["planets"][planetname]["house-rel"] = c.DEBILITATED
        elif(planetname == dispositor): #next check for own sign 
            l_Dx["planets"][planetname]["house-rel"] = c.OWNSIGN
        elif(dispositor in friends): #next check for friend sign 
            l_Dx["planets"][planetname]["house-rel"] = c.FRIENDSIGN
        elif(dispositor in enemies): #next check for enemy sign 
            l_Dx["planets"][planetname]["house-rel"] = c.ENEMYSIGN
        elif(dispositor in neutral): #next check for neutral sign 
            l_Dx["planets"][planetname]["house-rel"] = c.NEUTRALSIGN
        else:
            l_Dx["planets"][planetname]["house-rel"] = "UNKNOWN"

    lagnesh = l_Dx["ascendant"]["lagna-lord"]  #get lagnesh
    l_Dx["ascendant"]["lagnesh-sign"]  = l_Dx["planets"][lagnesh]["sign"]  #check the sign of lagnesh
    l_Dx["ascendant"]["lagnesh-rashi"] = l_Dx["planets"][lagnesh]["rashi"] 
    l_Dx["ascendant"]["lagnesh-disp"]  = l_Dx["planets"][lagnesh]["dispositor"]
    
    #computing benefics, malefics and neutral planets for given lagna
    gen.compute_BenMalNeu4lagna(lagna,data.charts[Dx]["classifications"])

    gen.update_houses(data.charts[Dx])

    #computing aspects and conjunction planets
    gen.compute_aspects(data.charts[Dx])
    gen.compute_aspectedby(data.charts[Dx])  
    gen.compute_conjuncts(data.charts[Dx]) 

    #populating the classification part of divisional chart
    gen.populate_kendraplanets(data.charts[Dx]) #kendra planets
    gen.populate_trikonaplanets(data.charts[Dx]) #trikona planets
    gen.populate_trikplanets(data.charts[Dx]) #trik planets
    gen.populate_upachayaplanets(data.charts[Dx]) #upachaya planets
    gen.populate_dharmaplanets(data.charts[Dx]) #dharma planets
    gen.populate_arthaplanets(data.charts[Dx]) #artha planets
    gen.populate_kamaplanets(data.charts[Dx]) #kama planets
    gen.populate_mokshaplanets(data.charts[Dx]) #moksha planets


def compute_D9_4m_D1(charts):
    l_D1 = charts["D1"]
    l_D9 = charts["D9"]
    prepDivisionalchartElements(l_D9)
    
    #for computing Navamsa Lagna
    #Gather inputs
    D1lagnaSign = (gen.signnum(l_D1["ascendant"]["sign"]))
    D1lagnaPosDeg = (l_D1["ascendant"]["pos"]["deg"])
    D1lagnaPosMin = (l_D1["ascendant"]["pos"]["min"])
    D1lagnaPosSec = (l_D1["ascendant"]["pos"]["sec"])
    #compute Navamsa of Ascendant
    (nav_fullLongi_sec, navSign, navDeg, navMin, navSec) = navamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    lagna = navSign
    #update Navamsa lagna in charts
    l_D9["ascendant"]["sign"] = gen.signs[navSign-1]
    l_D9["ascendant"]["pos"]["deg"] = navDeg
    l_D9["ascendant"]["pos"]["min"] = navMin
    l_D9["ascendant"]["pos"]["sec"] = navSec
    l_D9["ascendant"]["pos"]["dec_deg"] = ((navDeg*3600) + (navMin*60) + navSec)/3600
    l_D9["ascendant"]["rashi"]      = gen.rashis[navSign-1]
    l_D9["ascendant"]["lagna-lord"] = gen.signlords[navSign-1]
    l_D9["ascendant"]["sign-tatva"] = gen.signtatvas[navSign-1]

    #update nakshatra related data for ascendant
    nak_pad = nakshatra_pada(nav_fullLongi_sec / 3600)  #argument must be full longitude in degrees
    l_D9["ascendant"]["nakshatra"] = nak_pad[0]
    l_D9["ascendant"]["pada"] = nak_pad[1]
    l_D9["ascendant"]["nak-ruler"] = gen.ruler_of_nakshatra[nak_pad[0]]
    l_D9["ascendant"]["nak-diety"] = gen.diety_of_nakshatra[nak_pad[0]]

    #update for every planet
    for planetname in l_D9["planets"]:
        #Gather inputs
        D1PlanetSign = (gen.signnum(l_D1["planets"][planetname]["sign"]))
        D1PlanetPosDeg = (l_D1["planets"][planetname]["pos"]["deg"])
        D1PlanetPosMin = (l_D1["planets"][planetname]["pos"]["min"])
        D1PlanetPosSec = (l_D1["planets"][planetname]["pos"]["sec"])
        #compute Navamsa of Ascendant
        (nav_fullLongi_sec, navSign, navDeg, navMin, navSec) = navamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        
        #Updating the attributes
        if(D1PlanetSign == navSign):
            l_D9["vargottamas"].append(planetname)

        l_D9["planets"][planetname]["retro"] = l_D1["planets"][planetname]["retro"]
        currentsign = gen.signs[navSign-1]
        l_D9["planets"][planetname]["sign"] = currentsign
        l_D9["planets"][planetname]["pos"]["deg"] = navDeg
        l_D9["planets"][planetname]["pos"]["min"] = navMin
        l_D9["planets"][planetname]["pos"]["sec"] = navSec
        l_D9["planets"][planetname]["pos"]["dec_deg"] = ((navDeg*3600) + (navMin*60) + navSec)/3600
        l_D9["planets"][planetname]["rashi"]      = gen.rashis[navSign-1]
        l_D9["planets"][planetname]["sign-tatva"] = gen.signtatvas[navSign-1]
        dispositor = gen.signlords[navSign-1]
        l_D9["planets"][planetname]["dispositor"] = dispositor
        l_D9["planets"][planetname]["house-num"] = gen.housediff(lagna, navSign)
        #update nakshatra related data for ascendant
        nak_pad = nakshatra_pada(nav_fullLongi_sec / 3600)  #argument must be full longitude in degrees
        l_D9["planets"][planetname]["nakshatra"] = nak_pad[0]
        l_D9["planets"][planetname]["pada"] = nak_pad[1]
        l_D9["planets"][planetname]["nak-ruler"] = gen.ruler_of_nakshatra[nak_pad[0]]
        l_D9["planets"][planetname]["nak-diety"] = gen.diety_of_nakshatra[nak_pad[0]]

        exhaltsign = gen.exhaltationSign_of_planet[planetname] 
        debilitsign = gen.debilitationSign_of_planet[planetname]
        friends = l_D9["planets"][planetname]["friends"]
        enemies = l_D9["planets"][planetname]["enemies"]
        neutral = l_D9["planets"][planetname]["nuetral"]
        if(currentsign == exhaltsign):  #first check for exhaltation
            l_D9["planets"][planetname]["house-rel"] = c.EXHALTED
        elif(currentsign == debilitsign): #next check for debilitated 
            l_D9["planets"][planetname]["house-rel"] = c.DEBILITATED
        elif(planetname == dispositor): #next check for own sign 
            l_D9["planets"][planetname]["house-rel"] = c.OWNSIGN
        elif(dispositor in friends): #next check for friend sign 
            l_D9["planets"][planetname]["house-rel"] = c.FRIENDSIGN
        elif(dispositor in enemies): #next check for enemy sign 
            l_D9["planets"][planetname]["house-rel"] = c.ENEMYSIGN
        elif(dispositor in neutral): #next check for neutral sign 
            l_D9["planets"][planetname]["house-rel"] = c.NEUTRALSIGN
        else:
            l_D9["planets"][planetname]["house-rel"] = "UNKNOWN"

    lagnesh = l_D9["ascendant"]["lagna-lord"]  #get lagnesh
    l_D9["ascendant"]["lagnesh-sign"]  = l_D9["planets"][lagnesh]["sign"]  #check the sign of lagnesh
    l_D9["ascendant"]["lagnesh-rashi"] = l_D9["planets"][lagnesh]["rashi"] 
    l_D9["ascendant"]["lagnesh-disp"]  = l_D9["planets"][lagnesh]["dispositor"]
    
    #computing benefics, malefics and neutral planets for given lagna
    gen.compute_BenMalNeu4lagna(lagna,data.D9["classifications"])

    gen.update_houses(data.D9)

    #computing aspects and conjunction planets
    gen.compute_aspects(data.D9)
    gen.compute_aspectedby(data.D9)  
    gen.compute_conjuncts(data.D9) 

    #populating the classification part of divisional chart
    gen.populate_kendraplanets(data.D9) #kendra planets
    gen.populate_trikonaplanets(data.D9) #trikona planets
    gen.populate_trikplanets(data.D9) #trik planets
    gen.populate_upachayaplanets(data.D9) #upachaya planets
    gen.populate_dharmaplanets(data.D9) #dharma planets
    gen.populate_arthaplanets(data.D9) #artha planets
    gen.populate_kamaplanets(data.D9) #kama planets
    gen.populate_mokshaplanets(data.D9) #moksha planets




if __name__ == "__main__":
      print(f'navamsha of Ketu is {dasamsa_from_long(3, 20, 33, 21.76)}')
