#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# mod_astrodata.py -- module Astro Data. All data computed for given birth details handled here.
#   charts [D1 to D60]
#   Dashas [Vimshottari etc]
#   Shadbala [And all six balkas individually]
#   basic details [Birth data, rashi, nakshatra, masa vaara, tithi etc]
# 
# Copyright (C) 2022 Shyam Bhat  <vicharavandana@gmail.com>
# Downloaded from "https://github.com/VicharaVandana/jyotishyam.git"
#
# This file is part of the "jyotishyam" Python library
# for computing Hindu jataka with sidereal lahiri ayanamsha technique 
# using swiss ephemeries
#

import mod_constants as c
#from mod_lagna import compute_lagnaChart as updatelagna
################ CHARTS ########################
##  Lagna Ascendant related data
###   LAGNA - ASCENDANT
lagna_ascendant = {"name"        : "Ascendant",
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
                  }
##  Lagna planets related data
###   LAGNA - SUN
lagna_sun = {"name"         : "Sun",
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
            }
###   LAGNA - MOON
lagna_moon = {"name"         : "Moon",
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
            }
###   LAGNA - MARS
lagna_mars = {"name"        : "Mars",
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
            }
###   LAGNA - MERCURY
lagna_mercury = {"name"     : "Mercury",
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
            }
###   LAGNA - JUPITER
lagna_jupiter = {"name"     : "Jupiter",
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
            }
###   LAGNA - VENUS
lagna_venus = {"name"       : "Venus",
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
            }
###   LAGNA - SATURN
lagna_saturn = {"name"      : "Saturn",
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
            }
###   LAGNA - RAHU
lagna_rahu = {"name"        : "Rahu",
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
            }
###   LAGNA - KETU
lagna_ketu = {"name"        : "Ketu",
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
            }
lagna_planets = {"Sun"      : lagna_sun,
                 "Moon"     : lagna_moon,
                 "Mars"     : lagna_mars,
                 "Mercury"  : lagna_mercury,
                 "Jupiter"  : lagna_jupiter,
                 "Venus"    : lagna_venus,
                 "Saturn"   : lagna_saturn,
                 "Rahu"     : lagna_rahu,
                 "Ketu"     : lagna_ketu
                 }
#charts consists of Divisional charts
D1 = {"name"            : "Lagna",
      "symbol"          : "D1",
      "ascendant"       : lagna_ascendant,
      "planets"         : lagna_planets,
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }



