#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# mod_drawChart.py -- module to Draw AstroCharts. - It creates the astrology charts in svg images. 
#
# Copyright (C) 2022 Shyam Bhat  <vicharavandana@gmail.com>
# Downloaded from "https://github.com/VicharaVandana/jyotishyam.git"
#
# This file is part of the "jyotishyam" Python library
# for computing Hindu jataka with sidereal lahiri ayanamsha technique 
# using swiss ephemeries
#

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from html2image import Html2Image
from scipy.stats import rankdata

from mod_chartPlanetPositions import planetPosition_northSquareClassic as ppnsc
from mod_chartPlanetPositions import bhavnames, aspectSymbols

chartCfg = {}   #contains all the configurations for drawing chart. Loaded from chartDraw_cfg.json file


def printconfig():
    print(chartCfg)
    return

def draw_classicNorthChartSkeleton(chartSVG):
    # Chart drawing section - Skeleton part for template - north-square-classic
    chartSVG.write(f'''  <rect width="410" height="410" x="5" y="5" style="fill:{chartCfg["background-colour"]};stroke-width:3;stroke:{chartCfg["outerbox-colour"]}" />\n''')
    chartSVG.write(f'''  <polygon id ="tanbhav" points="210,10 110,110 210,210 310,110" style="fill:{chartCfg["house-colour"]["tanbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="dhanbhav" points="10,10 210,10 110,110" style="fill:{chartCfg["house-colour"]["dhanbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="anujbhav" points="10,10 10,210 110,110" style="fill:{chartCfg["house-colour"]["anujbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="maatabhav" points="110,110 10,210 110,310 210,210" style="fill:{chartCfg["house-colour"]["maatabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="santanbhav" points="10,210 110,310 10,410" style="fill:{chartCfg["house-colour"]["santanbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="rogbhav" points="210,410 110,310 10,410" style="fill:{chartCfg["house-colour"]["rogbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="dampathyabhav" points="210,410 110,310 210,210 310,310" style="fill:{chartCfg["house-colour"]["dampathyabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="aayubhav" points="210,410 310,310 410,410" style="fill:{chartCfg["house-colour"]["aayubhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="bhagyabhav" points="310,310 410,410 410,210" style="fill:{chartCfg["house-colour"]["bhagyabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="karmabhav" points="310,310 410,210 310,110 210,210" style="fill:{chartCfg["house-colour"]["karmabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="laabbhav" points="410,210 310,110 410,10" style="fill:{chartCfg["house-colour"]["laabbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="karchbhav" points="310,110 410,10 210,10" style="fill:{chartCfg["house-colour"]["karchbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    return

def write_signnumOnChart_nsc(division, chartSVG, signclr):
    chartSVG.write('\n  <!-- ********** Sign Numbers ********** -->\n')
    chartSVG.write(f'''  <text id ="tan" x="193" y="195" fill="{signclr}" class="sign-num">{division["houses"][0]["sign-num"]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="dhan" x="97" y="95" fill="{signclr}" class="sign-num">{division["houses"][1]["sign-num"]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="anuj" x="70" y="118" fill="{signclr}" class="sign-num">{division["houses"][2]["sign-num"]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="maata" x="170" y="218" fill="{signclr}" class="sign-num">{division["houses"][3]["sign-num"]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="santaan" x="75" y="316" fill="{signclr}" class="sign-num">{division["houses"][4]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="rog" x="97" y="335" fill="{signclr}" class="sign-num">{division["houses"][5]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="dampathya" x="195" y="240" fill="{signclr}" class="sign-num">{division["houses"][6]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="aayu" x="296" y="337" fill="{signclr}" class="sign-num">{division["houses"][7]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="bhagya" x="320" y="318" fill="{signclr}" class="sign-num">{division["houses"][8]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="karma" x="220" y="218" fill="{signclr}" class="sign-num">{division["houses"][9]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="laab" x="318" y="118" fill="{signclr}" class="sign-num">{division["houses"][10]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="karch" x="298" y="98" fill="{signclr}" class="sign-num">{division["houses"][11]["sign-num"]:02}</text>\n''')
    return

def get_planetColour(planetname, classification):
    if(planetname in classification["benefics"]):
        #its a benefic planet for the chart. So make it benefic colour
        planetcolour = chartCfg["benefic-planet-colour"]
    elif(planetname in classification["malefics"]):
        #its a malefic planet for the chart. So make it malefic colour
        planetcolour = chartCfg["malefic-planet-colour"]
    elif(planetname in classification["neutral"]):
        #its a neutral planet for the chart. So make it neutral colour
        planetcolour = chartCfg["neutral-planet-colour"]
    else:
        #its not categorised. Control should not come here. So make it neutral colour
        #print(f'The planet {planetname} is not classified as either benefic or malefic or neutral. Fix it.')
        planetcolour = chartCfg["neutral-planet-colour"]
    return(planetcolour)

def write_planetsAspectsOnChart_nsc(division, chartSVG):
    chartSVG.write('\n  <!-- ********** Planets ********** -->\n')
    for houseIdx in range(0,12):    #for all houses
        chartSVG.write(f'  <!-- Aspects -->\n')
        for planetname in division["houses"][houseIdx]["aspect-planets"]:
            planetIdx = division["houses"][houseIdx]["aspect-planets"].index(planetname)
            #compute index of aspect position as planets present in house occupy first and aspects occupy next positions
            planetposIdx = planetIdx + len(division["houses"][houseIdx]["planets"])
            symbol = aspectSymbols[planetname]
            retro = division["planets"][planetname]["retro"]
            #identify the planet colour to be put in chart
            planetcolour = get_planetColour(planetname, division["classifications"])
            #Get planet position co-ordinates x and y on chart svg
            px = ppnsc[houseIdx][planetposIdx]["x"]
            py = ppnsc[houseIdx][planetposIdx]["y"]
            #Since all needed properties are computed, Now create the svg entry string for planet
            if(retro == True):
                Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" text-decoration="underline" class="planet">({symbol})</text>\n'''
            else:
                Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="planet">{symbol}</text>\n'''
            #write the planet to SVG chart
            chartSVG.write(Planet_SVGstring)
    return

def write_planetsOnChart_nsc(division, chartSVG):
    chartSVG.write('\n  <!-- ********** Planets ********** -->\n')
    for houseIdx in range(0,12):    #for all houses
        chartSVG.write(f'  <!-- {bhavnames[houseIdx]} -->\n')
        chartSVG.write(f'  <!-- Planet placements -->\n')
        for planetname in division["houses"][houseIdx]["planets"]:
            planetIdx = division["houses"][houseIdx]["planets"].index(planetname)
            symbol = division["planets"][planetname]["symbol"]
            retro = division["planets"][planetname]["retro"]
            #identify the planet colour to be put in chart
            planetcolour = get_planetColour(planetname, division["classifications"])
            #Get planet position co-ordinates x and y on chart svg
            px = ppnsc[houseIdx][planetIdx]["x"]
            py = ppnsc[houseIdx][planetIdx]["y"]
            #Since all needed properties are computed, Now create the svg entry string for planet
            if(retro == True):
                Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" text-decoration="underline" class="planet">({symbol})</text>\n'''
            else:
                Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="planet">{symbol}</text>\n'''
            #write the planet to SVG chart
            chartSVG.write(Planet_SVGstring)
    return

def create_chartSVG(division):
    ''' Creates SVG image of astrology chart as per the chart draw configuration
        with data in division. The divisional chart is mentioned by division and 
        hence named accordingly'''
    # open or create chart file 
    chartSVGfilename = f'{division["name"]}_chart'
    chartSVGFullname = f'images/{chartSVGfilename}.svg'
    chartSVG = open(chartSVGFullname, 'w',  encoding='utf-16')
    chartPNGFullname = f'images/{chartSVGfilename}.png'
    chartPNGShortname = f'{chartSVGfilename}.png'
    hti = Html2Image()

    #Write the content into the file
    #SVG chart open section
    chartSVG.write(f'''<svg id="{chartSVGfilename}" height="500" width="500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 420 420" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" charset="utf-16">\n''')
    chartSVG.write('  <style>\n')
    chartSVG.write('    .sign-num { font: bold 22px sans-serif; }\n')
    chartSVG.write('    .planet { font: bold 20px sans-serif; }\n')
    chartSVG.write('  </style>\n')
    chartSVG.write('  <!-- ********** Chart Diagram ********** -->\n')

    #create chart for given template
    if (chartCfg["template"] == "north-square-classic"):
        draw_classicNorthChartSkeleton(chartSVG)    #Create skeleton
        write_signnumOnChart_nsc(division, chartSVG, chartCfg["sign-colour"])    #Update the sign numbers on chart skeleton
        write_planetsOnChart_nsc(division, chartSVG)    #Update the planets on chart for every house
        if(chartCfg["aspect-visibility"] == True):
            write_planetsAspectsOnChart_nsc(division, chartSVG)
    
    #SVG chart End section
    chartSVG.write('\n  Sorry, your browser does not support inline SVG.\n')
    chartSVG.write('</svg>\n')

    #close the file
    chartSVG.close()

    #Convert Svg file to PNG file
    if(chartCfg["aspect-visibility"] == True):
        hti.output_path = './images/'
        hti.screenshot(other_file=chartSVGFullname, size=(500, 500), save_as=chartPNGShortname)
    else:
        drawing = svg2rlg(chartSVGFullname)
        renderPM.drawToFile(drawing, chartPNGFullname, fmt="PNG")

    return

##############################################################################################################

def write_relevantplanetsOnChart_nsc(division, chartSVG, relevantPlanets):
    chartSVG.write('\n  <!-- ********** Planets ********** -->\n')
    for houseIdx in range(0,12):    #for all houses
        chartSVG.write(f'  <!-- {bhavnames[houseIdx]} -->\n')
        chartSVG.write(f'  <!-- Planet placements -->\n')
        for planetname in division["houses"][houseIdx]["planets"]:
            planetIdx = division["houses"][houseIdx]["planets"].index(planetname)
            symbol = division["planets"][planetname]["symbol"]
            retro = division["planets"][planetname]["retro"]

            #Write the planet only if it is relevant
            if symbol in relevantPlanets:
                #identify the planet colour to be put in chart
                planetcolour = chartCfg["neutral-planet-colour"]
                #Get planet position co-ordinates x and y on chart svg
                px = ppnsc[houseIdx][planetIdx]["x"]
                py = ppnsc[houseIdx][planetIdx]["y"]
                #Since all needed properties are computed, Now create the svg entry string for planet
                if(retro == True):
                    Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" text-decoration="underline" class="planet">({symbol})</text>\n'''
                else:
                    Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="planet">{symbol}</text>\n'''
                #write the planet to SVG chart
                chartSVG.write(Planet_SVGstring)
    return

def write_signnumOnChart_customcolour_nsc(division, chartSVG, colorlist):
    chartSVG.write('\n  <!-- ********** Sign Numbers ********** -->\n')
    chartSVG.write(f'''  <text id ="tan" x="193" y="195" fill="{colorlist[0]}" class="sign-num">{division["houses"][0]["sign-num"]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="dhan" x="97" y="95" fill="{colorlist[1]}" class="sign-num">{division["houses"][1]["sign-num"]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="anuj" x="70" y="118" fill="{colorlist[2]}" class="sign-num">{division["houses"][2]["sign-num"]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="maata" x="170" y="218" fill="{colorlist[3]}" class="sign-num">{division["houses"][3]["sign-num"]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="santaan" x="75" y="316" fill="{colorlist[4]}" class="sign-num">{division["houses"][4]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="rog" x="97" y="335" fill="{colorlist[5]}" class="sign-num">{division["houses"][5]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="dampathya" x="195" y="240" fill="{colorlist[6]}" class="sign-num">{division["houses"][6]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="aayu" x="296" y="337" fill="{colorlist[7]}" class="sign-num">{division["houses"][7]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="bhagya" x="320" y="318" fill="{colorlist[8]}" class="sign-num">{division["houses"][8]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="karma" x="220" y="218" fill="{colorlist[9]}" class="sign-num">{division["houses"][9]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="laab" x="318" y="118" fill="{colorlist[10]}" class="sign-num">{division["houses"][10]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="karch" x="298" y="98" fill="{colorlist[11]}" class="sign-num">{division["houses"][11]["sign-num"]:02}</text>\n''')
    return

def create_SimpleYogaDoshaChart(division,YogaDoshaName, relevantPlanets, colorlist):
    ''' Creates SVG image of astrology chart as per the chart draw configuration
        with data in division specific for That yoga or dosha. '''
    # open or create chart file 
    chartSVGfilename = f'{YogaDoshaName}_chart'
    chartSVGFullname = f'images/yogaImages/{chartSVGfilename}.svg'
    chartSVG = open(chartSVGFullname, 'w',  encoding='utf-16')
    chartPNGFullname = f'images/yogaImages/{chartSVGfilename}.png'
    chartPNGShortname = f'{chartSVGfilename}.png'
    hti = Html2Image()

    #Write the content into the file
    #SVG chart open section
    chartSVG.write(f'''<svg id="{chartSVGfilename}" height="500" width="500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 420 420" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" charset="utf-16">\n''')
    chartSVG.write('  <style>\n')
    chartSVG.write('    .sign-num { font: bold 22px sans-serif; }\n')
    chartSVG.write('    .planet { font: bold 20px sans-serif; }\n')
    chartSVG.write('  </style>\n')
    chartSVG.write('  <!-- ********** Chart Diagram ********** -->\n')

    #create chart for given template
    if (chartCfg["template"] == "north-square-classic"):
        draw_classicNorthChartSkeleton(chartSVG)    #Create skeleton
        write_signnumOnChart_customcolour_nsc(division, chartSVG, colorlist)    #Update the sign numbers on chart skeleton
        write_relevantplanetsOnChart_nsc(division, chartSVG, relevantPlanets)    #Update the planets on chart for every house
        #if(chartCfg["aspect-visibility"] == True):
            #write_planetsAspectsOnChart_nsc(division, chartSVG)
    
    #SVG chart End section
    chartSVG.write('\n  Sorry, your browser does not support inline SVG.\n')
    chartSVG.write('</svg>\n')

    #close the file
    chartSVG.close()

    #Convert Svg file to PNG file
    if(chartCfg["aspect-visibility"] == True):
        hti.output_path = './images/yogaImages/'
        hti.screenshot(other_file=chartSVGFullname, size=(500, 500), save_as=chartPNGShortname)
    else:
        drawing = svg2rlg(chartSVGFullname)
        renderPM.drawToFile(drawing, chartPNGFullname, fmt="PNG")
    return

########################## Bhavabala Charts #####################################
def write_bhavaBalasOnChart_nsc(charts, chartSVG):
    bhavbalas = []
    for bala in charts["Balas"]["BhavaBala"]["Total"]:
        bhavbalas.append(int(bala))

    
    chartSVG.write('\n  <!-- ********** Bhavabala Numbers ********** -->\n')
    chartSVG.write(f'''  <text id ="tanEntry" x="187" y="115" fill="lime" class="center-text">{bhavbalas[0]}</text>
  <text id ="dhanEntry" x="90" y="60" fill="lime" class="center-text">{bhavbalas[1]}</text>
  <text id ="anujEntry" x="22" y="120" fill="lime" class="center-text">{bhavbalas[2]}</text>
  <text id ="maataEntry" x="90" y="218" fill="lime" class="center-text">{bhavbalas[3]}</text>
  <text id ="santaanEntry" x="22" y="320" fill="lime" class="center-text">{bhavbalas[4]}</text>
  <text id ="rogEntry" x="95" y="380" fill="lime" class="center-text">{bhavbalas[5]}</text>
  <text id ="dampathyaEntry" x="195" y="310" fill="lime" class="center-text">{bhavbalas[6]}</text>
  <text id ="aayuEntry" x="290" y="380" fill="lime" class="center-text">{bhavbalas[7]}</text>
  <text id ="bhagyaEntry" x="355" y="320" fill="lime" class="center-text">{bhavbalas[8]}</text>
  <text id ="karmaEntry" x="290" y="220" fill="lime" class="center-text">{bhavbalas[9]}</text>
  <text id ="laabEntry" x="355" y="120" fill="lime" class="center-text">{bhavbalas[10]}</text>
  <text id ="karchEntry" x="287" y="60" fill="lime" class="center-text">{bhavbalas[11]}</text>\n''')
    return

def create_bhavaBalaChartSVG(charts):
    ''' Creates SVG image of astrology chart as per the chart draw configuration
        with data in division. The chart is bhavabala chart 
        with sign numbers and bhavabala in middle'''
    # open or create chart file 
    chartSVGfilename = f'Bhavabala_chart'
    chartSVGFullname = f'images/balaImages/{chartSVGfilename}.svg'
    chartSVG = open(chartSVGFullname, 'w',  encoding='utf-16')
    chartPNGFullname = f'images/balaImages/{chartSVGfilename}.png'
    chartPNGShortname = f'{chartSVGfilename}.png'
    hti = Html2Image()

    #Write the content into the file
    #SVG chart open section
    chartSVG.write(f'''<svg id="Bhavabala_chart" height="410" width="410" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 420 420" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" charset="utf-16">\n''')
    chartSVG.write('  <style>\n')
    chartSVG.write('    .sign-num { font: bold 22px sans-serif; }\n')
    chartSVG.write('    .center-text { font: bold 26px sans-serif; }\n')
    chartSVG.write('    .planet { font: bold 20px sans-serif; }\n')
    chartSVG.write('  </style>\n')
    chartSVG.write('  <!-- ********** Chart Diagram ********** -->\n')

    #create chart for given template
    if (chartCfg["template"] == "north-square-classic"):
        draw_classicNorthChartSkeleton(chartSVG)    #Create skeleton
        write_signnumOnChart_nsc(charts["D1"], chartSVG, "white")    #Update the sign numbers on chart skeleton
        write_bhavaBalasOnChart_nsc(charts, chartSVG)    #Update the planets on chart for every house
    
    #SVG chart End section
    chartSVG.write('\n  Sorry, your browser does not support inline SVG.\n')
    chartSVG.write('</svg>\n')

    #close the file
    chartSVG.close()

    #Convert Svg file to PNG file
    if(chartCfg["aspect-visibility"] == True):
        hti.output_path = './images/balaImages/'
        hti.screenshot(other_file=chartSVGFullname, size=(500, 500), save_as=chartPNGShortname)
    else:
        drawing = svg2rlg(chartSVGFullname)
        renderPM.drawToFile(drawing, chartPNGFullname, fmt="PNG")

    return

def write_bhavaBalasRankOnChart_nsc(charts, chartSVG):
    bhavbalas = charts["Balas"]["BhavaBala"]["Total"].copy()
    rankorderofbhavabalas = rankdata(bhavbalas, method='dense')
    maxrank = max(rankorderofbhavabalas)
    bhavabalarank = [(maxrank+1)-x for x in rankorderofbhavabalas]  
    
    chartSVG.write('\n  <!-- ********** Bhavabala Rank Numbers ********** -->\n')
    chartSVG.write(f'''  <text id ="tanEntry" x="187" y="115" fill="skyblue" class="center-text">{bhavabalarank[0]}</text>
  <text id ="dhanEntry" x="90" y="60" fill="skyblue" class="center-text">{bhavabalarank[1]}</text>
  <text id ="anujEntry" x="22" y="120" fill="skyblue" class="center-text">{bhavabalarank[2]}</text>
  <text id ="maataEntry" x="90" y="218" fill="skyblue" class="center-text">{bhavabalarank[3]}</text>
  <text id ="santaanEntry" x="22" y="320" fill="skyblue" class="center-text">{bhavabalarank[4]}</text>
  <text id ="rogEntry" x="95" y="380" fill="skyblue" class="center-text">{bhavabalarank[5]}</text>
  <text id ="dampathyaEntry" x="195" y="310" fill="skyblue" class="center-text">{bhavabalarank[6]}</text>
  <text id ="aayuEntry" x="290" y="380" fill="skyblue" class="center-text">{bhavabalarank[7]}</text>
  <text id ="bhagyaEntry" x="355" y="320" fill="skyblue" class="center-text">{bhavabalarank[8]}</text>
  <text id ="karmaEntry" x="290" y="220" fill="skyblue" class="center-text">{bhavabalarank[9]}</text>
  <text id ="laabEntry" x="355" y="120" fill="skyblue" class="center-text">{bhavabalarank[10]}</text>
  <text id ="karchEntry" x="287" y="60" fill="skyblue" class="center-text">{bhavabalarank[11]}</text>\n''')
    return

def create_bhavaBalaRankChartSVG(charts):
    ''' Creates SVG image of astrology chart as per the chart draw configuration
        with data in division. The chart is bhavabala chart 
        with sign numbers and bhavabala in middle'''
    # open or create chart file 
    chartSVGfilename = f'BhavabalaRank_chart'
    chartSVGFullname = f'images/balaImages/{chartSVGfilename}.svg'
    chartSVG = open(chartSVGFullname, 'w',  encoding='utf-16')
    chartPNGFullname = f'images/balaImages/{chartSVGfilename}.png'
    chartPNGShortname = f'{chartSVGfilename}.png'
    hti = Html2Image()

    #Write the content into the file
    #SVG chart open section
    chartSVG.write(f'''<svg id="Bhavabala_chart" height="410" width="410" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 420 420" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" charset="utf-16">\n''')
    chartSVG.write('  <style>\n')
    chartSVG.write('    .sign-num { font: bold 22px sans-serif; }\n')
    chartSVG.write('    .center-text { font: bold 38px sans-serif; }\n')
    chartSVG.write('    .planet { font: bold 20px sans-serif; }\n')
    chartSVG.write('  </style>\n')
    chartSVG.write('  <!-- ********** Chart Diagram ********** -->\n')

    #create chart for given template
    if (chartCfg["template"] == "north-square-classic"):
        draw_classicNorthChartSkeleton(chartSVG)    #Create skeleton
        write_signnumOnChart_nsc(charts["D1"], chartSVG, "white")    #Update the sign numbers on chart skeleton
        write_bhavaBalasRankOnChart_nsc(charts, chartSVG)    #Update the bhavabala ranks
    
    #SVG chart End section
    chartSVG.write('\n  Sorry, your browser does not support inline SVG.\n')
    chartSVG.write('</svg>\n')

    #close the file
    chartSVG.close()

    #Convert Svg file to PNG file
    if(chartCfg["aspect-visibility"] == True):
        hti.output_path = './images/balaImages/'
        hti.screenshot(other_file=chartSVGFullname, size=(500, 500), save_as=chartPNGShortname)
    else:
        drawing = svg2rlg(chartSVGFullname)
        renderPM.drawToFile(drawing, chartPNGFullname, fmt="PNG")

    return

############################## AshtakaVarga Charts #############################
def write_AshtakaVargaPointsOnChart_nsc(chartSVG, planetashtaka):     
    
    chartSVG.write('\n  <!-- ********** AshtakaVarga Points ********** -->\n')
    chartSVG.write(f'''  <text id ="tanEntry" x="187" y="115" fill="skyblue" class="center-text">{planetashtaka[0]}</text>
  <text id ="dhanEntry" x="90" y="60" fill="skyblue" class="center-text">{planetashtaka[1]}</text>
  <text id ="anujEntry" x="22" y="120" fill="skyblue" class="center-text">{planetashtaka[2]}</text>
  <text id ="maataEntry" x="90" y="218" fill="skyblue" class="center-text">{planetashtaka[3]}</text>
  <text id ="santaanEntry" x="22" y="320" fill="skyblue" class="center-text">{planetashtaka[4]}</text>
  <text id ="rogEntry" x="95" y="380" fill="skyblue" class="center-text">{planetashtaka[5]}</text>
  <text id ="dampathyaEntry" x="195" y="310" fill="skyblue" class="center-text">{planetashtaka[6]}</text>
  <text id ="aayuEntry" x="290" y="380" fill="skyblue" class="center-text">{planetashtaka[7]}</text>
  <text id ="bhagyaEntry" x="355" y="320" fill="skyblue" class="center-text">{planetashtaka[8]}</text>
  <text id ="karmaEntry" x="290" y="220" fill="skyblue" class="center-text">{planetashtaka[9]}</text>
  <text id ="laabEntry" x="355" y="120" fill="skyblue" class="center-text">{planetashtaka[10]}</text>
  <text id ="karchEntry" x="287" y="60" fill="skyblue" class="center-text">{planetashtaka[11]}</text>\n''')
    return

def create_ashtakavargaChartSVG(charts):
    ashtaka = charts["AshtakaVarga"]
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        # open or create chart file 
        chartSVGfilename = f'BAV_{planet}_chart'
        chartSVGFullname = f'images/ashtakavargaImages/{chartSVGfilename}.svg'
        chartSVG = open(chartSVGFullname, 'w',  encoding='utf-16')
        chartPNGFullname = f'images/ashtakavargaImages/{chartSVGfilename}.png'
        chartPNGShortname = f'{chartSVGfilename}.png'
        hti = Html2Image()

        #Write the content into the file
        #SVG chart open section
        chartSVG.write(f'''<svg id="BhinnaAshtakaVarga_chart" height="500" width="500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 420 420" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" charset="utf-16">\n''')
        chartSVG.write('  <style>\n')
        chartSVG.write('    .sign-num { font: bold 22px sans-serif; }\n')
        chartSVG.write('    .center-text { font: bold 38px sans-serif; }\n')
        chartSVG.write('    .planet { font: bold 20px sans-serif; }\n')
        chartSVG.write('  </style>\n')
        chartSVG.write('  <!-- ********** Chart Diagram ********** -->\n')

        #create chart for given template
        if (chartCfg["template"] == "north-square-classic"):
            draw_classicNorthChartSkeleton(chartSVG)    #Create skeleton
            colorlist = ["white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white"]
            planet_hno = charts["D1"]["planets"][planet]["house-num"]
            colorlist[planet_hno-1] = "yellow"
            write_signnumOnChart_customcolour_nsc(charts["D1"], chartSVG, colorlist)    #Update the sign numbers on chart skeleton
            write_AshtakaVargaPointsOnChart_nsc(chartSVG, ashtaka[planet])    #Update the ashtakavarga points
        
        #SVG chart End section
        chartSVG.write('\n  Sorry, your browser does not support inline SVG.\n')
        chartSVG.write('</svg>\n')

        #close the file
        chartSVG.close()

        #Convert Svg file to PNG file
        if(chartCfg["aspect-visibility"] == True):
            hti.output_path = './images/ashtakavargaImages/'
            hti.screenshot(other_file=chartSVGFullname, size=(500, 500), save_as=chartPNGShortname)
        else:
            drawing = svg2rlg(chartSVGFullname)
            renderPM.drawToFile(drawing, chartPNGFullname, fmt="PNG")
    ######## FOR Sarva AshtakaVarga ##################
    # open or create chart file 
    chartSVGfilename = f'SAV_chart'
    chartSVGFullname = f'images/ashtakavargaImages/{chartSVGfilename}.svg'
    chartSVG = open(chartSVGFullname, 'w',  encoding='utf-16')
    chartPNGFullname = f'images/ashtakavargaImages/{chartSVGfilename}.png'
    chartPNGShortname = f'{chartSVGfilename}.png'
    hti = Html2Image()

    #Write the content into the file
    #SVG chart open section
    chartSVG.write(f'''<svg id="SarvaAshtakaVarga_chart" height="500" width="500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 420 420" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" charset="utf-16">\n''')
    chartSVG.write('  <style>\n')
    chartSVG.write('    .sign-num { font: bold 22px sans-serif; }\n')
    chartSVG.write('    .center-text { font: bold 38px sans-serif; }\n')
    chartSVG.write('    .planet { font: bold 20px sans-serif; }\n')
    chartSVG.write('  </style>\n')
    chartSVG.write('  <!-- ********** Chart Diagram ********** -->\n')

    #create chart for given template
    if (chartCfg["template"] == "north-square-classic"):
        draw_classicNorthChartSkeleton(chartSVG)    #Create skeleton
        colorlist = ["white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white"]
        #planet_hno = charts["D1"]["planets"][planet]["house-num"]
        #colorlist[planet_hno-1] = "yellow"
        write_signnumOnChart_customcolour_nsc(charts["D1"], chartSVG, colorlist)    #Update the sign numbers on chart skeleton
        write_AshtakaVargaPointsOnChart_nsc(chartSVG, ashtaka["Total"])    #Update the ashtakavarga points
    
    #SVG chart End section
    chartSVG.write('\n  Sorry, your browser does not support inline SVG.\n')
    chartSVG.write('</svg>\n')

    #close the file
    chartSVG.close()

    #Convert Svg file to PNG file
    if(chartCfg["aspect-visibility"] == True):
        hti.output_path = './images/ashtakavargaImages/'
        hti.screenshot(other_file=chartSVGFullname, size=(500, 500), save_as=chartPNGShortname)
    else:
        drawing = svg2rlg(chartSVGFullname)
        renderPM.drawToFile(drawing, chartPNGFullname, fmt="PNG")




    return