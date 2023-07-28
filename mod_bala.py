import mod_astrodata as data
import mod_general as gen
import mod_constants as c
import mod_graphplot as gp

rel2vimshopakratio = {  c.SWAYAM        : (20/20),
                        c.ATHIMITRA     : (18/20),
                        c.MITRA         : (15/20),
                        c.SAMA          : (10/20),
                        c.SHATRU        : (7/20),
                        c.ATHISHATRU    : (5/20)
                      }

vimshopak_divisionstrengths = { "shadvarga":{   "D1":6,
                                                "D2":2,
                                                "D3":4,
                                                "D9":5,
                                                "D12":2,
                                                "D30":1
                                            },
                                "saptavarga":{  "D1":5,
                                                "D2":2,
                                                "D3":3,
                                                "D7":2.5,
                                                "D9":4.5,
                                                "D12":2,
                                                "D30":1
                                            },
                                "dashavarga":{  "D1":3,
                                                "D2":1.5,
                                                "D3":1.5,
                                                "D7":1.5,
                                                "D9":1.5,
                                                "D10":1.5,
                                                "D12":1.5,
                                                "D16":1.5,
                                                "D30":1.5,
                                                "D60":5
                                            },
                                "shodashavarga":{   "D1":3.5,
                                                    "D2":1,
                                                    "D3":1,
                                                    "D4":0.5,
                                                    "D7":0.5,
                                                    "D9":3,
                                                    "D10":0.5,
                                                    "D12":0.5,
                                                    "D16":2,
                                                    "D20":0.5,
                                                    "D24":0.5,
                                                    "D27":0.5,
                                                    "D30":1,
                                                    "D40":0.5,
                                                    "D45":0.5,
                                                    "D60":4
                                                }
                               }

def get_PlanetaryDispositorRelation(planet, division, lagna):
    #Computes the relation of planet with its dispositor in the given divisional chart
    #outputs can be Swayam rashi, athimitra to athishatru
    dispositor = division["planets"][planet]["dispositor"]
    naturalfriends = lagna["planets"][planet]["friends"]
    naturalenemies = lagna["planets"][planet]["enemies"]
    naturalnuetrals = lagna["planets"][planet]["nuetral"]

    #Getting the natural friendship between planet and dispositor    
    if(dispositor == planet): #first check for own sign
      naturalrelation = "Swarashi"
      return(c.SWAYAM)
    elif(dispositor in naturalfriends): #next check for friend sign       
      naturalrelation = "Mitra"
      n_val = 1
    elif(dispositor in naturalenemies): #next check for enemy sign 
      naturalrelation = "Shatru"
      n_val = -1
    elif(dispositor in naturalnuetrals): #next check for neutral sign       
      naturalrelation = "Sama"
      n_val = 0
    else:
      naturalrelation = "UNKNOWN"
      n_val = 0

    #getting the temporary friendship between planet and dispositor
    temporaryrelation = ""
    planethouse = lagna["planets"][planet]["house-num"]
    dispositorhouse = lagna["planets"][dispositor]["house-num"]
    planet2disp = gen.housediff(planethouse,dispositorhouse)
    if((planet2disp == 2) or 
       (planet2disp == 3) or 
       (planet2disp == 4) or
       (planet2disp == 10) or
       (planet2disp == 11) or
       (planet2disp == 12)):
       temporaryrelation = "Mitra"
       t_val = 1
    else:
        temporaryrelation = "Shatru"
        t_val = -1
    
    final_val = n_val + t_val
    if (final_val == 2):
        return (c.ATHIMITRA)
    elif (final_val == 1):
        return (c.MITRA)
    elif (final_val == 0):
        return (c.SAMA)
    elif (final_val == -1):
        return (c.SHATRU)
    elif (final_val == -2):
        return (c.ATHISHATRU)
    else:
        print("Should not reach here while computing planet to dispositor relation")
        return (c.SAMA)


def compute_VimshopakaBalas():
    #this function computes vimshopaka balas for all varga levels for all 9 planets
    #and updates it in data structure Balas -> Vimshopaka
    for level in ["shadvarga", "saptavarga", "dashavarga", "shodashavarga"]:
        for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu"]:
            planet_vimshopakaBala = 0.0
            #for each planet go through each division
            for div in vimshopak_divisionstrengths[level]:
                planetDispositor_relationInDiv = get_PlanetaryDispositorRelation(planet, data.charts[div], data.charts["D1"])
                planetStrengthInDiv = rel2vimshopakratio[planetDispositor_relationInDiv]
                divisionWeightage = vimshopak_divisionstrengths[level][div]
                planet_vimshopakaBala = planet_vimshopakaBala + (planetStrengthInDiv * divisionWeightage)
            
            #Update the Vimshopaka Bala for the planet in given level
            data.charts["Balas"]["Vimshopaka"][level][planet] = round(planet_vimshopakaBala, 3)
    #Plot the graph and create image
    gp.barPlot(data.charts["Balas"]["Vimshopaka"],"VimshopakaBala", "Vimshopaka Bala of planets in various Varga-groups", "Planets", "Vimshopaka Bala")
    return