D9 = {"name"            : "Navamsa",
      "symbol"          : "D9",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D10 = {"name"            : "Dasamsa",
      "symbol"          : "D10",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D2 = {"name"            : "Hora",
      "symbol"          : "D2",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D3 = {"name"            : "Drekkana",
      "symbol"          : "D3",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D4 = {"name"            : "Chaturtamsa",
      "symbol"          : "D4",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D7 = {"name"            : "Saptamsa",
      "symbol"          : "D7",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D12 = {"name"            : "Dwadasamsa",
      "symbol"          : "D12",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D16 = {"name"            : "Shodasamsa",
      "symbol"          : "D16",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D20 = {"name"            : "Vimsamsa",
      "symbol"          : "D20",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D24 = {"name"            : "Chaturvimsamsa",
      "symbol"          : "D24",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D27 = {"name"            : "Saptavimsamsa",
      "symbol"          : "D27",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D30 = {"name"            : "Trimsamsa",
      "symbol"          : "D30",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D40 = {"name"            : "Khavedamsa",
      "symbol"          : "D40",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D45 = {"name"            : "Akshavedamsa",
      "symbol"          : "D45",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D60 = {"name"            : "Shashtiamsa",
      "symbol"          : "D60",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

isAstroDataComputed = False

charts = {"D1": D1,
          "D9": D9,
          "D10":D10,
          "D2":D2,
          "D3":D3,
          "D4":D4,
          "D7":D7,
          "D12":D12,
          "D16":D16,
          "D20":D20,
          "D24":D24,
          "D27":D27,
          "D30":D30,
          "D40":D40,
          "D45":D45,
          "D60":D60,
          "yogadoshas":[],
          "Balas":{"Vimshopaka":{ "shadvarga": {  "Sun": 0,
                                                  "Moon": 0,
                                                  "Mars": 0,
                                                  "Mercury": 0,
                                                  "Jupiter": 0,
                                                  "Venus": 0,
                                                  "Saturn": 0,
                                                  "Rahu": 0,
                                                  "Ketu": 0
                                                },
                                  "saptavarga": { "Sun": 0,
                                                  "Moon": 0,
                                                  "Mars": 0,
                                                  "Mercury": 0,
                                                  "Jupiter": 0,
                                                  "Venus": 0,
                                                  "Saturn": 0,
                                                  "Rahu": 0,
                                                  "Ketu": 0
                                                },
                                  "dashavarga": { "Sun": 0,
                                                  "Moon": 0,
                                                  "Mars": 0,
                                                  "Mercury": 0,
                                                  "Jupiter": 0,
                                                  "Venus": 0,
                                                  "Saturn": 0,
                                                  "Rahu": 0,
                                                  "Ketu": 0
                                                },
                                  "shodashavarga": { "Sun": 0,
                                                  "Moon": 0,
                                                  "Mars": 0,
                                                  "Mercury": 0,
                                                  "Jupiter": 0,
                                                  "Venus": 0,
                                                  "Saturn": 0,
                                                  "Rahu": 0,
                                                  "Ketu": 0
                                                },
                                },
"Shadbala": { "Total" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
              "Rupas" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
              "Sthanabala": { "Total" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Uchhabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Saptavargajabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Ojhayugmarashiamshabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Kendradhibala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Drekshanabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                            },
              "Digbala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
              "Kaalabala": { "Total" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Natonnatabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Pakshabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Tribhagabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Varsha-maasa-dina-horabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Yuddhabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Ayanabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                            },
              "Cheshtabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
              "Naisargikabala" : {"Sun": 60, "Moon": 51.4, "Mars": 17.1 , "Mercury": 25.7, "Jupiter": 34.3, "Venus": 42.9, "Saturn": 8.6},
              "Drikbala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0}
            },
"Ishtabala":{"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
"Kashtabala":{"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
"BhavaBala": {  "BhavaAdhipathibala" : [0,0,0,0,0,0,0,0,0,0,0,0],
                "BhavaDigbala" : [0,0,0,0,0,0,0,0,0,0,0,0],
                "BhavaDrishtibala" : [0,0,0,0,0,0,0,0,0,0,0,0],
                "Total" : [0,0,0,0,0,0,0,0,0,0,0,0]
},
                  },
          "Dashas":{ "Vimshottari":{  "mahadashas" : {},
                                      "antardashas": {},
                                      "paryantardashas": {},
                                      "current":{
                                                  "date": "",
                                                  "dasha": "",
                                                  "bhukti": "",
                                                  "paryantardasha": "",
                                                 }
                                    }
                    },
          "user_details" : {"name"  :"Shyam Bhat",
                            "maasa" :"",
                            "vaara" : "",
                            "tithi" : "",
                            "karana" : "",
                            "nakshatra" : "",
                            "yoga" : "",
                            "rashi" : "",
                            "rutu" : ""}
          }



############################################################################
##                   BIRTH DATA of CURRENT USER                           ##
############################################################################
birthdata = { "DOB"     : { "year"     : 1991,
                            "month"    : 10,
                            "day"      : 8
                          },
              "TOB"     : { "hour"     : 14,  #in 24 hour format
                            "min"      : 47,
                            "sec"      : 9
                          }, 
              "POB"     : { "name"     : "Honavar",
                            "lat"      : 15.4324,     #+ve for North and -ve for south
                            "lon"      : 75.6380,     #+ve for East and -ve for West
                            "timezone" : +5.5
                          },
              "name"    : "Shyam Bhat",
              "Gender"  : c.MALE,  
              "Comments": ""
            }
birthdatastr = { "DOB"  : { "year"     : "2020",
                            "month"    : "10",
                            "day"      : "31"
                          },
              "TOB"     : { "hour"     : "16",  #in 24 hour format
                            "min"      : "55",
                            "sec"      : "9"
                          }, 
              "POB"     : { "name"     : "Honavar",
                            "lat"      : "15.4324",     #+ve for North and -ve for south
                            "lon"      : "75.6380",     #+ve for East and -ve for West
                            "timezone" : "+5.5"
                          },
              "name"    : "Shyam Bhat",
              "Gender"  : c.MALE,  
              "Comments": "This is Birth data of creator of this software."
            }

            
birthdatas = {}
places = {}
yogadoshas = {}

def clearAstroData(charts):
  charts["D1"]["classifications"] = { "benefics"    : [],
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
  charts["D1"]["houses"] = []
  charts["yogadoshas"] = []

  for key in lagna_planets:
    lagna_planets[key]["Aspects"] = {"planets":[], "houses":[], "signs":[]}.copy()
    lagna_planets[key]["Aspected-by"] = []
    lagna_planets[key]["conjuncts"] = []


#if the striong is not a float then returns False. else returns the string as float number
def isfloat(num):
    try:
        float(num)
        return float(num)
    except ValueError:
        return False

#validate the birthdatastr contents are proper or not. If any error then report it. 
# If all fine then update birthdata
def validate_birthdatastr2birthdata():
    #check for name -> must be a non empty string
    l_name = birthdatastr["name"]
    if (len(l_name.strip()) == 0):
      return ("Name field cant be empty")
    #check for DOB:Year -> must be a number and less than 5000
    l_year = (birthdatastr["DOB"]["year"]).strip()
    if (len(l_year) == 0):
      return ("BirthYear field cant be empty")
    if (l_year.isnumeric() == False):
      return ("BirthYear field must have numerical value.")
    if (int(l_year) > 5000):
      return ("BirthYear field must in range of 0 to 5000 only.")
    #check for DOB:month -> must be a number and in range 1 to 12
    l_month = (birthdatastr["DOB"]["month"]).strip()
    if (len(l_month) == 0):
      return ("BirthMonth field cant be empty")
    if (l_month.isnumeric() == False):
      return ("BirthMonth field must have numerical value.")
    if ((int(l_month) < 1) or (int(l_month) > 12)):
      return ("BirthMonth field must in range of 1 to 12 only.")
    #check for DOB:day -> must be a number and  in range 1 to 31 -consideration of 30 days and leap year etc not done
    l_day = (birthdatastr["DOB"]["day"]).strip()
    if (len(l_day) == 0):
      return ("BirthDay field cant be empty")
    if (l_day.isnumeric() == False):
      return ("BirthDay field must have numerical value.")
    if ((int(l_day) < 1) or (int(l_day) > 31)):
      return ("BirthDay field must in range of 1 to 31 only.")
    #check for TOB:hour -> must be a number and in range 0 to 23
    l_hr = (birthdatastr["TOB"]["hour"]).strip()
    if (len(l_hr) == 0):
      return ("BirthHour field cant be empty")
    if (l_hr.isnumeric() == False):
      return ("BirthHour field must have numerical value.")
    if ((int(l_hr) < 0) or (int(l_hr) > 23)):
      return ("BirthHour field must in range of 0 to 23 only.")
    #check for TOB:minute -> must be a number and in range 0 to 59
    l_mn = (birthdatastr["TOB"]["min"]).strip()
    if (len(l_mn) == 0):
      return ("BirthMinute field cant be empty")
    if (l_mn.isnumeric() == False):
      return ("BirthMinute field must have numerical value.")
    if ((int(l_mn) < 0) or (int(l_mn) > 59)):
      return ("BirthMinute field must in range of 0 to 59 only.")
    #check for TOB:second -> must be a number and in range 0 to 59
    l_ss = (birthdatastr["TOB"]["sec"]).strip()
    if (len(l_ss) == 0):
      return ("BirthSecond field cant be empty")
    if (l_ss.isnumeric() == False):
      return ("BirthSecond field must have numerical value.")
    if ((int(l_ss) < 0) or (int(l_ss) > 59)):
      return ("BirthSecond field must in range of 0 to 59 only.")
    #check for POB:name -> must be a non empty string
    l_placename = birthdatastr["POB"]["name"]
    if (len(l_placename.strip()) == 0):
      return ("Place name field cant be empty")
    #check for POB:longitude -> must be a floatnumber 
    l_lonstr = (birthdatastr["POB"]["lon"]).strip()
    if (len(l_lonstr) == 0):
      return ("Longitude field cant be empty")
    l_lon = isfloat(l_lonstr) 
    if (l_lon == False):
      return ("Longitude field must be a number (+ve or -ve with or without decimal point)")
    #check for POB:lattitude -> must be a floatnumber 
    l_latstr = (birthdatastr["POB"]["lat"]).strip()
    if (len(l_latstr) == 0):
      return ("Lattitude field cant be empty")
    l_lat = isfloat(l_latstr) 
    if (l_lat == False):
      return ("Lattitude field must be a number (+ve or -ve with or without decimal point)")
    #check for POB:timezone -> must be a float number and divisible by 0.5
    l_tzstr = (birthdatastr["POB"]["timezone"]).strip()
    if (len(l_tzstr) == 0):
      return ("Timezone field cant be empty")
    l_tz = isfloat(l_tzstr) 
    if (l_tz == False):
      return ("Timezone field must be a number (+ve or -ve with or without decimal point)")
    if (((l_tz%0.5)==0) == False):
      return ("Timezone field must be in hour format with steps of 30 min (30 min would be 0.5 hours)")
    #check for Gender -> must be a non empty string
    l_gender = birthdatastr["Gender"]
    if (len(l_gender.strip()) == 0):
      return ("Gender field cant be empty")
    #All fields are proper. So update birthdata
    birthdata["name"] = l_name.strip()
    birthdata["Gender"] = l_gender.strip()
    birthdata["DOB"]["year"] = int(l_year)
    birthdata["DOB"]["month"] = int(l_month) 
    birthdata["DOB"]["day"] = int(l_day)
    birthdata["TOB"]["hour"] = int(l_hr)
    birthdata["TOB"]["min"] = int(l_mn)
    birthdata["TOB"]["sec"] = int(l_ss)
    birthdata["POB"]["name"] = l_placename.strip()
    birthdata["POB"]["lon"] = l_lon
    birthdata["POB"]["lat"] = l_lat
    birthdata["POB"]["timezone"] = l_tz
    return("SUCCESS")


if __name__ == "__main__":
      print(charts)
      