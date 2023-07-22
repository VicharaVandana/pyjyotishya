
#imports
import mod_json as js
import mod_astrodata as data
import mod_constants as c
import mod_general as gen
import mod_drawChart as dc




#Function definitions
#function to check for Sasa Panchamahapurusha yoga - Saturn
def SasaYoga(charts):
    IsSasaYogaPresent = False   #initially assume the yoga is not present
    Rule = ""
    Results = ""
    Note = ""
    #two conditions for Sasa yoga to be present
        #cond1 -> Saturn must be in own rashi (Capricorn or Aquarius) OR Saturn must be exhalted(Libra)
        #cond2 -> Saturn must be in Kendra (either from ascendant or from moon)

    #check for Sasa yoga with lagna D1 chart
    lagnasaturn = charts["D1"]["planets"]["Saturn"]
    lagnamoon = charts["D1"]["planets"]["Moon"]

    #For condition 1
    lagna_cond1_exhaltation = False
    lagna_cond1_swarashi = False
    if(lagnasaturn["sign"] == "Libra"):
        lagna_cond1_exhaltation = True
        Rule = Rule + "In Lagna chart, Saturn is exhalted [Libra]"
    elif (lagnasaturn["sign"] == "Capricorn"):
        lagna_cond1_swarashi = True
        Rule = Rule + f'In Lagna chart, Saturn is in Own sign [Capricorn]'
    elif (lagnasaturn["sign"] == "Aquarius"):
        lagna_cond1_swarashi = True
        Rule = Rule + f'In Lagna chart, Saturn is in Own sign [Aquarius]'
    else:
        lagna_cond1_exhaltation = False
        lagna_cond1_swarashi = False
    lagna_cond1 = lagna_cond1_exhaltation or lagna_cond1_swarashi

    #For condition 2
    lagna_cond2_4mAsc = False
    lagna_cond2_4mMoon = False
    #check for Sasa yoga kendra condition from ascendant
    kendranum_4mlagna = lagnasaturn["house-num"]
    if((kendranum_4mlagna % 3) == 1):
        lagna_cond2_4mAsc = True
        Rule = Rule + f' and in Kendra [house number:{lagnasaturn["house-num"]}]'
    else:
        lagna_cond2_4mAsc = False

    #check for Sasa yoga kendra condition from moon
    kendranum_4mmoon = gen.housediff(lagnamoon["house-num"], lagnasaturn["house-num"])
    if((kendranum_4mmoon % 3) == 1):
        lagna_cond2_4mMoon = True
        Rule = Rule + f' and in Kendra with respect to Moon [house number:{kendranum_4mmoon} from moon]'
    else:
        lagna_cond2_4mMoon = False

    lagna_cond2 = lagna_cond2_4mAsc or lagna_cond2_4mMoon
    IsSasaYogaPresent = lagna_cond1 and lagna_cond2

    #detection part of yoga is over. Now if present then update the other details
    if(IsSasaYogaPresent == True):
        #finish the rule. 
        Rule = Rule + f' Hence Sasa Panchamahapurusha yoga is formed.'

        #Update the results
        Results = f'''Sasa Yoga makes the native practical, realistic, responsible and hardworking. They also develop exceptional mass communication skills and bear an air of authority. Embracing the effects of Saturn wholeheartedly is said to be the mark of a successful person. Saturn can bless people under Sasa Yoga with exceptional abilities to produce positive results.
        Persons with Sasa Yoga in their kundali are well placed in society, often in senior bureaucratic positions. They possess superlative intelligence and leadership qualities. The financial benefits are many; they are blessed with every creature comfort known to man. The effects Sasa yoga may become more pronounced as one grows in years when it is time for the hard work to pay off.
        Natives with Sasa Yoga in their horoscope will be elevated to positions of power. They will enjoy success and riches, and their fame will spread far and wide. They are pragmatic by nature. They are hardworking, conscientious and self-made.
        The native is blessed with the good qualities of Saturn. They are devoted to their mothers and often engage in charitable activities.
        Sasa Yoga enables the natives to draw benefits from spiritualism and meditation. Such people have heightened intuition and can become good spiritual healers and yoga teachers.
        '''           
        
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"].copy()
        malefics = charts["D1"]["classifications"]["malefics"].copy()
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"]["Saturn"]["Aspected-by"]
        conjuncts = charts["D1"]["planets"]["Saturn"]["conjuncts"]
        benefics_aspectingSaturn = list(set(benefics).intersection(aspectedby))
        benefics_conjunctSaturn = list(set(benefics).intersection(conjuncts))
        malefics_aspectingSaturn = list(set(malefics).intersection(aspectedby))
        malefics_conjunctSaturn = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = ["Sa"]
        if (lagna_cond1_exhaltation  == True):
            relevant_planets.append(lagnasaturn["dispositor"][0:2])
        if (lagna_cond2_4mMoon  == True):
            relevant_planets.append("Mo")
        if (lagna_cond2_4mAsc  == True):
            relevant_planets.append(charts["D1"]["ascendant"]["lagna-lord"][0:2])
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"SASA",relevant_planets, colorlist)

        Note = f'''The Sasa Yoga is strengthened by association with Benefics and weakened by association with malefics. Also the results are subject to strength of ascendant or moon with which the saturn is in kendra.
        Benefic planets aspecting Saturn: {benefics_aspectingSaturn} and conjunct benefics: {benefics_conjunctSaturn}.
        Malefic planets aspecting Saturn: {malefics_aspectingSaturn} and conjunct malefics: {malefics_conjunctSaturn}.
        Consider all these points carefully before concluding the results of this panchamahapurusha yoga.'''

        #Update the yogadosha sections
        data.yogadoshas["SASA"] = {}
        data.yogadoshas["SASA"]["name"] = "Sasa Panchamahapurusha"
        data.yogadoshas["SASA"]["type"] = "Yoga"
        data.yogadoshas["SASA"]["exist"] = IsSasaYogaPresent
        data.yogadoshas["SASA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["SASA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["SASA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["SASA"]["Source"] = "https://www.astroyogi.com/kundli/yog/sasa/"
    
    return IsSasaYogaPresent

#function to check for Bhadra Panchamahapurusha yoga - Mercury
def BhadraYoga(charts):
    IsBhadraYogaPresent = False   #initially assume the yoga is not present
    Rule = ""
    Results = ""
    Note = ""
    #two conditions for Bhadra yoga to be present
        #cond1 -> Mercury must be in own rashi (Gemini) OR Mercury must be exhalted(Virgo)
        #cond2 -> Mercury must be in Kendra (either from ascendant or from moon)

    #check for Bhadra yoga with lagna D1 chart
    lagnamercury = charts["D1"]["planets"]["Mercury"]
    lagnamoon = charts["D1"]["planets"]["Moon"]

    #For condition 1
    lagna_cond1_exhaltation = False
    lagna_cond1_swarashi = False
    if(lagnamercury["sign"] == "Virgo"):
        lagna_cond1_exhaltation = True
        Rule = Rule + "In Lagna chart, Mercury is exhalted [Virgo]"
    elif (lagnamercury["sign"] == "Gemini"):
        lagna_cond1_swarashi = True
        Rule = Rule + f'In Lagna chart, Mercury is in Own sign [Gemini]'
    else:
        lagna_cond1_exhaltation = False
        lagna_cond1_swarashi = False
    lagna_cond1 = lagna_cond1_exhaltation or lagna_cond1_swarashi

    #For condition 2
    lagna_cond2_4mAsc = False
    lagna_cond2_4mMoon = False
    #check for Bhadra yoga kendra condition from ascendant
    kendranum_4mlagna = lagnamercury["house-num"]
    if((kendranum_4mlagna % 3) == 1):
        lagna_cond2_4mAsc = True
        Rule = Rule + f' and in Kendra [house number:{lagnamercury["house-num"]}]'
    else:
        lagna_cond2_4mAsc = False

    #check for Bhadra yoga kendra condition from moon
    kendranum_4mmoon = gen.housediff(lagnamoon["house-num"], lagnamercury["house-num"])
    if((kendranum_4mmoon % 3) == 1):
        lagna_cond2_4mMoon = True
        Rule = Rule + f' and in Kendra with respect to Moon [house number:{kendranum_4mmoon} from moon]'
    else:
        lagna_cond2_4mMoon = False

    lagna_cond2 = lagna_cond2_4mAsc or lagna_cond2_4mMoon
    IsBhadraYogaPresent = lagna_cond1 and lagna_cond2

    #detection part of yoga is over. Now if present then update the other details
    if(IsBhadraYogaPresent == True):
        #finish the rule. 
        Rule = Rule + f' Hence Bhadra Panchamahapurusha yoga is formed.'

        #Update the results
        Results = f'''Bhadra Yoga makes you stand out from the crowd and helps you advance steadily towards the highest level of success. It is believed that if the planet Mercury holds a favourable position in your birth chart and forms the Bhadra Yoga, it will enhance your intelligence and ensure that you achieve success in all your endeavours.
        The native is blessed with superlative intelligence and wisdom to make the right decisions at the right time. Also, it blesses the native with advanced communication skills which enables them to have a deep and lasting influence on people around them.
        This yoga blesses you with a long and healthy life. With the help of Bhadra Yoga, you will have a great career as a journalist, speaker, political person or reformer.
        Bhadra Yoga will improve your mental faculties and make you intelligent and wise. It also gives you a pleasing personality and a flexible mind. You are approachable and easily become a trusted confidant to many.
        '''           
        
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"].copy()
        malefics = charts["D1"]["classifications"]["malefics"].copy()
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"]["Mercury"]["Aspected-by"]
        conjuncts = charts["D1"]["planets"]["Mercury"]["conjuncts"]
        benefics_aspectingMercury = list(set(benefics).intersection(aspectedby))
        benefics_conjunctMercury = list(set(benefics).intersection(conjuncts))
        malefics_aspectingMercury = list(set(malefics).intersection(aspectedby))
        malefics_conjunctMercury = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = ["Me"]
        if (lagna_cond2_4mMoon  == True):
            relevant_planets.append("Mo")
        if (lagna_cond2_4mAsc  == True):
            relevant_planets.append(charts["D1"]["ascendant"]["lagna-lord"][0:2])
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"BHADRA",relevant_planets, colorlist)

        Note = f'''The Bhadra Yoga is strengthened by association with Benefics and weakened by association with malefics. Also the results are subject to strength of ascendant or moon with which the mercury is in kendra.
        Benefic planets aspecting Mercury: {benefics_aspectingMercury} and conjunct benefics: {benefics_conjunctMercury}.
        Malefic planets aspecting Mercury: {malefics_aspectingMercury} and conjunct malefics: {malefics_conjunctMercury}.
        Consider all these points carefully before concluding the results of this panchamahapurusha yoga.'''

        #Update the yogadosha sections
        data.yogadoshas["BHADRA"] = {}
        data.yogadoshas["BHADRA"]["name"] = "Bhadra Panchamahapurusha"
        data.yogadoshas["BHADRA"]["type"] = "Yoga"
        data.yogadoshas["BHADRA"]["exist"] = IsBhadraYogaPresent
        data.yogadoshas["BHADRA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["BHADRA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["BHADRA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["BHADRA"]["Source"] = "https://www.astroyogi.com/kundli/yog/bhadra/"
    
    return IsBhadraYogaPresent

#function to check for Ruchaka Panchamahapurusha yoga - Mars
def RuchakaYoga(charts):
    IsRuchakaYogaPresent = False   #initially assume the yoga is not present
    Rule = ""
    Results = ""
    Note = ""
    #two conditions for ruchaka yoga to be present
        #cond1 -> Mars must be in own rashi (Aries or Scorpio) OR Mars must be exhalted(Capricorn)
        #cond2 -> Mars must be in Kendra

    #check for ruchaka yoga with lagna D1 chart
    lagnamars = charts["D1"]["planets"]["Mars"]
    lagnamoon = charts["D1"]["planets"]["Moon"]

    #For condition 1
    lagna_cond1_exhaltation = False
    lagna_cond1_swarashi = False
    if(lagnamars["sign"] == "Capricorn"):
        lagna_cond1_exhaltation = True
        Rule = Rule + "In Lagna chart, Mars is exhalted [Capricorn]"
    elif (lagnamars["dispositor"] == "Mars"):
        lagna_cond1_swarashi = True
        Rule = Rule + f'In Lagna chart, Mars is in Own sign [{lagnamars["sign"]}]'
    else:
        lagna_cond1_exhaltation = False
        lagna_cond1_swarashi = False
    lagna_cond1 = lagna_cond1_exhaltation or lagna_cond1_swarashi

    #For condition 2
    lagna_cond2_4mAsc = False
    lagna_cond2_4mMoon = False
    #check for ruchaka yoga kendra condition from ascendant
    kendranum_4mlagna = lagnamars["house-num"]
    if((kendranum_4mlagna % 3) == 1):
        lagna_cond2_4mAsc = True
        Rule = Rule + f' and in Kendra [house number:{lagnamars["house-num"]}]'
    else:
        lagna_cond2_4mAsc = False

    #check for ruchaka yoga kendra condition from moon
    kendranum_4mmoon = gen.housediff(lagnamoon["house-num"], lagnamars["house-num"])
    if((kendranum_4mmoon % 3) == 1):
        lagna_cond2_4mMoon = True
        Rule = Rule + f' and in Kendra with respect to Moon [house number:{kendranum_4mmoon} from moon]'
    else:
        lagna_cond2_4mMoon = False

    lagna_cond2 = lagna_cond2_4mAsc or lagna_cond2_4mMoon
    IsRuchakaYogaPresent = lagna_cond1 and lagna_cond2


    if(IsRuchakaYogaPresent == True):
        #finish the rule. 
        Rule = Rule + f' Hence Ruchaka Panchamahapurusha yoga is formed.'

        #Update the results
        if(lagnamoon["house-num"] == 1): #if moon is in lagna thenruchaka is formed with both and same house distance
            #here ruchaka from ascendant is formed and moon also is in lagna so both are covered
            if (kendranum_4mlagna == 1):
                Results = f'''The  native shall become brave and courageous. His personality will be strong, and he would love to say their point straightforwardly. However, sometimes they might speak in a way that their words may hurt people unknowingly.
                Ruchaka yoga would provide immense physical energy. Their physical well-being would be a treat to watch. Therefore, a career in sports shall enhance their personality and make them successful people. Also, joining forces and being in police work would be good domains for them, career-wise.They will be good leaders.
                Ruchaka Yoga in 1st house comes with a con. With Mars in the first house, the native becomes a victim of the Kuja Dosha or Mangal Dosha. It may bring adversities in the person's life. Specifically, he/she may use all its positive points for attaining wrong deeds. Also, it shall lead to problems in the marital life of the person.
                '''
            elif (kendranum_4mlagna == 4):
                Results = f'''This Ruchaka Yoga provides natives with multiple lands and properties. The person might take birth with property in hand. Along with it, he/she shall possess all comforts and luxuries and true and pure love from mother and other family members.
                Natives shall also possess immense opportunities and growth in their professional world. From here, planet Mars forms a direct aspect with the 10th house. It shall help him grow and become successful in the workplace and grab a good job for himself.
                If the native ever faces hard times, he/she may effortlessly earn money and seek the benefit of wealth. Planet Mars acts as a Karak Grah for real estate and lands. Thus, it is a perfect Yoga to attain success in real estate matters.
                Natives would possess qualities like physical appearance, high energy levels, bravery, and courage. There wont be any shortage of support from people.
                On negative side, Mars in the fourth house makes the native Manglik. However, performing remedies for Mangal dosha can wear off the ill impacts of Kuja Dosha in the chart. With the Mangal Dosha, you may get into quarrelsome behavior and possess the same in the house.
                '''
            elif (kendranum_4mlagna == 7):
                Results = f'''This Ruchaka Yoga makes the person a serial entrepreneur. Native shall be fully driven and possess the energy to grow the business.
                The native is utterly competitive and very active in work. They grab jobs and careers that get them success immensely. However, there are chances that these natives wouldnt take criticism positively. It becomes their behavior to defend themselves as much as possible.
                Ruchaka Yoga leads to natives possessing support from external sources. He/she shall get into partnerships and seek a helping hand from his co-workers and employees. Also, during the Mars Mahadasha, his/her career flourishes to heights. Furthermore, it helps the natives in terms of wealth and business.
                Natives energy also uplifts others. The person becomes a great orator and holds the quality to influence the masses with words and speeches.
                On negative side, Mars in 7th house causes Mangal Dosha. The native becomes utterly aggressive, especially towards the spouse. Also, nature turns possessive around the partner. If the spouse is emotional, the native might deem the attitude of the person as angry.
                '''
            elif (kendranum_4mlagna == 10):
                Results = f'''The benefits of Ruchaka Yoga here are maximum. One because, planet Mars does not form a Mangal Dosha here, second because, in the 10th house, it gains the natural strength of the tenth house. Thus, it also forms a Maha Raj Yoga in the Kundli of the native.
                It helps natives enjoy career growth at an active rate. He/she shall be great as a leader and enjoy successful times and steady growth in her professional life. Moreover, Mars positioning here can create high possibilities for government jobs and politics. Natives would enjoy all sorts of comforts and seek many opportunities in the professional sector of life.
                The physical endurance of the native will be noteworthy and stamina unmatched. So, such people wont be afraid of bearing any sort of physical pain and love using their strengths more than anybody. Along with all this, the placement of Mars in the tenth house shall also make the native achieve utter fame and wealth.
                On negative side, Mars here may make the natives lack patience. He/she shall have to put the effort in excess to make things work. And the hasty decision-making skills will highlight with Mars placement in the 10th house. All this might make natives confront problems in the professional environment and lose important and worth taking opportunities too often. 
                However, on the other hand, natives will definitely be intelligent, and wisdom would be something he/she shall use at its best. Along with it, the energy of Mars will be maximum here. Thus, the person would be courageous and daring to do anything in life. Moreover, with their efforts and energy, natives would achieve greatness and success in life, for sure.
                '''
            else:
                Results = "It should not reach here. Something wrong in computation. Dont trust this analysis."
        
        else:
            #Here ruchaka is formed by either ascendant or/and moon position but not common house.
            if (lagna_cond2_4mAsc  == True):
                #Here ruchak is formed from lagna then
                if (kendranum_4mlagna == 1):
                    Results = f'''The  native shall become brave and courageous. His personality will be strong, and he would love to say their point straightforwardly. However, sometimes they might speak in a way that their words may hurt people unknowingly.
                    Ruchaka yoga would provide immense physical energy. Their physical well-being would be a treat to watch. Therefore, a career in sports shall enhance their personality and make them successful people. Also, joining forces and being in police work would be good domains for them, career-wise.They will be good leaders.
                    Ruchaka Yoga in 1st house comes with a con. With Mars in the first house, the native becomes a victim of the Kuja Dosha or Mangal Dosha. It may bring adversities in the person's life. Specifically, he/she may use all its positive points for attaining wrong deeds. Also, it shall lead to problems in the marital life of the person.
                    '''
                elif (kendranum_4mlagna == 4):
                    Results = f'''This Ruchaka Yoga provides natives with multiple lands and properties. The person might take birth with property in hand. Along with it, he/she shall possess all comforts and luxuries and true and pure love from mother and other family members.
                    Natives shall also possess immense opportunities and growth in their professional world. From here, planet Mars forms a direct aspect with the 10th house. It shall help him grow and become successful in the workplace and grab a good job for himself.
                    If the native ever faces hard times, he/she may effortlessly earn money and seek the benefit of wealth. Planet Mars acts as a Karak Grah for real estate and lands. Thus, it is a perfect Yoga to attain success in real estate matters.
                    Natives would possess qualities like physical appearance, high energy levels, bravery, and courage. There wont be any shortage of support from people.
                    On negative side, Mars in the fourth house makes the native Manglik. However, performing remedies for Mangal dosha can wear off the ill impacts of Kuja Dosha in the chart. With the Mangal Dosha, you may get into quarrelsome behavior and possess the same in the house.
                    '''
                elif (kendranum_4mlagna == 7):
                    Results = f'''This Ruchaka Yoga makes the person a serial entrepreneur. Native shall be fully driven and possess the energy to grow the business.
                    The native is utterly competitive and very active in work. They grab jobs and careers that get them success immensely. However, there are chances that these natives wouldnt take criticism positively. It becomes their behavior to defend themselves as much as possible.
                    Ruchaka Yoga leads to natives possessing support from external sources. He/she shall get into partnerships and seek a helping hand from his co-workers and employees. Also, during the Mars Mahadasha, his/her career flourishes to heights. Furthermore, it helps the natives in terms of wealth and business.
                    Natives energy also uplifts others. The person becomes a great orator and holds the quality to influence the masses with words and speeches.
                    On negative side, Mars in 7th house causes Mangal Dosha. The native becomes utterly aggressive, especially towards the spouse. Also, nature turns possessive around the partner. If the spouse is emotional, the native might deem the attitude of the person as angry.
                    '''
                elif (kendranum_4mlagna == 10):
                    Results = f'''The benefits of Ruchaka Yoga here are maximum. One because, planet Mars does not form a Mangal Dosha here, second because, in the 10th house, it gains the natural strength of the tenth house. Thus, it also forms a Maha Raj Yoga in the Kundli of the native.
                    It helps natives enjoy career growth at an active rate. He/she shall be great as a leader and enjoy successful times and steady growth in her professional life. Moreover, Mars positioning here can create high possibilities for government jobs and politics. Natives would enjoy all sorts of comforts and seek many opportunities in the professional sector of life.
                    The physical endurance of the native will be noteworthy and stamina unmatched. So, such people wont be afraid of bearing any sort of physical pain and love using their strengths more than anybody. Along with all this, the placement of Mars in the tenth house shall also make the native achieve utter fame and wealth.
                    On negative side, Mars here may make the natives lack patience. He/she shall have to put the effort in excess to make things work. And the hasty decision-making skills will highlight with Mars placement in the 10th house. All this might make natives confront problems in the professional environment and lose important and worth taking opportunities too often. 
                    However, on the other hand, natives will definitely be intelligent, and wisdom would be something he/she shall use at its best. Along with it, the energy of Mars will be maximum here. Thus, the person would be courageous and daring to do anything in life. Moreover, with their efforts and energy, natives would achieve greatness and success in life, for sure.
                    '''
                else:
                    Results = "It should not reach here. Something wrong in computation. Dont trust this analysis. "
            
            if (lagna_cond2_4mMoon  == True):
                #Here ruchak is formed from Moon then
                if (kendranum_4mmoon == 1):
                    Results = f'''{Results}The  native shall become brave and courageous. His personality will be strong, and he would love to say their point straightforwardly. However, sometimes they might speak in a way that their words may hurt people unknowingly.
                    Ruchaka yoga would provide immense physical energy. Their physical well-being would be a treat to watch. Therefore, a career in sports shall enhance their personality and make them successful people. Also, joining forces and being in police work would be good domains for them, career-wise.They will be good leaders.
                    Ruchaka Yoga in 1st house comes with a con. With Mars in the first house, the native becomes a victim of the Kuja Dosha or Mangal Dosha. It may bring adversities in the person's life. Specifically, he/she may use all its positive points for attaining wrong deeds. Also, it shall lead to problems in the marital life of the person.'''
                elif (kendranum_4mmoon == 4):
                    Results = f'''{Results}This Ruchaka Yoga provides natives with multiple lands and properties. The person might take birth with property in hand. Along with it, he/she shall possess all comforts and luxuries and true and pure love from mother and other family members.
                    Natives shall also possess immense opportunities and growth in their professional world. From here, planet Mars forms a direct aspect with the 10th house. It shall help him grow and become successful in the workplace and grab a good job for himself.
                    If the native ever faces hard times, he/she may effortlessly earn money and seek the benefit of wealth. Planet Mars acts as a Karak Grah for real estate and lands. Thus, it is a perfect Yoga to attain success in real estate matters.
                    Natives would possess qualities like physical appearance, high energy levels, bravery, and courage. There wont be any shortage of support from people.
                    On negative side, Mars in the fourth house makes the native Manglik. However, performing remedies for Mangal dosha can wear off the ill impacts of Kuja Dosha in the chart. With the Mangal Dosha, you may get into quarrelsome behavior and possess the same in the house.'''
                elif (kendranum_4mmoon == 7):
                    Results = f'''{Results}This Ruchaka Yoga makes the person a serial entrepreneur. Native shall be fully driven and possess the energy to grow the business.
                    The native is utterly competitive and very active in work. They grab jobs and careers that get them success immensely. However, there are chances that these natives wouldnt take criticism positively. It becomes their behavior to defend themselves as much as possible.
                    Ruchaka Yoga leads to natives possessing support from external sources. He/she shall get into partnerships and seek a helping hand from his co-workers and employees. Also, during the Mars Mahadasha, his/her career flourishes to heights. Furthermore, it helps the natives in terms of wealth and business.
                    Natives energy also uplifts others. The person becomes a great orator and holds the quality to influence the masses with words and speeches.
                    On negative side, Mars in 7th house causes Mangal Dosha. The native becomes utterly aggressive, especially towards the spouse. Also, nature turns possessive around the partner. If the spouse is emotional, the native might deem the attitude of the person as angry.'''
                elif (kendranum_4mmoon == 10):
                    Results = f'''{Results}The benefits of Ruchaka Yoga here are maximum. One because, planet Mars does not form a Mangal Dosha here, second because, in the 10th house, it gains the natural strength of the tenth house. Thus, it also forms a Maha Raj Yoga in the Kundli of the native.
                    It helps natives enjoy career growth at an active rate. He/she shall be great as a leader and enjoy successful times and steady growth in her professional life. Moreover, Mars positioning here can create high possibilities for government jobs and politics. Natives would enjoy all sorts of comforts and seek many opportunities in the professional sector of life.
                    The physical endurance of the native will be noteworthy and stamina unmatched. So, such people wont be afraid of bearing any sort of physical pain and love using their strengths more than anybody. Along with all this, the placement of Mars in the tenth house shall also make the native achieve utter fame and wealth.
                    On negative side, Mars here may make the natives lack patience. He/she shall have to put the effort in excess to make things work. And the hasty decision-making skills will highlight with Mars placement in the 10th house. All this might make natives confront problems in the professional environment and lose important and worth taking opportunities too often. 
                    However, on the other hand, natives will definitely be intelligent, and wisdom would be something he/she shall use at its best. Along with it, the energy of Mars will be maximum here. Thus, the person would be courageous and daring to do anything in life. Moreover, with their efforts and energy, natives would achieve greatness and success in life, for sure.'''
                else:
                    Results = f"{Results}It should not reach here. Something wrong in computation. Dont trust this analysis."
                     
        
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"].copy()
        malefics = charts["D1"]["classifications"]["malefics"].copy()
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"]["Mars"]["Aspected-by"]
        conjuncts = charts["D1"]["planets"]["Mars"]["conjuncts"]
        benefics_aspectingMars = list(set(benefics).intersection(aspectedby))
        benefics_conjunctMars = list(set(benefics).intersection(conjuncts))
        malefics_aspectingMars = list(set(malefics).intersection(aspectedby))
        malefics_conjunctMars = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = ["Ma"]
        if (lagna_cond1_exhaltation  == True):
            relevant_planets.append(lagnamars["dispositor"][0:2])
        if (lagna_cond2_4mMoon  == True):
            relevant_planets.append("Mo")
        if (lagna_cond2_4mAsc  == True):
            relevant_planets.append(charts["D1"]["ascendant"]["lagna-lord"][0:2])
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"RUCHAKA",relevant_planets, colorlist)

        Note = f'''The Ruchaka Yoga is strengthened by association with Benefics and weakened by association with malefics. Also the results are subject to strength of ascendant or moon with which the mars is in kendra.
        Benefic planets aspecting Mars: {benefics_aspectingMars} and conjunct benefics: {benefics_conjunctMars}.
        Malefic planets aspecting Mars: {malefics_aspectingMars} and conjunct malefics: {malefics_conjunctMars}.
        Consider all these points carefully before concluding the results of this panchamahapurusha yoga.'''

        #Update the yogadosha sections
        data.yogadoshas["RUCHAKA"] = {}
        data.yogadoshas["RUCHAKA"]["name"] = "Ruchaka Panchamahapurusha"
        data.yogadoshas["RUCHAKA"]["type"] = "Yoga"
        data.yogadoshas["RUCHAKA"]["exist"] = IsRuchakaYogaPresent
        data.yogadoshas["RUCHAKA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["RUCHAKA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["RUCHAKA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["RUCHAKA"]["Source"] = "https://astrotalk.com/astrology-blog/ruchaka-yoga-in-astrology-impacts-and-benefits-in-different-houses/"
    
    return IsRuchakaYogaPresent

#function to check for Hamsa Panchamahapurusha yoga - Jupiter
def HamsaYoga(charts):
    IsHamsaYogaPresent = False   #initially assume the yoga is not present
    Rule = ""
    Results = ""
    Note = ""
    #two conditions for Hamsa yoga to be present
        #cond1 -> Jupiter must be in own rashi (Saggitarius or Pisces) OR Jupiter must be exhalted(Cancer)
        #cond2 -> Jupiter must be in Kendra (either from ascendant or from moon)

    #check for Hamsa yoga with lagna D1 chart
    lagnajupiter = charts["D1"]["planets"]["Jupiter"]
    lagnamoon = charts["D1"]["planets"]["Moon"]

    #For condition 1
    lagna_cond1_exhaltation = False
    lagna_cond1_swarashi = False
    if(lagnajupiter["sign"] == "Cancer"):
        lagna_cond1_exhaltation = True
        Rule = Rule + "In Lagna chart, Jupiter is exhalted [Cancer]"
    elif (lagnajupiter["sign"] == "Saggitarius"):
        lagna_cond1_swarashi = True
        Rule = Rule + f'In Lagna chart, Jupiter is in Own sign [Saggitarius]'
    elif (lagnajupiter["sign"] == "Pisces"):
        lagna_cond1_swarashi = True
        Rule = Rule + f'In Lagna chart, Jupiter is in Own sign [Pisces]'
    else:
        lagna_cond1_exhaltation = False
        lagna_cond1_swarashi = False
    lagna_cond1 = lagna_cond1_exhaltation or lagna_cond1_swarashi

    #For condition 2
    lagna_cond2_4mAsc = False
    lagna_cond2_4mMoon = False
    #check for Hamsa yoga kendra condition from ascendant
    kendranum_4mlagna = lagnajupiter["house-num"]
    if((kendranum_4mlagna % 3) == 1):
        lagna_cond2_4mAsc = True
        Rule = Rule + f' and in Kendra [house number:{lagnajupiter["house-num"]}]'
    else:
        lagna_cond2_4mAsc = False

    #check for Hamsa yoga kendra condition from moon
    kendranum_4mmoon = gen.housediff(lagnamoon["house-num"], lagnajupiter["house-num"])
    if((kendranum_4mmoon % 3) == 1):
        lagna_cond2_4mMoon = True
        Rule = Rule + f' and in Kendra with respect to Moon [house number:{kendranum_4mmoon} from moon]'
    else:
        lagna_cond2_4mMoon = False

    lagna_cond2 = lagna_cond2_4mAsc or lagna_cond2_4mMoon
    IsHamsaYogaPresent = lagna_cond1 and lagna_cond2

    #detection part of yoga is over. Now if present then update the other details
    if(IsHamsaYogaPresent == True):
        #finish the rule. 
        Rule = Rule + f' Hence Hamsa Panchamahapurusha yoga is formed.'

        #Update the results
        Results = f'''Incredible Emotional Intelligence & Knowledge for the Welfare of Masses.
        This yoga in your horoscope blesses you with incredible emotional Intelligence and knowledge that brings about the welfare of the masses and underprivileged, drawing great respect for you in society.
        Hamsa Yoga confers respect in society with great knowledge, high rank in educational institution. This yoga has the power to bless you with an incredible amount of emotional intelligence, which can give you strong social connectivity. 
        Hamsa Yoga will help you get support from Jupiter to acquire a good amount of wisdom and knowledge that can lead you towards growth and success with great achievements. It helps the person write great books, accumulate great amount of knowledge for the welfare of society and the underprivileged.
        It is very difficult to stand against a person with Hamsa Yoga and win. Some famous people with Hamsa Yoga are Jayalalitha, Dr APJ Abdul Kalam, Farooq Abdullah etc.'''           
        
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"]
        malefics = charts["D1"]["classifications"]["malefics"]
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"]["Jupiter"]["Aspected-by"]
        conjuncts = charts["D1"]["planets"]["Jupiter"]["conjuncts"]
        benefics_aspectingJupiter = list(set(benefics).intersection(aspectedby))
        benefics_conjunctJupiter = list(set(benefics).intersection(conjuncts))
        malefics_aspectingJupiter = list(set(malefics).intersection(aspectedby))
        malefics_conjunctJupiter = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = ["Ju"]
        if (lagna_cond2_4mMoon  == True):
            relevant_planets.append("Mo")
        if (lagna_cond2_4mAsc  == True):
            relevant_planets.append(charts["D1"]["ascendant"]["lagna-lord"][0:2])
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"HAMSA",relevant_planets, colorlist)

        Note = f'''The Hamsa Yoga is strengthened by association with Benefics and weakened by association with malefics. Also the results are subject to strength of ascendant or moon with which the jupiter is in kendra.
        Benefic planets aspecting Jupiter: {benefics_aspectingJupiter} and conjunct benefics: {benefics_conjunctJupiter}.
        Malefic planets aspecting Jupiter: {malefics_aspectingJupiter} and conjunct malefics: {malefics_conjunctJupiter}.
        Consider all these points carefully before concluding the results of this panchamahapurusha yoga.'''

        #Update the yogadosha sections
        data.yogadoshas["HAMSA"] = {}
        data.yogadoshas["HAMSA"]["name"] = "Hamsa Panchamahapurusha"
        data.yogadoshas["HAMSA"]["type"] = "Yoga"
        data.yogadoshas["HAMSA"]["exist"] = IsHamsaYogaPresent
        data.yogadoshas["HAMSA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["HAMSA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["HAMSA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["HAMSA"]["Source"] = "https://www.indastro.com/astrology-reports/hamsa-yoga.php"
    
    return IsHamsaYogaPresent

#function to check for Malavya Panchamahapurusha yoga - Venus
def MalavyaYoga(charts):
    IsMalavyaYogaPresent = False   #initially assume the yoga is not present
    Rule = ""
    Results = ""
    Note = ""
    #two conditions for Malavya yoga to be present
        #cond1 -> Venus must be in own rashi (Taurus or Libra) OR Venus must be exhalted(Pisces)
        #cond2 -> Venus must be in Kendra (either from ascendant or from moon)

    #check for Malavya yoga with lagna D1 chart
    lagnavenus = charts["D1"]["planets"]["Venus"]
    lagnamoon = charts["D1"]["planets"]["Moon"]

    #For condition 1
    lagna_cond1_exhaltation = False
    lagna_cond1_swarashi = False
    if(lagnavenus["sign"] == "Pisces"):
        lagna_cond1_exhaltation = True
        Rule = Rule + "In Lagna chart, Venus is exhalted [Pisces]"
    elif (lagnavenus["sign"] == "Taurus"):
        lagna_cond1_swarashi = True
        Rule = Rule + f'In Lagna chart, Venus is in Own sign [Taurus]'
    elif (lagnavenus["sign"] == "Libra"):
        lagna_cond1_swarashi = True
        Rule = Rule + f'In Lagna chart, Venus is in Own sign [Libra]'
    else:
        lagna_cond1_exhaltation = False
        lagna_cond1_swarashi = False
    lagna_cond1 = lagna_cond1_exhaltation or lagna_cond1_swarashi

    #For condition 2
    lagna_cond2_4mAsc = False
    lagna_cond2_4mMoon = False
    #check for Malavya yoga kendra condition from ascendant
    kendranum_4mlagna = lagnavenus["house-num"]
    if((kendranum_4mlagna % 3) == 1):
        lagna_cond2_4mAsc = True
        Rule = Rule + f' and in Kendra [house number:{lagnavenus["house-num"]}]'
    else:
        lagna_cond2_4mAsc = False

    #check for Malavya yoga kendra condition from moon
    kendranum_4mmoon = gen.housediff(lagnamoon["house-num"], lagnavenus["house-num"])
    if((kendranum_4mmoon % 3) == 1):
        lagna_cond2_4mMoon = True
        Rule = Rule + f' and in Kendra with respect to Moon [house number:{kendranum_4mmoon} from moon]'
    else:
        lagna_cond2_4mMoon = False

    lagna_cond2 = lagna_cond2_4mAsc or lagna_cond2_4mMoon
    IsMalavyaYogaPresent = lagna_cond1 and lagna_cond2

    #detection part of yoga is over. Now if present then update the other details
    if(IsMalavyaYogaPresent == True):
        #finish the rule. 
        Rule = Rule + f' Hence Malavya Panchamahapurusha yoga is formed.'

        #Update the results
        Results = f'''The natives having Malavya Yoga in a horoscope will possess a charming and magnetic personality that attracts other people very easily and especially the people from the opposite sex.
        The natives will be good looking, artistic, intelligent, famous, a powerful sense of humor, and possess all materialistic pleasures and richness in life. The natives are praiseworthy, open-minded, determined, powerful, and lucky.
        The natives will be renowned, successful, own many vehicles, highly educated, and lives a life full of luxury and happiness. They will enjoy happiness through life-partner and children along with materialistic happiness.
        Malavya yoga blesses the native with a beautiful and loving wife, success in business, a life full of luxuries and comforts, and fame on the national or international level. It also gives a good home, vehicles, luxury and comfort, and beauty.
        The natives having Malavya yoga can become successful in the professional fields like modeling, cinema, movies and other such fields that require beauty and charm in order to be successful. The natives can excel in the fields of acting, dancing, singing, cosmetics, and fashion.
        Your artistic skills are greatly advanced due to the powerful influence of this yoga in your life. It makes you a visionary and enables you to find solutions to situations with a high level of creativity. The aesthetic part of you shows up in everything you do.
        Some famous persons with this yoga are: Jayalalitha, Sania Mirza, Sonia Gandhi, Jawaharlal Nehru, Mahatma Gandhi etc
        '''           
        
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"]
        malefics = charts["D1"]["classifications"]["malefics"]
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"]["Venus"]["Aspected-by"]
        conjuncts = charts["D1"]["planets"]["Venus"]["conjuncts"]
        benefics_aspectingVenus = list(set(benefics).intersection(aspectedby))
        benefics_conjunctVenus = list(set(benefics).intersection(conjuncts))
        malefics_aspectingVenus = list(set(malefics).intersection(aspectedby))
        malefics_conjunctVenus = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = ["Ve"]
        if (lagna_cond1_exhaltation  == True):
            relevant_planets.append(lagnavenus["dispositor"][0:2])
        if (lagna_cond2_4mMoon  == True):
            relevant_planets.append("Mo")
        if (lagna_cond2_4mAsc  == True):
            relevant_planets.append(charts["D1"]["ascendant"]["lagna-lord"][0:2])
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"MALAVYA",relevant_planets, colorlist)

        Note = f'''The Malavya Yoga is strengthened by association with Benefics and weakened by association with malefics. Also the results are subject to strength of ascendant or moon with which the venus is in kendra.
        Benefic planets aspecting Venus: {benefics_aspectingVenus} and conjunct benefics: {benefics_conjunctVenus}.
        Malefic planets aspecting Venus: {malefics_aspectingVenus} and conjunct malefics: {malefics_conjunctVenus}.
        Consider all these points carefully before concluding the results of this panchamahapurusha yoga.'''

        #Update the yogadosha sections
        data.yogadoshas["MALAVYA"] = {}
        data.yogadoshas["MALAVYA"]["name"] = "Malavya Panchamahapurusha"
        data.yogadoshas["MALAVYA"]["type"] = "Yoga"
        data.yogadoshas["MALAVYA"]["exist"] = IsMalavyaYogaPresent
        data.yogadoshas["MALAVYA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["MALAVYA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["MALAVYA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["MALAVYA"]["Source"] = "https://www.ganeshaspeaks.com/learn-astrology/yogas/malavya-yoga/"
    
    return IsMalavyaYogaPresent

#Functions to check for Vipareeta Raja Yogas - Harsha, Sarala , Vimala
#function to check for Harsha Vipareeta Raja Yoga - 6th/8th/12th Lord in 6th house in lagna
def HarshaYoga(charts):
    IsHarshaYogaPresent = False   #initially assume the yoga is not present
    cnt = 0
    Rule = ""
    Results = ""
    Note = "The Harsha Yoga is impacted by association with Benefics and malefics. Also the results are subject to strength of ascendant and combustion with Sun\n"

    #Section for checking if Yoga is formed
    #Condition for formation of Harsha Yoga is When 6th, 8th or 12th house lords occupy 6th house
    #initially assume the Yoga Doesnt exist
    cond_SixthlordInSixth = False
    cond_EighthlordInSixth = False
    cond_TwelfthlordInSixth = False
    colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
    colorlist[6-1] = "yellow"
    #check if 6th lord is in 6th
    lord = gen.get_nthLord(charts["D1"], 6)
    if (gen.get_planetPlacedHousenum(charts["D1"],lord) == 6):
        cond_SixthlordInSixth = True
        colorlist[6-1] = "yellow"
        cnt = cnt + 1
        lordsdetails = charts["D1"]["planets"][lord]
        Rule = f'''{Rule}Lord of sixth house {lord} is placed in sixth house. '''
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"]
        malefics = charts["D1"]["classifications"]["malefics"]
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"][lord]["Aspected-by"]
        conjuncts = charts["D1"]["planets"][lord]["conjuncts"]
        benefics_aspectinglord = list(set(benefics).intersection(aspectedby))
        benefics_conjunctlord = list(set(benefics).intersection(conjuncts))
        malefics_aspectinglord = list(set(malefics).intersection(aspectedby))
        malefics_conjunctlord = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = [lord[0:2]]
        relevant_planets.append(lordsdetails["dispositor"][0:2])        
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        Note = f'''{Note}Benefic planets aspecting {lord}: {benefics_aspectinglord} and conjunct benefics: {benefics_conjunctlord}.
        Malefic planets aspecting {lord}: {malefics_aspectinglord} and conjunct malefics: {malefics_conjunctlord}.
        '''

    #check if 8th lord is in 6th
    lord = gen.get_nthLord(charts["D1"], 8)
    if (gen.get_planetPlacedHousenum(charts["D1"],lord) == 6):
        cond_EighthlordInSixth = True
        colorlist[8-1] = "yellow"
        cnt = cnt + 1
        lordsdetails = charts["D1"]["planets"][lord]
        Rule = f'''{Rule}Lord of eighth house {lord} is placed in sixth house. '''
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"]
        malefics = charts["D1"]["classifications"]["malefics"]
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"][lord]["Aspected-by"]
        conjuncts = charts["D1"]["planets"][lord]["conjuncts"]
        benefics_aspectinglord = list(set(benefics).intersection(aspectedby))
        benefics_conjunctlord = list(set(benefics).intersection(conjuncts))
        malefics_aspectinglord = list(set(malefics).intersection(aspectedby))
        malefics_conjunctlord = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = [lord[0:2]]
        relevant_planets.append(lordsdetails["dispositor"][0:2])        
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        Note = f'''{Note}Benefic planets aspecting {lord}: {benefics_aspectinglord} and conjunct benefics: {benefics_conjunctlord}.
        Malefic planets aspecting {lord}: {malefics_aspectinglord} and conjunct malefics: {malefics_conjunctlord}.
        '''

    #check if 12th lord is in 6th
    lord = gen.get_nthLord(charts["D1"], 12)
    if (gen.get_planetPlacedHousenum(charts["D1"],lord) == 6):
        cond_TwelfthlordInSixth = True
        colorlist[12-1] = "yellow"
        cnt = cnt + 1
        lordsdetails = charts["D1"]["planets"][lord]
        Rule = f'''{Rule}Lord of Twelfth house {lord} is placed in sixth house. '''
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"]
        malefics = charts["D1"]["classifications"]["malefics"]
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"][lord]["Aspected-by"]
        conjuncts = charts["D1"]["planets"][lord]["conjuncts"]
        benefics_aspectinglord = list(set(benefics).intersection(aspectedby))
        benefics_conjunctlord = list(set(benefics).intersection(conjuncts))
        malefics_aspectinglord = list(set(malefics).intersection(aspectedby))
        malefics_conjunctlord = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = [lord[0:2]]
        relevant_planets.append(lordsdetails["dispositor"][0:2])        
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        Note = f'''{Note}Benefic planets aspecting {lord}: {benefics_aspectinglord} and conjunct benefics: {benefics_conjunctlord}.
        Malefic planets aspecting {lord}: {malefics_aspectinglord} and conjunct malefics: {malefics_conjunctlord}.
        '''

    IsHarshaYogaPresent = (cond_SixthlordInSixth or cond_EighthlordInSixth or cond_TwelfthlordInSixth)
    #If yoga is present then update the details and results etc
    if(IsHarshaYogaPresent == True):
        Rule = f'''{Rule}Hence {cnt} count of Harsha yoga is formed in Natives Lagna chart\n'''
        Note = f'''{Note}Consider all these points carefully before concluding the results of this Vipareeta rajayoga.'''
        dc.create_SimpleYogaDoshaChart(charts["D1"],"HARSHA",relevant_planets, colorlist)

        #Update the Results of Harsha Yoga
        Results = f'''Harsha Yoga is a Vipreeta Raja Yoga. As its name suggests, it is made up of two words - <Vipreeta> which means reverse and <Raja> which means a ruler. This presents a condition in the kundali of a person where the negatives add up to a positive outcome that can be life-altering. Fortunes are reversed wherein you receive benefits after a spate of bad luck.
        Vipreeta Raj Yoga is a contradictory yoga where you get the positive results from the paapi grahas. These grahas are notorious for causing malice and ill-will with their effects. But they face an advantageous position when they are in each other's houses and this results in positive outcomes.
        According to Phaladeepika, Harsha yoga native will be blessed with happiness, good fortune, and have a strong constitution. He will conquer his enemies and will not do sinful deeds. He will become a friend of illustrious, wealthy, splendorous, famous, and will have many friends.
        Harsha Vipreet Raj Yoga blesses the native with health and wealth. He or she is considered a leader who wins over enemies, earning much fame and glory
        '''

        #Update the yogadosha sections
        data.yogadoshas["HARSHA"] = {}
        data.yogadoshas["HARSHA"]["name"] = "Harsha Vipareeta Raja"
        data.yogadoshas["HARSHA"]["type"] = "Yoga"
        data.yogadoshas["HARSHA"]["exist"] = IsHarshaYogaPresent
        data.yogadoshas["HARSHA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["HARSHA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["HARSHA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["HARSHA"]["Source"] = "https://www.sanatanveda.com/astrology/vipareeta-raja-yoga-in-vedic-astrology/"
    
    return IsHarshaYogaPresent

#function to check for Sarala Vipareeta Raja Yoga - 6th/8th/12th Lord in 8th house in lagna
def SaralaYoga(charts):
    IsSaralaYogaPresent = False   #initially assume the yoga is not present
    cnt = 0
    Rule = ""
    Results = ""
    Note = "The Sarala Yoga is impacted by association with Benefics and malefics. Also the results are subject to strength of ascendant and combustion with Sun\n"

    #Section for checking if Yoga is formed
    #Condition for formation of Sarala Yoga is When 6th, 8th or 12th house lords occupy 8th house
    #initially assume the Yoga Doesnt exist
    cond_SixthlordInEighth = False
    cond_EighthlordInEighth = False
    cond_TwelfthlordInEighth = False
    colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
    colorlist[8-1] = "yellow"
    #check if 6th lord is in 8th
    lord = gen.get_nthLord(charts["D1"], 6)
    if (gen.get_planetPlacedHousenum(charts["D1"],lord) == 8):
        cond_SixthlordInEighth = True
        colorlist[6-1] = "yellow"
        cnt = cnt + 1
        lordsdetails = charts["D1"]["planets"][lord]
        Rule = f'''{Rule}Lord of sixth house {lord} is placed in eighth house. '''
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"]
        malefics = charts["D1"]["classifications"]["malefics"]
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"][lord]["Aspected-by"]
        conjuncts = charts["D1"]["planets"][lord]["conjuncts"]
        benefics_aspectinglord = list(set(benefics).intersection(aspectedby))
        benefics_conjunctlord = list(set(benefics).intersection(conjuncts))
        malefics_aspectinglord = list(set(malefics).intersection(aspectedby))
        malefics_conjunctlord = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = [lord[0:2]]
        relevant_planets.append(lordsdetails["dispositor"][0:2])        
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        Note = f'''{Note}Benefic planets aspecting {lord}: {benefics_aspectinglord} and conjunct benefics: {benefics_conjunctlord}.
        Malefic planets aspecting {lord}: {malefics_aspectinglord} and conjunct malefics: {malefics_conjunctlord}.
        '''

    #check if 8th lord is in 8th
    lord = gen.get_nthLord(charts["D1"], 8)
    if (gen.get_planetPlacedHousenum(charts["D1"],lord) == 8):
        cond_EighthlordInEighth = True
        colorlist[8-1] = "yellow"
        cnt = cnt + 1
        lordsdetails = charts["D1"]["planets"][lord]
        Rule = f'''{Rule}Lord of eighth house {lord} is placed in eighth house. '''
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"]
        malefics = charts["D1"]["classifications"]["malefics"]
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"][lord]["Aspected-by"]
        conjuncts = charts["D1"]["planets"][lord]["conjuncts"]
        benefics_aspectinglord = list(set(benefics).intersection(aspectedby))
        benefics_conjunctlord = list(set(benefics).intersection(conjuncts))
        malefics_aspectinglord = list(set(malefics).intersection(aspectedby))
        malefics_conjunctlord = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = [lord[0:2]]
        relevant_planets.append(lordsdetails["dispositor"][0:2])        
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        Note = f'''{Note}Benefic planets aspecting {lord}: {benefics_aspectinglord} and conjunct benefics: {benefics_conjunctlord}.
        Malefic planets aspecting {lord}: {malefics_aspectinglord} and conjunct malefics: {malefics_conjunctlord}.
        '''

    #check if 12th lord is in 8th
    lord = gen.get_nthLord(charts["D1"], 12)
    if (gen.get_planetPlacedHousenum(charts["D1"],lord) == 8):
        cond_TwelfthlordInEighth = True
        colorlist[12-1] = "yellow"
        cnt = cnt + 1
        lordsdetails = charts["D1"]["planets"][lord]
        Rule = f'''{Rule}Lord of Twelfth house {lord} is placed in eighth house. '''
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"]
        malefics = charts["D1"]["classifications"]["malefics"]
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"][lord]["Aspected-by"]
        conjuncts = charts["D1"]["planets"][lord]["conjuncts"]
        benefics_aspectinglord = list(set(benefics).intersection(aspectedby))
        benefics_conjunctlord = list(set(benefics).intersection(conjuncts))
        malefics_aspectinglord = list(set(malefics).intersection(aspectedby))
        malefics_conjunctlord = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = [lord[0:2]]
        relevant_planets.append(lordsdetails["dispositor"][0:2])        
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        Note = f'''{Note}Benefic planets aspecting {lord}: {benefics_aspectinglord} and conjunct benefics: {benefics_conjunctlord}.
        Malefic planets aspecting {lord}: {malefics_aspectinglord} and conjunct malefics: {malefics_conjunctlord}.
        '''

    IsSaralaYogaPresent = (cond_SixthlordInEighth or cond_EighthlordInEighth or cond_TwelfthlordInEighth)
    #If yoga is present then update the details and results etc
    if(IsSaralaYogaPresent == True):
        Rule = f'''{Rule}Hence {cnt} count of Sarala yoga is formed in Natives Lagna chart\n'''
        Note = f'''{Note}Consider all these points carefully before concluding the results of this Vipareeta rajayoga.'''
        dc.create_SimpleYogaDoshaChart(charts["D1"],"SARALA",relevant_planets, colorlist)

        #Update the Results of Sarala Yoga
        Results = f'''Sarala Yoga is a Vipreeta Raja Yoga. As its name suggests, it is made up of two words - <Vipreeta> which means reverse and <Raja> which means a ruler. This presents a condition in the kundali of a person where the negatives add up to a positive outcome that can be life-altering. Fortunes are reversed wherein you receive benefits after a spate of bad luck.
        Vipreeta Raj Yoga is a contradictory yoga where you get the positive results from the paapi grahas. These grahas are notorious for causing malice and ill-will with their effects. But they face an advantageous position when they are in each other's houses and this results in positive outcomes.
        According to Phaladeepika, Sarala yoga enables the natives to be long-lived, resolute, fearless, prosperous, learned, blessed with children, and wealth. The native with this yoga will achieve success in all his ventures, will be victorious over his enemies, and will be a great celebrity.
        Sarala Vipreeta Raja Yoga blesses the person with wisdom and power. It infuses the native with an air of authority and the sagacity to solve problems
        '''

        #Update the yogadosha sections
        data.yogadoshas["SARALA"] = {}
        data.yogadoshas["SARALA"]["name"] = "Sarala Vipareeta Raja"
        data.yogadoshas["SARALA"]["type"] = "Yoga"
        data.yogadoshas["SARALA"]["exist"] = IsSaralaYogaPresent
        data.yogadoshas["SARALA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["SARALA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["SARALA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["SARALA"]["Source"] = "https://www.sanatanveda.com/astrology/vipareeta-raja-yoga-in-vedic-astrology/"
    
    return IsSaralaYogaPresent

#function to check for Vimala Vipareeta Raja Yoga - 6th/8th/12th Lord in 12th house in lagna
def VimalaYoga(charts):
    IsVimalaYogaPresent = False   #initially assume the yoga is not present
    cnt = 0
    Rule = ""
    Results = ""
    Note = "The Vimala Yoga is impacted by association with Benefics and malefics. Also the results are subject to strength of ascendant and combustion with Sun\n"

    #Section for checking if Yoga is formed
    #Condition for formation of Vimala Yoga is When 6th, 8th or 12th house lords occupy 12th house
    #initially assume the Yoga Doesnt exist
    cond_SixthlordInTwelfth = False
    cond_EighthlordInTwelfth = False
    cond_TwelfthlordInTwelfth = False
    colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
    colorlist[12-1] = "yellow"
    #check if 6th lord is in 12th
    lord = gen.get_nthLord(charts["D1"], 6)
    if (gen.get_planetPlacedHousenum(charts["D1"],lord) == 12):
        cond_SixthlordInTwelfth = True
        colorlist[6-1] = "yellow"
        cnt = cnt + 1
        lordsdetails = charts["D1"]["planets"][lord]
        Rule = f'''{Rule}Lord of sixth house {lord} is placed in twelfth house. '''
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"]
        malefics = charts["D1"]["classifications"]["malefics"]
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"][lord]["Aspected-by"]
        conjuncts = charts["D1"]["planets"][lord]["conjuncts"]
        benefics_aspectinglord = list(set(benefics).intersection(aspectedby))
        benefics_conjunctlord = list(set(benefics).intersection(conjuncts))
        malefics_aspectinglord = list(set(malefics).intersection(aspectedby))
        malefics_conjunctlord = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = [lord[0:2]]
        relevant_planets.append(lordsdetails["dispositor"][0:2])        
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        Note = f'''{Note}Benefic planets aspecting {lord}: {benefics_aspectinglord} and conjunct benefics: {benefics_conjunctlord}.
        Malefic planets aspecting {lord}: {malefics_aspectinglord} and conjunct malefics: {malefics_conjunctlord}.
        '''

    #check if 8th lord is in 12th
    lord = gen.get_nthLord(charts["D1"], 8)
    if (gen.get_planetPlacedHousenum(charts["D1"],lord) == 12):
        cond_EighthlordInTwelfth = True
        colorlist[8-1] = "yellow"
        cnt = cnt + 1
        lordsdetails = charts["D1"]["planets"][lord]
        Rule = f'''{Rule}Lord of eighth house {lord} is placed in twelfth house. '''
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"]
        malefics = charts["D1"]["classifications"]["malefics"]
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"][lord]["Aspected-by"]
        conjuncts = charts["D1"]["planets"][lord]["conjuncts"]
        benefics_aspectinglord = list(set(benefics).intersection(aspectedby))
        benefics_conjunctlord = list(set(benefics).intersection(conjuncts))
        malefics_aspectinglord = list(set(malefics).intersection(aspectedby))
        malefics_conjunctlord = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = [lord[0:2]]
        relevant_planets.append(lordsdetails["dispositor"][0:2])        
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        Note = f'''{Note}Benefic planets aspecting {lord}: {benefics_aspectinglord} and conjunct benefics: {benefics_conjunctlord}.
        Malefic planets aspecting {lord}: {malefics_aspectinglord} and conjunct malefics: {malefics_conjunctlord}.
        '''

    #check if 12th lord is in 12th
    lord = gen.get_nthLord(charts["D1"], 12)
    if (gen.get_planetPlacedHousenum(charts["D1"],lord) == 12):
        cond_TwelfthlordInTwelfth = True
        colorlist[12-1] = "yellow"
        cnt = cnt + 1
        lordsdetails = charts["D1"]["planets"][lord]
        Rule = f'''{Rule}Lord of Twelfth house {lord} is placed in twelfth house. '''
        #update the notes 
        benefics = charts["D1"]["classifications"]["benefics"]
        malefics = charts["D1"]["classifications"]["malefics"]
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = charts["D1"]["planets"][lord]["Aspected-by"]
        conjuncts = charts["D1"]["planets"][lord]["conjuncts"]
        benefics_aspectinglord = list(set(benefics).intersection(aspectedby))
        benefics_conjunctlord = list(set(benefics).intersection(conjuncts))
        malefics_aspectinglord = list(set(malefics).intersection(aspectedby))
        malefics_conjunctlord = list(set(malefics).intersection(conjuncts))
        #getting full list of relevant planets for this yoga
        relevant_planets = [lord[0:2]]
        relevant_planets.append(lordsdetails["dispositor"][0:2])        
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        Note = f'''{Note}Benefic planets aspecting {lord}: {benefics_aspectinglord} and conjunct benefics: {benefics_conjunctlord}.
        Malefic planets aspecting {lord}: {malefics_aspectinglord} and conjunct malefics: {malefics_conjunctlord}.
        '''

    IsVimalaYogaPresent = (cond_SixthlordInTwelfth or cond_EighthlordInTwelfth or cond_TwelfthlordInTwelfth)
    #If yoga is present then update the details and results etc
    if(IsVimalaYogaPresent == True):
        Rule = f'''{Rule}Hence {cnt} count of Vimala yoga is formed in Natives Lagna chart\n'''
        Note = f'''{Note}Consider all these points carefully before concluding the results of this Vipareeta rajayoga.'''
        dc.create_SimpleYogaDoshaChart(charts["D1"],"VIMALA",relevant_planets, colorlist)

        #Update the Results of Vimala Yoga
        Results = f'''Vimala Yoga is a Vipreeta Raja Yoga. As its name suggests, it is made up of two words - <Vipreeta> which means reverse and <Raja> which means a ruler. This presents a condition in the kundali of a person where the negatives add up to a positive outcome that can be life-altering. Fortunes are reversed wherein you receive benefits after a spate of bad luck.
        Vipreeta Raja Yoga is a contradictory yoga where you get the positive results from the paapi grahas. These grahas are notorious for causing malice and ill-will with their effects. But they face an advantageous position when they are in each other's houses and this results in positive outcomes.
        According to Phaladeepika, The native with Vimala yoga will be clever in saving money, frugal in his expenses, equipped with good behavior towards others, will enjoy happiness, will be independent, will follow a respectable profession or conduct, and will be well known for his good qualities.
        The native with Vimala yoga will be good at accumulating wealth, good in financial management, spend less, enjoy the pleasures, he also charitable in nature, will be famous in the circle. On the other side, he will also spend on hospitalization, hostile to learned people, will get into unnecessary arguments, short-lived. This yoga also blesses the person with a positive attitude, an honourable career and a spiritual approach to life.
        '''

        #Update the yogadosha sections
        data.yogadoshas["VIMALA"] = {}
        data.yogadoshas["VIMALA"]["name"] = "Vimala Vipareeta Raja"
        data.yogadoshas["VIMALA"]["type"] = "Yoga"
        data.yogadoshas["VIMALA"]["exist"] = IsVimalaYogaPresent
        data.yogadoshas["VIMALA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["VIMALA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["VIMALA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["VIMALA"]["Source"] = "https://www.sanatanveda.com/astrology/vipareeta-raja-yoga-in-vedic-astrology/"
    
    return IsVimalaYogaPresent

#Functions to detect Kaal Sarpa Doshas
#function to identify if kaal sarpa dosha exist or not and if yes then is it ascending or descending
def kaalSarpaDosha(charts):
    #Check if kaal sarpa dosha exists. 
    #return value can be ABSENT, ASCENDPRESENT, DESCENDPRESENT

    #For Kaal sarpa dosha to be present, All 7 planets must be on the same side of Rahu Ketu Axis in D1 chart
    #If planets are present right side of Rahu-Ketu axis then its ascending kaala sarpa dosha else its descending

    IsKaalSarpaDoshaPresent = True  #initially assume the dosha is present. 
    #Check distance between Rahu and Sun
    baseplanet = "Rahu"
    dist = gen.get_distancebetweenplanets(charts["D1"], baseplanet, "Sun")
    if (dist > (180*3600)): #If sun is greater than sun is in the right side of rahu ketu axis. so lets make Ketu as base planet
        baseplanet = "Ketu"
    
    #now lets check if all other 6 planets are also same side of rahu ketu axis as sub. 
    #So now distance between any of 6 remaining planets from baseplanet must not be more than 180 degrees for kaal sarpa dosha to exist
    for planet in ["Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        dist = gen.get_distancebetweenplanets(charts["D1"], baseplanet, planet)
        if (dist > (180*3600)): #Rahu ketu axis is broken
            IsKaalSarpaDoshaPresent = False
            break   #end for loop once kaal sarpa dosha is broken
    
    if(IsKaalSarpaDoshaPresent == True):
        if (baseplanet == "Rahu"):
            retval = "DESCENDPRESENT"
        else:
            retval = "ASCENDPRESENT"
    else:
         retval = "ABSENT"
    
    return retval

#Ananta Kaal sarpa dosha - Kaalsarpa dosha with Rahu in Tan bhav
def AnantaKaalSarpaDosha(charts):
    IsAnantaKaalSarpaDoshaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    Remedies = ""

    KaalSarpDoshaSts = kaalSarpaDosha(charts)
    if (KaalSarpDoshaSts != "ABSENT") and (charts["D1"]["planets"]["Rahu"]["house-num"] == 1):
        IsAnantaKaalSarpaDoshaPresent = True
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[1-1] = "yellow"
        colorlist[7-1] = "yellow"
        #Update the Name and Rule
        if (KaalSarpDoshaSts == "ASCENDPRESENT"):
            Name = "Ascending Ananta Kaala Sarpa"
            typ = "Ascending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 1st house and Ketu is in 7th house this is Ananta Kaala Sarpa Dosha. All the planets are right side of Rahu-Ketu Axis heading towards Rahu So its Ascending Ananta Kaala Sarpa Dosha.
            '''
        else:
            Name = "Descending Ananta Kaala Sarpa"
            typ = "Descending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 1st house and Ketu is in 7th house this is Ananta Kaala Sarpa Dosha. All the planets are left side of Rahu-Ketu Axis heading towards Ketu So its Descending Ananta Kaala Sarpa Dosha.
            '''
        #Update the Results of Ananta Kaala Sarpa Dosha
        Results = f'''Kaal Sarp Dosha is a frightful astrological event that affects a person severely with multifaceted catastrophes. It is a result of bad karma done by the native in the previous lives.
        As Kaalsarp dosh veils the planets, the aspects other planets represent may get hampered, which may lead to problems in the life of the native. So the results from aspects of other planets will be blocked by Rahu-Ketu axis and the native will not be ble to get full results of other planets in his kundali.
        The natives with Ananta kaala sarpa dosha will have to struggle for longer to find success. Although you will work very hard in order to succeed, but the results will come to you after a delay. The Anant Kaalsarp dosh will likely test your patience by introducing you to constant obstacles and challenges. Due to this dosha, a person faces problems in all aspects of their lives, but if you don't lose hope, you will find success later. 
        Also, don't indulge in ill deeds such as gambling, lust, etc.
        '''
        #Update the Note
        Note = "The effect of Ananta Kaala Sarpa Dosha will decrease after the age of 27 if other strong Yogas are present in Native's Kundali."
        #update Remedies for Dosha
        Remedies = f'''One of the most effective remedies to reduce the effects of the Kala Sarpa Dosha is visiting shrines of higher spiritual beings. The popular places to visit include Srikalahasti temple, Trimbakeshwar temple, Rameswaram, and Thirunageswaram. The Kalasarpa Dosha Nivaran Puja at Sri Kalahasti mandir, Rameswaram, and Thirunageswaram, is considered the best remedy for Kala Sarpa Dosha. This Dosha can also be remedied by Kal Rudra Yagna performed in these temples.
        Rudra Avisek of Shiva, in any Shiva Temple, and chanting of powerful mantras like the Mrityunjay Mantra, Vishnu Panchakshari Mantra, and Sarp Mantra are the other popular remedies for this Dosha.
        Specifically for Ananta Kaal Sarpa dosha can be solved or atleast impact be reduced by Reading Hanuman Chalisa five times a day for 40 days. If you are a student, you should chant the 'Saraswati Mantra' and 'Saraswatye Namah' for 10-15 minutes daily.'''
        
        relevant_planets = ["Su", "Mo", "Ma", "Me", "Ju", "Ve", "Sa", "Ra", "Ke"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"ANANTAKAALSARPA",relevant_planets, colorlist)


        #Update the yogadosha sections
        data.yogadoshas["ANANTAKAALSARPA"] = {}
        data.yogadoshas["ANANTAKAALSARPA"]["name"] = Name
        data.yogadoshas["ANANTAKAALSARPA"]["type"] = "Dosha"
        data.yogadoshas["ANANTAKAALSARPA"]["exist"] = IsAnantaKaalSarpaDoshaPresent
        data.yogadoshas["ANANTAKAALSARPA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["ANANTAKAALSARPA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["ANANTAKAALSARPA"]["Remedies"] = gen.iterativeReplace(Remedies,"\n ", "\n").replace("\n","\n        ")
        data.yogadoshas["ANANTAKAALSARPA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["ANANTAKAALSARPA"]["Source"] = "https://astrotalk.com/kaal-sarp-dosh-12-types"
    
    return IsAnantaKaalSarpaDoshaPresent

#Kulika Kaal sarpa dosha - Kaalsarpa dosha with Rahu in Tan bhav
def KulikaKaalSarpaDosha(charts):
    IsKulikaKaalSarpaDoshaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    Remedies = ""

    KaalSarpDoshaSts = kaalSarpaDosha(charts)
    if (KaalSarpDoshaSts != "ABSENT") and (charts["D1"]["planets"]["Rahu"]["house-num"] == 2):
        IsKulikaKaalSarpaDoshaPresent = True
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[2-1] = "yellow"
        colorlist[8-1] = "yellow"
        #Update the Name and Rule
        if (KaalSarpDoshaSts == "ASCENDPRESENT"):
            Name = "Ascending Kulika Kaala Sarpa"
            typ = "Ascending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 2nd house and Ketu is in 8th house this is Kulika Kaala Sarpa Dosha. All the planets are right side of Rahu-Ketu Axis heading towards Rahu So its Ascending Kulika Kaala Sarpa Dosha.
            '''
        else:
            Name = "Descending Kulika Kaala Sarpa"
            typ = "Descending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 2nd house and Ketu is in 8th house this is Kulika Kaala Sarpa Dosha. All the planets are left side of Rahu-Ketu Axis heading towards Ketu So its Descending Kulika Kaala Sarpa Dosha.
            '''
        #Update the Results of Kulika Kaala Sarpa Dosha
        Results = f'''Kaal Sarp Dosha is a frightful astrological event that affects a person severely with multifaceted catastrophes. It is a result of bad karma done by the native in the previous lives.
        As Kaalsarp dosh veils the planets, the aspects other planets represent may get hampered, which may lead to problems in the life of the native. So the results from aspects of other planets will be blocked by Rahu-Ketu axis and the native will not be ble to get full results of other planets in his kundali.
        The Kulika kaala sarpa dosha is believed to bring economic losses, humiliation, debt and various other obstacles in the native's life. Hence astrologers suggest that you don't form bondings with people without careful scrutiny. If you are into business, make sure you do it with 100% honesty, especially during the Kulik dosh period. 
        When it comes to married life, it is to remain normal for the native dealing with Kulika dosh. You however may feel that you are getting old before time, thus you must invest in taking care of your health. Do not use intoxicants such as cigarettes, tobacco, etc
        Defamations, scandals, unstable marital life, problems from inheritance, financial issues, etc. are connected with this Dosha.
        '''
        #Update the Note
        Note = "The effect of Kulika Kaala Sarpa Dosha will decrease after the age of 33 if other strong Yogas are present in Native's Kundali."
        #update Remedies for Dosha
        Remedies = f'''One of the most effective remedies to reduce the effects of the Kala Sarpa Dosha is visiting shrines of higher spiritual beings. The popular places to visit include Srikalahasti temple, Trimbakeshwar temple, Rameswaram, and Thirunageswaram. The Kalasarpa Dosha Nivaran Puja at Sri Kalahasti mandir, Rameswaram, and Thirunageswaram, is considered the best remedy for Kala Sarpa Dosha. This Dosha can also be remedied by Kal Rudra Yagna performed in these temples.
        Rudra Avisek of Shiva, in any Shiva Temple, and chanting of powerful mantras like the Mrityunjay Mantra, Vishnu Panchakshari Mantra, and Sarp Mantra are the other popular remedies for this Dosha.
        Specifically, Kulika Kaal Sarpa dosha can be solved or atleast impact be reduced by lighting a lamp of mustard oil in front of the Hanuman idol on every saturday evening. Hold energised Silver Rahu Yantra on Saturday'''
        
        relevant_planets = ["Su", "Mo", "Ma", "Me", "Ju", "Ve", "Sa", "Ra", "Ke"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"KULIKAKAALSARPA",relevant_planets, colorlist)


        #Update the yogadosha sections
        data.yogadoshas["KULIKAKAALSARPA"] = {}
        data.yogadoshas["KULIKAKAALSARPA"]["name"] = Name
        data.yogadoshas["KULIKAKAALSARPA"]["type"] = "Dosha"
        data.yogadoshas["KULIKAKAALSARPA"]["exist"] = IsKulikaKaalSarpaDoshaPresent
        data.yogadoshas["KULIKAKAALSARPA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["KULIKAKAALSARPA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["KULIKAKAALSARPA"]["Remedies"] = gen.iterativeReplace(Remedies,"\n ", "\n").replace("\n","\n        ")
        data.yogadoshas["KULIKAKAALSARPA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["KULIKAKAALSARPA"]["Source"] = "https://astrotalk.com/kaal-sarp-dosh-12-types"
    
    return IsKulikaKaalSarpaDoshaPresent

#Vasuki Kaal sarpa dosha - Kaalsarpa dosha with Rahu in Tan bhav
def VasukiKaalSarpaDosha(charts):
    IsVasukiKaalSarpaDoshaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    Remedies = ""

    KaalSarpDoshaSts = kaalSarpaDosha(charts)
    if (KaalSarpDoshaSts != "ABSENT") and (charts["D1"]["planets"]["Rahu"]["house-num"] == 3):
        IsVasukiKaalSarpaDoshaPresent = True
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[3-1] = "yellow"
        colorlist[9-1] = "yellow"
        #Update the Name and Rule
        if (KaalSarpDoshaSts == "ASCENDPRESENT"):
            Name = "Ascending Vasuki Kaala Sarpa"
            typ = "Ascending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 3rd house and Ketu is in 9th house this is Vasuki Kaala Sarpa Dosha. All the planets are right side of Rahu-Ketu Axis heading towards Rahu So its Ascending Vasuki Kaala Sarpa Dosha.
            '''
        else:
            Name = "Descending Vasuki Kaala Sarpa"
            typ = "Descending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 3rd house and Ketu is in 9th house this is Vasuki Kaala Sarpa Dosha. All the planets are left side of Rahu-Ketu Axis heading towards Ketu So its Descending Vasuki Kaala Sarpa Dosha.
            '''
        #Update the Results of Vasuki Kaala Sarpa Dosha
        Results = f'''Kaal Sarp Dosha is a frightful astrological event that affects a person severely with multifaceted catastrophes. It is a result of bad karma done by the native in the previous lives.
        As Kaalsarp dosh veils the planets, the aspects other planets represent may get hampered, which may lead to problems in the life of the native. So the results from aspects of other planets will be blocked by Rahu-Ketu axis and the native will not be ble to get full results of other planets in his kundali.
        The Vasuki kaala sarpa dosha doesn't only hamper the life of the native but also of the ones related to him, such as his siblings, parents, spouse, etc. You have to face the fact that your family members may cheat on you. There will likely be a lack of peace in the family, and the peace will further shatter with inflating economic problems as the Vasuki Kaalsarp dosh continues. 
        However, the good thing is that the person will have economic success as he continues to put in the hard work in making sure things work out for him. 
        The individual would not get the desired results of their hard work and receive their rewards late in life. This Dosha may cause losses in business too.
        '''
        #Update the Note
        Note = "The effect of Vasuki Kaala Sarpa Dosha will decrease after the age of 36 if other strong Yogas are present in Native's Kundali."
        #update Remedies for Dosha
        Remedies = f'''One of the most effective remedies to reduce the effects of the Kala Sarpa Dosha is visiting shrines of higher spiritual beings. The popular places to visit include Srikalahasti temple, Trimbakeshwar temple, Rameswaram, and Thirunageswaram. The Kalasarpa Dosha Nivaran Puja at Sri Kalahasti mandir, Rameswaram, and Thirunageswaram, is considered the best remedy for Kala Sarpa Dosha. This Dosha can also be remedied by Kal Rudra Yagna performed in these temples.
        Rudra Avisek of Shiva, in any Shiva Temple, and chanting of powerful mantras like the Mrityunjay Mantra, Vishnu Panchakshari Mantra, and Sarp Mantra are the other popular remedies for this Dosha.
        Specifically, Vasuki Kaal Sarpa dosha can be solved or atleast impact be reduced by reading Hanuman Chalisa and Bajrang Baan 5 times for 40 days. Hold energised Silver Rahu Yantra on Saturday. 
        Also every Wednesday keep a handful of Urad dal in a black cloth, and chant the Rahu spell mantra and flow the Urad in the water.'''
        
        relevant_planets = ["Su", "Mo", "Ma", "Me", "Ju", "Ve", "Sa", "Ra", "Ke"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"VASUKIKAALSARPA",relevant_planets, colorlist)


        #Update the yogadosha sections
        data.yogadoshas["VASUKIKAALSARPA"] = {}
        data.yogadoshas["VASUKIKAALSARPA"]["name"] = Name
        data.yogadoshas["VASUKIKAALSARPA"]["type"] = "Dosha"
        data.yogadoshas["VASUKIKAALSARPA"]["exist"] = IsVasukiKaalSarpaDoshaPresent
        data.yogadoshas["VASUKIKAALSARPA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["VASUKIKAALSARPA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["VASUKIKAALSARPA"]["Remedies"] = gen.iterativeReplace(Remedies,"\n ", "\n").replace("\n","\n        ")
        data.yogadoshas["VASUKIKAALSARPA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["VASUKIKAALSARPA"]["Source"] = "https://astrotalk.com/kaal-sarp-dosh-12-types"
    
    return IsVasukiKaalSarpaDoshaPresent

#Shankhapala Kaal sarpa dosha - Kaalsarpa dosha with Rahu in Tan bhav
def ShankhapalaKaalSarpaDosha(charts):
    IsShankhapalaKaalSarpaDoshaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    Remedies = ""

    KaalSarpDoshaSts = kaalSarpaDosha(charts)
    if (KaalSarpDoshaSts != "ABSENT") and (charts["D1"]["planets"]["Rahu"]["house-num"] == 4):
        IsShankhapalaKaalSarpaDoshaPresent = True
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[4-1] = "yellow"
        colorlist[10-1] = "yellow"
        #Update the Name and Rule
        if (KaalSarpDoshaSts == "ASCENDPRESENT"):
            Name = "Ascending Shankhapala Kaala Sarpa"
            typ = "Ascending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 4th house and Ketu is in 10th house this is Shankhapala Kaala Sarpa Dosha. All the planets are right side of Rahu-Ketu Axis heading towards Rahu So its Ascending Shankhapala Kaala Sarpa Dosha.
            '''
        else:
            Name = "Descending Shankhapala Kaala Sarpa"
            typ = "Descending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 4th house and Ketu is in 10th house this is Shankhapala Kaala Sarpa Dosha. All the planets are left side of Rahu-Ketu Axis heading towards Ketu So its Descending Shankhapala Kaala Sarpa Dosha.
            '''
        #Update the Results of Shankhapala Kaala Sarpa Dosha
        Results = f'''Kaal Sarp Dosha is a frightful astrological event that affects a person severely with multifaceted catastrophes. It is a result of bad karma done by the native in the previous lives.
        As Kaalsarp dosh veils the planets, the aspects other planets represent may get hampered, which may lead to problems in the life of the native. So the results from aspects of other planets will be blocked by Rahu-Ketu axis and the native will not be ble to get full results of other planets in his kundali.
        The Shankhapala kaala sarpa dosha is the signal of incoming financial hardship, disease and disorder in the native's life. Hence, he/she should prepare for it. During this period, the happiness in the native's family will plunge to new lows. This may further hamper elements such as love, child's education, etc. 
        If a youngster, the native will find it tough to make the right choices, due to which he or she may find it difficult to settle early in life. The people of this yoga have to face difficulties related to land and property, thus any such deals must be done after proper scrutiny.
        '''
        #Update the Note
        Note = "The effect of Shankhapala Kaala Sarpa Dosha will decrease after the age of 43 if other strong Yogas are present in Native's Kundali."
        #update Remedies for Dosha
        Remedies = f'''One of the most effective remedies to reduce the effects of the Kala Sarpa Dosha is visiting shrines of higher spiritual beings. The popular places to visit include Srikalahasti temple, Trimbakeshwar temple, Rameswaram, and Thirunageswaram. The Kalasarpa Dosha Nivaran Puja at Sri Kalahasti mandir, Rameswaram, and Thirunageswaram, is considered the best remedy for Kala Sarpa Dosha. This Dosha can also be remedied by Kal Rudra Yagna performed in these temples.
        Rudra Avisek of Shiva, in any Shiva Temple, and chanting of powerful mantras like the Mrityunjay Mantra, Vishnu Panchakshari Mantra, and Sarp Mantra are the other popular remedies for this Dosha.
        Specifically, Shankhapala Kaal Sarpa dosha can be solved or atleast impact be reduced by hanging Hanuman Bahuk in red cloth on any Tuesday on the wall towards the south side of the house. On any Friday, flush the water coconut in water during the day. 
        you can also hang Hanuman Bahuk in red cloth on any Tuesday on the wall towards the south side of the house.'''
        
        relevant_planets = ["Su", "Mo", "Ma", "Me", "Ju", "Ve", "Sa", "Ra", "Ke"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"SHANKHAPALAKAALSARPA",relevant_planets, colorlist)


        #Update the yogadosha sections
        data.yogadoshas["SHANKHAPALAKAALSARPA"] = {}
        data.yogadoshas["SHANKHAPALAKAALSARPA"]["name"] = Name
        data.yogadoshas["SHANKHAPALAKAALSARPA"]["type"] = "Dosha"
        data.yogadoshas["SHANKHAPALAKAALSARPA"]["exist"] = IsShankhapalaKaalSarpaDoshaPresent
        data.yogadoshas["SHANKHAPALAKAALSARPA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["SHANKHAPALAKAALSARPA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["SHANKHAPALAKAALSARPA"]["Remedies"] = gen.iterativeReplace(Remedies,"\n ", "\n").replace("\n","\n        ")
        data.yogadoshas["SHANKHAPALAKAALSARPA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["SHANKHAPALAKAALSARPA"]["Source"] = "https://astrotalk.com/kaal-sarp-dosh-12-types"
    
    return IsShankhapalaKaalSarpaDoshaPresent

#Padam Kaal sarpa dosha - Kaalsarpa dosha with Rahu in Santaan bhav
def PadamKaalSarpaDosha(charts):
    IsPadamKaalSarpaDoshaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    Remedies = ""

    KaalSarpDoshaSts = kaalSarpaDosha(charts)
    if (KaalSarpDoshaSts != "ABSENT") and (charts["D1"]["planets"]["Rahu"]["house-num"] == 5):
        IsPadamKaalSarpaDoshaPresent = True
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[5-1] = "yellow"
        colorlist[11-1] = "yellow"
        #Update the Name and Rule
        if (KaalSarpDoshaSts == "ASCENDPRESENT"):
            Name = "Ascending Padam Kaala Sarpa"
            typ = "Ascending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 5th house and Ketu is in 11th house this is Padam Kaala Sarpa Dosha. All the planets are right side of Rahu-Ketu Axis heading towards Rahu So its Ascending Padam Kaala Sarpa Dosha.
            '''
        else:
            Name = "Descending Padam Kaala Sarpa"
            typ = "Descending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 5th house and Ketu is in 11th house this is Padam Kaala Sarpa Dosha. All the planets are left side of Rahu-Ketu Axis heading towards Ketu So its Descending Padam Kaala Sarpa Dosha.
            '''
        #Update the Results of Padam Kaala Sarpa Dosha
        Results = f'''Kaal Sarp Dosha is a frightful astrological event that affects a person severely with multifaceted catastrophes. It is a result of bad karma done by the native in the previous lives.
        As Kaalsarp dosh veils the planets, the aspects other planets represent may get hampered, which may lead to problems in the life of the native. So the results from aspects of other planets will be blocked by Rahu-Ketu axis and the native will not be ble to get full results of other planets in his kundali.
        The Padam kaala sarpa dosha is especially harmful to students as they may lose concentration in studies and indulge in detrimental deeds. Hence, parents must keep an eye on their children during this period. You also need to ensure you help your child make the right choices in education or it will simply cost you and him a loss of money and time. 
        For grown-ups, the dosh may hamper your progress in your career. If you are looking for new opportunities or taking risks, you must do it with a partner. Also, health should be a priority as the Padam Kaalsarp dosh progresses.
        The 5th house indicates Purva Punya so this clearly shows the lack of Purva Punya. There will be hindrances in the field of education and career, but the individual could cross all barriers and succeed eventually. Ill health and secret enemies are the biggest adversaries.
        '''
        #Update the Note
        Note = "The effect of Padam Kaala Sarpa Dosha will decrease after the age of 48 if other strong Yogas are present in Native's Kundali."
        #update Remedies for Dosha
        Remedies = f'''One of the most effective remedies to reduce the effects of the Kala Sarpa Dosha is visiting shrines of higher spiritual beings. The popular places to visit include Srikalahasti temple, Trimbakeshwar temple, Rameswaram, and Thirunageswaram. The Kalasarpa Dosha Nivaran Puja at Sri Kalahasti mandir, Rameswaram, and Thirunageswaram, is considered the best remedy for Kala Sarpa Dosha. This Dosha can also be remedied by Kal Rudra Yagna performed in these temples.
        Rudra Avisek of Shiva, in any Shiva Temple, and chanting of powerful mantras like the Mrityunjay Mantra, Vishnu Panchakshari Mantra, and Sarp Mantra are the other popular remedies for this Dosha.
        Specifically, Padam Kaal Sarpa dosha can be solved or atleast impact be reduced by wering a triangular Coral gemstone of seven and a quarter with copper in the middle finger of the right hand on any Tuesday. Keep a Peacock feather in the books on Saturday.
        '''
        
        relevant_planets = ["Su", "Mo", "Ma", "Me", "Ju", "Ve", "Sa", "Ra", "Ke"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"PADAMKAALSARPA",relevant_planets, colorlist)


        #Update the yogadosha sections
        data.yogadoshas["PADAMKAALSARPA"] = {}
        data.yogadoshas["PADAMKAALSARPA"]["name"] = Name
        data.yogadoshas["PADAMKAALSARPA"]["type"] = "Dosha"
        data.yogadoshas["PADAMKAALSARPA"]["exist"] = IsPadamKaalSarpaDoshaPresent
        data.yogadoshas["PADAMKAALSARPA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["PADAMKAALSARPA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["PADAMKAALSARPA"]["Remedies"] = gen.iterativeReplace(Remedies,"\n ", "\n").replace("\n","\n        ")
        data.yogadoshas["PADAMKAALSARPA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["PADAMKAALSARPA"]["Source"] = "https://astrotalk.com/kaal-sarp-dosh-12-types"
    
    return IsPadamKaalSarpaDoshaPresent

#Mahapadma Kaal sarpa dosha - Kaalsarpa dosha with Rahu in Rog bhav
def MahapadmaKaalSarpaDosha(charts):
    IsMahapadmaKaalSarpaDoshaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    Remedies = ""

    KaalSarpDoshaSts = kaalSarpaDosha(charts)
    if (KaalSarpDoshaSts != "ABSENT") and (charts["D1"]["planets"]["Rahu"]["house-num"] == 6):
        IsMahapadmaKaalSarpaDoshaPresent = True
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[6-1] = "yellow"
        colorlist[12-1] = "yellow"
        #Update the Name and Rule
        if (KaalSarpDoshaSts == "ASCENDPRESENT"):
            Name = "Ascending Mahapadma Kaala Sarpa"
            typ = "Ascending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 6th house and Ketu is in 12th house this is Mahapadma Kaala Sarpa Dosha. All the planets are right side of Rahu-Ketu Axis heading towards Rahu So its Ascending Mahapadma Kaala Sarpa Dosha.
            '''
        else:
            Name = "Descending Mahapadma Kaala Sarpa"
            typ = "Descending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 6th house and Ketu is in 12th house this is Mahapadma Kaala Sarpa Dosha. All the planets are left side of Rahu-Ketu Axis heading towards Ketu So its Descending Mahapadma Kaala Sarpa Dosha.
            '''
        #Update the Results of Mahapadma Kaala Sarpa Dosha
        Results = f'''Kaal Sarp Dosha is a frightful astrological event that affects a person severely with multifaceted catastrophes. It is a result of bad karma done by the native in the previous lives.
        As Kaalsarp dosh veils the planets, the aspects other planets represent may get hampered, which may lead to problems in the life of the native. So the results from aspects of other planets will be blocked by Rahu-Ketu axis and the native will not be ble to get full results of other planets in his kundali.
        The Mahapadma kaala sarpa dosha is special as its more of a partial-yoga than a Dosha. The native finds himself the luck to win over all his enemies with ease. There is an enhancement in wisdom and a thrust of will to do something worthwhile and big in life. 
        However, as the dosh period continues, the native tends to lose peace of mind and may make thoughtless choices. In the dosh period, the person earns profit from business from abroad. 
        '''
        #Update the Note
        Note = "The effect of Mahapadma Kaala Sarpa Dosha will decrease after the age of 54 if other strong Yogas are present in Native's Kundali."
        #update Remedies for Dosha
        Remedies = f'''One of the most effective remedies to reduce the effects of the Kala Sarpa Dosha is visiting shrines of higher spiritual beings. The popular places to visit include Srikalahasti temple, Trimbakeshwar temple, Rameswaram, and Thirunageswaram. The Kalasarpa Dosha Nivaran Puja at Sri Kalahasti mandir, Rameswaram, and Thirunageswaram, is considered the best remedy for Kala Sarpa Dosha. This Dosha can also be remedied by Kal Rudra Yagna performed in these temples.
        Rudra Avisek of Shiva, in any Shiva Temple, and chanting of powerful mantras like the Mrityunjay Mantra, Vishnu Panchakshari Mantra, and Sarp Mantra are the other popular remedies for this Dosha.
        Specifically, Mahapadma Kaal Sarpa dosha can be solved or atleast impact be reduced by visiting the Hanuman idol in the morning on Tuesday. Recite Hanuman Chalisa once in a day for 40 days. 
        Also you can recite Sunderkand of Ramcharitmanas on Tuesday or Saturday 108 times.
        '''
        
        relevant_planets = ["Su", "Mo", "Ma", "Me", "Ju", "Ve", "Sa", "Ra", "Ke"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"MAHAPADMAKAALSARPA",relevant_planets, colorlist)


        #Update the yogadosha sections
        data.yogadoshas["MAHAPADMAKAALSARPA"] = {}
        data.yogadoshas["MAHAPADMAKAALSARPA"]["name"] = Name
        data.yogadoshas["MAHAPADMAKAALSARPA"]["type"] = "Dosha"
        data.yogadoshas["MAHAPADMAKAALSARPA"]["exist"] = IsMahapadmaKaalSarpaDoshaPresent
        data.yogadoshas["MAHAPADMAKAALSARPA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["MAHAPADMAKAALSARPA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["MAHAPADMAKAALSARPA"]["Remedies"] = gen.iterativeReplace(Remedies,"\n ", "\n").replace("\n","\n        ")
        data.yogadoshas["MAHAPADMAKAALSARPA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["MAHAPADMAKAALSARPA"]["Source"] = "https://astrotalk.com/kaal-sarp-dosh-12-types"
    
    return IsMahapadmaKaalSarpaDoshaPresent

#Takshaka Kaal sarpa dosha - Kaalsarpa dosha with Rahu in Santaan bhav
def TakshakaKaalSarpaDosha(charts):
    IsTakshakaKaalSarpaDoshaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    Remedies = ""

    KaalSarpDoshaSts = kaalSarpaDosha(charts)
    if (KaalSarpDoshaSts != "ABSENT") and (charts["D1"]["planets"]["Rahu"]["house-num"] == 7):
        IsTakshakaKaalSarpaDoshaPresent = True
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[7-1] = "yellow"
        colorlist[1-1] = "yellow"
        #Update the Name and Rule
        if (KaalSarpDoshaSts == "ASCENDPRESENT"):
            Name = "Ascending Takshaka Kaala Sarpa"
            typ = "Ascending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 7th house and Ketu is in 1st house this is Takshaka Kaala Sarpa Dosha. All the planets are right side of Rahu-Ketu Axis heading towards Rahu So its Ascending Takshaka Kaala Sarpa Dosha.
            '''
        else:
            Name = "Descending Takshaka Kaala Sarpa"
            typ = "Descending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 7th house and Ketu is in 1st house this is Takshaka Kaala Sarpa Dosha. All the planets are left side of Rahu-Ketu Axis heading towards Ketu So its Descending Takshaka Kaala Sarpa Dosha.
            '''
        #Update the Results of Takshaka Kaala Sarpa Dosha
        Results = f'''Kaal Sarp Dosha is a frightful astrological event that affects a person severely with multifaceted catastrophes. It is a result of bad karma done by the native in the previous lives.
        As Kaalsarp dosh veils the planets, the aspects other planets represent may get hampered, which may lead to problems in the life of the native. So the results from aspects of other planets will be blocked by Rahu-Ketu axis and the native will not be ble to get full results of other planets in his kundali.
        The Takshaka kaala sarpa dosha impacts mainly the marriage. he or she may have to face a delay in marriage. The marriage delay may become the reason for tension and stress for your parents too. If married, there may be disturbances due to the nature of the in-laws. There may also arise situations when you might think of divorce. 
        Also, the ones dealing with Kaalsarp dosh must not consider love marriage during the dosh period. Doing so will hamper the love you share after marriage, and you will have to put extra effort to make things work.
        You find romance difficult and also have trouble receiving their share of ancestral property. They may have good achievements but would show the tendency to renounce everything.
        '''
        #Update the Note
        Note = "The effect of Takshaka Kaala Sarpa Dosha will decrease after the age of 60 if other strong Yogas are present in Native's Kundali."
        #update Remedies for Dosha
        Remedies = f'''One of the most effective remedies to reduce the effects of the Kala Sarpa Dosha is visiting shrines of higher spiritual beings. The popular places to visit include Srikalahasti temple, Trimbakeshwar temple, Rameswaram, and Thirunageswaram. The Kalasarpa Dosha Nivaran Puja at Sri Kalahasti mandir, Rameswaram, and Thirunageswaram, is considered the best remedy for Kala Sarpa Dosha. This Dosha can also be remedied by Kal Rudra Yagna performed in these temples.
        Rudra Avisek of Shiva, in any Shiva Temple, and chanting of powerful mantras like the Mrityunjay Mantra, Vishnu Panchakshari Mantra, and Sarp Mantra are the other popular remedies for this Dosha.
        Specifically, Takshaka Kaal Sarpa dosha can be solved or atleast impact be reduced by reciting Sunderkand of Ramcharitmanas on Tuesday or Saturday 108 times. Read Ganapati Atharvashirsha on every full moon.
        Wear an energized Silver Rahu Yantra around your neck.
        '''
        
        relevant_planets = ["Su", "Mo", "Ma", "Me", "Ju", "Ve", "Sa", "Ra", "Ke"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"TAKSHAKAKAALSARPA",relevant_planets, colorlist)


        #Update the yogadosha sections
        data.yogadoshas["TAKSHAKAKAALSARPA"] = {}
        data.yogadoshas["TAKSHAKAKAALSARPA"]["name"] = Name
        data.yogadoshas["TAKSHAKAKAALSARPA"]["type"] = "Dosha"
        data.yogadoshas["TAKSHAKAKAALSARPA"]["exist"] = IsTakshakaKaalSarpaDoshaPresent
        data.yogadoshas["TAKSHAKAKAALSARPA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["TAKSHAKAKAALSARPA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["TAKSHAKAKAALSARPA"]["Remedies"] = gen.iterativeReplace(Remedies,"\n ", "\n").replace("\n","\n        ")
        data.yogadoshas["TAKSHAKAKAALSARPA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["TAKSHAKAKAALSARPA"]["Source"] = "https://astrotalk.com/kaal-sarp-dosh-12-types"
    
    return IsTakshakaKaalSarpaDoshaPresent

#Karkotak Kaal sarpa dosha - Kaalsarpa dosha with Rahu in Santaan bhav
def KarkotakKaalSarpaDosha(charts):
    IsKarkotakKaalSarpaDoshaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    Remedies = ""

    KaalSarpDoshaSts = kaalSarpaDosha(charts)
    if (KaalSarpDoshaSts != "ABSENT") and (charts["D1"]["planets"]["Rahu"]["house-num"] == 8):
        IsKarkotakKaalSarpaDoshaPresent = True
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[8-1] = "yellow"
        colorlist[2-1] = "yellow"
        #Update the Name and Rule
        if (KaalSarpDoshaSts == "ASCENDPRESENT"):
            Name = "Ascending Karkotak Kaala Sarpa"
            typ = "Ascending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 8th house and Ketu is in 2nd house this is Karkotak Kaala Sarpa Dosha. All the planets are right side of Rahu-Ketu Axis heading towards Rahu So its Ascending Karkotak Kaala Sarpa Dosha.
            '''
        else:
            Name = "Descending Karkotak Kaala Sarpa"
            typ = "Descending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 8th house and Ketu is in 2nd house this is Karkotak Kaala Sarpa Dosha. All the planets are left side of Rahu-Ketu Axis heading towards Ketu So its Descending Karkotak Kaala Sarpa Dosha.
            '''
        #Update the Results of Karkotak Kaala Sarpa Dosha
        Results = f'''Kaal Sarp Dosha is a frightful astrological event that affects a person severely with multifaceted catastrophes. It is a result of bad karma done by the native in the previous lives.
        As Kaalsarp dosh veils the planets, the aspects other planets represent may get hampered, which may lead to problems in the life of the native. So the results from aspects of other planets will be blocked by Rahu-Ketu axis and the native will not be ble to get full results of other planets in his kundali.
        The Karkotak kaala sarpa dosha is responsible for causing hindrance in acquiring a fortune. The dosh may also hamper career progress as you may witness several hindrances in acquiring a job and getting a well-deserved promotion. 
        People dealing with Karkotak Kaalsarp dosha also acquire the habit of speaking the truth. This may seem like a good thing, but this habit may bar the native from acquiring good deals for himself. This doesn't mean that you shouldn't speak the truth, but you must surely think before speaking to anyone.
        This Dosha affects mental wellbeing. An irritable nature and outspoken character work detrimentally for individuals who receive no success despite hard work. They would also face ups and downs in finance, legal issues, etc
        '''
        #Update the Note
        Note = "The effect of Karkotak Kaala Sarpa Dosha will decrease after the age of 33 if other strong Yogas are present in Native's Kundali."
        #update Remedies for Dosha
        Remedies = f'''One of the most effective remedies to reduce the effects of the Kala Sarpa Dosha is visiting shrines of higher spiritual beings. The popular places to visit include Srikalahasti temple, Trimbakeshwar temple, Rameswaram, and Thirunageswaram. The Kalasarpa Dosha Nivaran Puja at Sri Kalahasti mandir, Rameswaram, and Thirunageswaram, is considered the best remedy for Kala Sarpa Dosha. This Dosha can also be remedied by Kal Rudra Yagna performed in these temples.
        Rudra Avisek of Shiva, in any Shiva Temple, and chanting of powerful mantras like the Mrityunjay Mantra, Vishnu Panchakshari Mantra, and Sarp Mantra are the other popular remedies for this Dosha.
        Specifically, Karkotak Kaal Sarpa dosha can be solved or atleast impact be reduced by wearing Shiva Yantra made of silver around the neck. 
        Starting from Saturday, feed Boondi Laddoos to the ants for 27 days. Also wear a triangular Coral gemstone in copper on the middle finger of the right hand.
        '''
        
        relevant_planets = ["Su", "Mo", "Ma", "Me", "Ju", "Ve", "Sa", "Ra", "Ke"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"KARKOTAKKAALSARPA",relevant_planets, colorlist)


        #Update the yogadosha sections
        data.yogadoshas["KARKOTAKKAALSARPA"] = {}
        data.yogadoshas["KARKOTAKKAALSARPA"]["name"] = Name
        data.yogadoshas["KARKOTAKKAALSARPA"]["type"] = "Dosha"
        data.yogadoshas["KARKOTAKKAALSARPA"]["exist"] = IsKarkotakKaalSarpaDoshaPresent
        data.yogadoshas["KARKOTAKKAALSARPA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["KARKOTAKKAALSARPA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["KARKOTAKKAALSARPA"]["Remedies"] = gen.iterativeReplace(Remedies,"\n ", "\n").replace("\n","\n        ")
        data.yogadoshas["KARKOTAKKAALSARPA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["KARKOTAKKAALSARPA"]["Source"] = "https://astrotalk.com/kaal-sarp-dosh-12-types"
    
    return IsKarkotakKaalSarpaDoshaPresent

#Shankhachur Kaal sarpa dosha - Kaalsarpa dosha with Rahu in Santaan bhav
def ShankhachurKaalSarpaDosha(charts):
    IsShankhachurKaalSarpaDoshaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    Remedies = ""

    KaalSarpDoshaSts = kaalSarpaDosha(charts)
    if (KaalSarpDoshaSts != "ABSENT") and (charts["D1"]["planets"]["Rahu"]["house-num"] == 9):
        IsShankhachurKaalSarpaDoshaPresent = True
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[9-1] = "yellow"
        colorlist[3-1] = "yellow"
        #Update the Name and Rule
        if (KaalSarpDoshaSts == "ASCENDPRESENT"):
            Name = "Ascending Shankhachur Kaala Sarpa"
            typ = "Ascending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 9th house and Ketu is in 3rd house this is Shankhachur Kaala Sarpa Dosha. All the planets are right side of Rahu-Ketu Axis heading towards Rahu So its Ascending Shankhachur Kaala Sarpa Dosha.
            '''
        else:
            Name = "Descending Shankhachur Kaala Sarpa"
            typ = "Descending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 9th house and Ketu is in 3rd house this is Shankhachur Kaala Sarpa Dosha. All the planets are left side of Rahu-Ketu Axis heading towards Ketu So its Descending Shankhachur Kaala Sarpa Dosha.
            '''
        #Update the Results of Shankhachur Kaala Sarpa Dosha
        Results = f'''Kaal Sarp Dosha is a frightful astrological event that affects a person severely with multifaceted catastrophes. It is a result of bad karma done by the native in the previous lives.
        As Kaalsarp dosh veils the planets, the aspects other planets represent may get hampered, which may lead to problems in the life of the native. So the results from aspects of other planets will be blocked by Rahu-Ketu axis and the native will not be ble to get full results of other planets in his kundali.
        The Shankhachur kaala sarpa dosha good thing is that the desires of people born in this dosh are usually fulfilled. However, the bad thing is that there may be a delay in fulfilling such desires, which may leave you frustrated. 
        In the family and home of the native dealing with Shankhachur Kaalsarp dosh, there may be a lot of pain and suffering. In this period, it is suggested that you focus on your family and don't indulge in dealings that you will have to regret in the near future.
        The individuals with this Yoga would face troubles in business and sudden downfall from power and position. They may have to fight for their rights. Upon enduring these troubles, these individuals can become increasingly selfish
        '''
        #Update the Note
        Note = "The effect of Shankhachur Kaala Sarpa Dosha will decrease after the age of 36 if other strong Yogas are present in Native's Kundali."
        #update Remedies for Dosha
        Remedies = f'''One of the most effective remedies to reduce the effects of the Kala Sarpa Dosha is visiting shrines of higher spiritual beings. The popular places to visit include Srikalahasti temple, Trimbakeshwar temple, Rameswaram, and Thirunageswaram. The Kalasarpa Dosha Nivaran Puja at Sri Kalahasti mandir, Rameswaram, and Thirunageswaram, is considered the best remedy for Kala Sarpa Dosha. This Dosha can also be remedied by Kal Rudra Yagna performed in these temples.
        Rudra Avisek of Shiva, in any Shiva Temple, and chanting of powerful mantras like the Mrityunjay Mantra, Vishnu Panchakshari Mantra, and Sarp Mantra are the other popular remedies for this Dosha.
        Specifically, Shankhachur Kaal Sarpa dosha can be solved or atleast impact be reduced by reciting Hanuman Chalisa daily
        Regularly recite Mahamrityunjaya Mantra and observe fasting every Monday. Also Wear an energised Silver Rahu Yantra around your neck on Saturday.
        '''
        
        relevant_planets = ["Su", "Mo", "Ma", "Me", "Ju", "Ve", "Sa", "Ra", "Ke"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"SHANKACHURKAALSARPA",relevant_planets, colorlist)


        #Update the yogadosha sections
        data.yogadoshas["SHANKACHURKAALSARPA"] = {}
        data.yogadoshas["SHANKACHURKAALSARPA"]["name"] = Name
        data.yogadoshas["SHANKACHURKAALSARPA"]["type"] = "Dosha"
        data.yogadoshas["SHANKACHURKAALSARPA"]["exist"] = IsShankhachurKaalSarpaDoshaPresent
        data.yogadoshas["SHANKACHURKAALSARPA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["SHANKACHURKAALSARPA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["SHANKACHURKAALSARPA"]["Remedies"] = gen.iterativeReplace(Remedies,"\n ", "\n").replace("\n","\n        ")
        data.yogadoshas["SHANKACHURKAALSARPA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["SHANKACHURKAALSARPA"]["Source"] = "https://astrotalk.com/kaal-sarp-dosh-12-types"
    
    return IsShankhachurKaalSarpaDoshaPresent

#Ghatak Kaal sarpa dosha - Kaalsarpa dosha with Rahu in Santaan bhav
def GhatakKaalSarpaDosha(charts):
    IsGhatakKaalSarpaDoshaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    Remedies = ""

    KaalSarpDoshaSts = kaalSarpaDosha(charts)
    if (KaalSarpDoshaSts != "ABSENT") and (charts["D1"]["planets"]["Rahu"]["house-num"] == 10):
        IsGhatakKaalSarpaDoshaPresent = True
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[10-1] = "yellow"
        colorlist[4-1] = "yellow"
        #Update the Name and Rule
        if (KaalSarpDoshaSts == "ASCENDPRESENT"):
            Name = "Ascending Ghatak Kaala Sarpa"
            typ = "Ascending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 10th house and Ketu is in 4th house this is Ghatak Kaala Sarpa Dosha. All the planets are right side of Rahu-Ketu Axis heading towards Rahu So its Ascending Ghatak Kaala Sarpa Dosha.
            '''
        else:
            Name = "Descending Ghatak Kaala Sarpa"
            typ = "Descending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 10th house and Ketu is in 4th house this is Ghatak Kaala Sarpa Dosha. All the planets are left side of Rahu-Ketu Axis heading towards Ketu So its Descending Ghatak Kaala Sarpa Dosha.
            '''
        #Update the Results of Ghatak Kaala Sarpa Dosha
        Results = f'''Kaal Sarp Dosha is a frightful astrological event that affects a person severely with multifaceted catastrophes. It is a result of bad karma done by the native in the previous lives.
        As Kaalsarp dosh veils the planets, the aspects other planets represent may get hampered, which may lead to problems in the life of the native. So the results from aspects of other planets will be blocked by Rahu-Ketu axis and the native will not be ble to get full results of other planets in his kundali.
        Since you have Ghatak kaala sarpa dosha, it is highly recommended that you serve your mother, take care of her and never cause her any harm. This will help in bettering your life conditions. However, it has been noticed that in return, you may not get the same kind of affection from your mother. 
        Due to Ghatak Kaalsarp dosha, the person becomes arrogant even if he or she does not have anything to be proud of. Your ego is at the top of your head, which may hamper not only your personal but your professional bondings too.
        Despite the achieved success, the individuals with this Dosha would find it hard to be happy. There would be problems in professional and family lives. Excessive interference from family members may make their life miserable.
        '''
        #Update the Note
        Note = "The effect of Ghatak Kaala Sarpa Dosha will decrease after the age of 42 if other strong Yogas are present in Native's Kundali."
        #update Remedies for Dosha
        Remedies = f'''One of the most effective remedies to reduce the effects of the Kala Sarpa Dosha is visiting shrines of higher spiritual beings. The popular places to visit include Srikalahasti temple, Trimbakeshwar temple, Rameswaram, and Thirunageswaram. The Kalasarpa Dosha Nivaran Puja at Sri Kalahasti mandir, Rameswaram, and Thirunageswaram, is considered the best remedy for Kala Sarpa Dosha. This Dosha can also be remedied by Kal Rudra Yagna performed in these temples.
        Rudra Avisek of Shiva, in any Shiva Temple, and chanting of powerful mantras like the Mrityunjay Mantra, Vishnu Panchakshari Mantra, and Sarp Mantra are the other popular remedies for this Dosha.
        Specifically, Ghatak Kaal Sarpa dosha can be solved or atleast impact be reduced by always reading the Hanuman Chalisa and observe fast each Tuesday.
        Read Ganapati Atharvashirsha on every full moon. Also on Friday, donate coconut, blanket etc. along with epilogue, oil, black cloth, and peel.
        '''
        
        relevant_planets = ["Su", "Mo", "Ma", "Me", "Ju", "Ve", "Sa", "Ra", "Ke"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"GHATAKKAALSARPA",relevant_planets, colorlist)


        #Update the yogadosha sections
        data.yogadoshas["GHATAKKAALSARPA"] = {}
        data.yogadoshas["GHATAKKAALSARPA"]["name"] = Name
        data.yogadoshas["GHATAKKAALSARPA"]["type"] = "Dosha"
        data.yogadoshas["GHATAKKAALSARPA"]["exist"] = IsGhatakKaalSarpaDoshaPresent
        data.yogadoshas["GHATAKKAALSARPA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["GHATAKKAALSARPA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["GHATAKKAALSARPA"]["Remedies"] = gen.iterativeReplace(Remedies,"\n ", "\n").replace("\n","\n        ")
        data.yogadoshas["GHATAKKAALSARPA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["GHATAKKAALSARPA"]["Source"] = "https://astrotalk.com/kaal-sarp-dosh-12-types"
    
    return IsGhatakKaalSarpaDoshaPresent

#Vishadhara Kaal sarpa dosha - Kaalsarpa dosha with Rahu in Laab bhav
def VishadharaKaalSarpaDosha(charts):
    IsVishadharaKaalSarpaDoshaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    Remedies = ""

    KaalSarpDoshaSts = kaalSarpaDosha(charts)
    if (KaalSarpDoshaSts != "ABSENT") and (charts["D1"]["planets"]["Rahu"]["house-num"] == 11):
        IsVishadharaKaalSarpaDoshaPresent = True
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[11-1] = "yellow"
        colorlist[5-1] = "yellow"
        #Update the Name and Rule
        if (KaalSarpDoshaSts == "ASCENDPRESENT"):
            Name = "Ascending Vishadhara Kaala Sarpa"
            typ = "Ascending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 11th house and Ketu is in 5th house this is Vishadhara Kaala Sarpa Dosha. All the planets are right side of Rahu-Ketu Axis heading towards Rahu So its Ascending Vishadhara Kaala Sarpa Dosha.
            '''
        else:
            Name = "Descending Vishadhara Kaala Sarpa"
            typ = "Descending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 11th house and Ketu is in 5th house this is Vishadhara Kaala Sarpa Dosha. All the planets are left side of Rahu-Ketu Axis heading towards Ketu So its Descending Vishadhara Kaala Sarpa Dosha.
            '''
        #Update the Results of Vishadhara Kaala Sarpa Dosha
        Results = f'''Kaal Sarp Dosha is a frightful astrological event that affects a person severely with multifaceted catastrophes. It is a result of bad karma done by the native in the previous lives.
        As Kaalsarp dosh veils the planets, the aspects other planets represent may get hampered, which may lead to problems in the life of the native. So the results from aspects of other planets will be blocked by Rahu-Ketu axis and the native will not be ble to get full results of other planets in his kundali.
        The Vishadhara kaala sarpa dosha is fatal for the one trying to acquire education, especially higher education. There will be a lot of obstacles for such a person to get higher education. However, despite all odds, their patience and commitment will help them in moving forward. 
        These people do better in their professional life if they pursue their career from abroad than from their own country. Their fortune trends in foreign countries. In the family, the person has to suffer from property loss even after the possibility of benefiting from grandparents.
         The issues corresponding to this Dosha begin with memory loss, poor educational experience, and plenty of domestic issues on property and wealth. The individuals with this Dosha may also suffer on account of their child.
        '''
        #Update the Note
        Note = "The effect of Vishadhara Kaala Sarpa Dosha will decrease after the age of 48 if other strong Yogas are present in Native's Kundali."
        #update Remedies for Dosha
        Remedies = f'''One of the most effective remedies to reduce the effects of the Kala Sarpa Dosha is visiting shrines of higher spiritual beings. The popular places to visit include Srikalahasti temple, Trimbakeshwar temple, Rameswaram, and Thirunageswaram. The Kalasarpa Dosha Nivaran Puja at Sri Kalahasti mandir, Rameswaram, and Thirunageswaram, is considered the best remedy for Kala Sarpa Dosha. This Dosha can also be remedied by Kal Rudra Yagna performed in these temples.
        Rudra Avisek of Shiva, in any Shiva Temple, and chanting of powerful mantras like the Mrityunjay Mantra, Vishnu Panchakshari Mantra, and Sarp Mantra are the other popular remedies for this Dosha.
        Specifically, Vishadhara Kaal Sarpa dosha can be solved or atleast impact be reduced by feeding barley grains to the needy for 27 days on Saturday.
        On Saturday, circumambulate the raw coal anti-clockwise around your head 8 times, then throw the coal in the running water. Also dont forget to recite Hanuman Chalisa daily.
        '''
        
        relevant_planets = ["Su", "Mo", "Ma", "Me", "Ju", "Ve", "Sa", "Ra", "Ke"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"VISHADHARAKAALSARPA",relevant_planets, colorlist)


        #Update the yogadosha sections
        data.yogadoshas["VISHADHARAKAALSARPA"] = {}
        data.yogadoshas["VISHADHARAKAALSARPA"]["name"] = Name
        data.yogadoshas["VISHADHARAKAALSARPA"]["type"] = "Dosha"
        data.yogadoshas["VISHADHARAKAALSARPA"]["exist"] = IsVishadharaKaalSarpaDoshaPresent
        data.yogadoshas["VISHADHARAKAALSARPA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["VISHADHARAKAALSARPA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["VISHADHARAKAALSARPA"]["Remedies"] = gen.iterativeReplace(Remedies,"\n ", "\n").replace("\n","\n        ")
        data.yogadoshas["VISHADHARAKAALSARPA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["VISHADHARAKAALSARPA"]["Source"] = "https://astrotalk.com/kaal-sarp-dosh-12-types"
    
    return IsVishadharaKaalSarpaDoshaPresent

#Sheshanaga Kaal sarpa dosha - Kaalsarpa dosha with Rahu in Karch bhav
def SheshanagaKaalSarpaDosha(charts):
    IsSheshanagaKaalSarpaDoshaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    Remedies = ""

    KaalSarpDoshaSts = kaalSarpaDosha(charts)
    if (KaalSarpDoshaSts != "ABSENT") and (charts["D1"]["planets"]["Rahu"]["house-num"] == 12):
        IsSheshanagaKaalSarpaDoshaPresent = True
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[12-1] = "yellow"
        colorlist[6-1] = "yellow"
        #Update the Name and Rule
        if (KaalSarpDoshaSts == "ASCENDPRESENT"):
            Name = "Ascending Sheshanaga Kaala Sarpa"
            typ = "Ascending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 12th house and Ketu is in 6th house this is Sheshanaga Kaala Sarpa Dosha. All the planets are right side of Rahu-Ketu Axis heading towards Rahu So its Ascending Sheshanaga Kaala Sarpa Dosha.
            '''
        else:
            Name = "Descending Sheshanaga Kaala Sarpa"
            typ = "Descending"
            Rule = f'''All the remaining 7 planets are in the same side of Rahu-Ketu Axis forming Kaala Sarpa Dosha. Since Rahu is in 12th house and Ketu is in 6th house this is Sheshanaga Kaala Sarpa Dosha. All the planets are left side of Rahu-Ketu Axis heading towards Ketu So its Descending Sheshanaga Kaala Sarpa Dosha.
            '''
        #Update the Results of Sheshanaga Kaala Sarpa Dosha
        Results = f'''Kaal Sarp Dosha is a frightful astrological event that affects a person severely with multifaceted catastrophes. It is a result of bad karma done by the native in the previous lives.
        As Kaalsarp dosh veils the planets, the aspects other planets represent may get hampered, which may lead to problems in the life of the native. So the results from aspects of other planets will be blocked by Rahu-Ketu axis and the native will not be ble to get full results of other planets in his kundali.
        The Sheshanaga kaala sarpa dosha always fulfils natives desires, however, with a slight delay. The native under the presence of this dosh may develop a habit of spending more than his income. This is why he may usually find himself indebted. After 42 years of age, there is a time in his life when he may find himself a prestigious place in society. This, however, will require your constant hard work and commitment.
        This dosha has debilitating effects, both physically and mentally. The individuals face a life of defamation and find it hard to get rid of the same. They will have a lot of hidden enemies, and will never feel satisfied with their lives.
        '''
        #Update the Note
        Note = "The effect of Sheshanaga Kaala Sarpa Dosha will decrease after the age of 54 if other strong Yogas are present in Native's Kundali."
        #update Remedies for Dosha
        Remedies = f'''One of the most effective remedies to reduce the effects of the Kala Sarpa Dosha is visiting shrines of higher spiritual beings. The popular places to visit include Srikalahasti temple, Trimbakeshwar temple, Rameswaram, and Thirunageswaram. The Kalasarpa Dosha Nivaran Puja at Sri Kalahasti mandir, Rameswaram, and Thirunageswaram, is considered the best remedy for Kala Sarpa Dosha. This Dosha can also be remedied by Kal Rudra Yagna performed in these temples.
        Rudra Avisek of Shiva, in any Shiva Temple, and chanting of powerful mantras like the Mrityunjay Mantra, Vishnu Panchakshari Mantra, and Sarp Mantra are the other popular remedies for this Dosha.
        Specifically, Sheshanaga Kaal Sarpa dosha can be solved or atleast impact be reduced by hanging Hanuman Bahuk wrapped in red cloth on any Tuesday on the wall towards the south side of the house
        Feed the raw bread of barley flour to the birds for 3 months. Also you can wear an energised Shiva Yantra made of silver around the neck.
        '''
        
        relevant_planets = ["Su", "Mo", "Ma", "Me", "Ju", "Ve", "Sa", "Ra", "Ke"]
        dc.create_SimpleYogaDoshaChart(charts["D1"],"SHESHANAGAKAALSARPA",relevant_planets, colorlist)


        #Update the yogadosha sections
        data.yogadoshas["SHESHANAGAKAALSARPA"] = {}
        data.yogadoshas["SHESHANAGAKAALSARPA"]["name"] = Name
        data.yogadoshas["SHESHANAGAKAALSARPA"]["type"] = "Dosha"
        data.yogadoshas["SHESHANAGAKAALSARPA"]["exist"] = IsSheshanagaKaalSarpaDoshaPresent
        data.yogadoshas["SHESHANAGAKAALSARPA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["SHESHANAGAKAALSARPA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["SHESHANAGAKAALSARPA"]["Remedies"] = gen.iterativeReplace(Remedies,"\n ", "\n").replace("\n","\n        ")
        data.yogadoshas["SHESHANAGAKAALSARPA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["SHESHANAGAKAALSARPA"]["Source"] = "https://astrotalk.com/kaal-sarp-dosh-12-types"
    
    return IsSheshanagaKaalSarpaDoshaPresent

#Gajakesari Yoga - Jupiter is in Kendra with respect to Moon in D1 chart
def GajaKesariYoga(charts):
    IsGajaKesariYogaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    cnt = 0
    good_cnt = 0
    relevant_planets = ["Ju", "Mo"]
    #Check for existance of Gajakesari Yoga
    lagnaJupiter = charts["D1"]["planets"]["Jupiter"]
    lagnaMoon = charts["D1"]["planets"]["Moon"]
    #If Jupiter and Moon are in kendra with respect to each other then Gajakesari is formed. Jupiter must not be Retrograde.
    if(gen.housediff(lagnaJupiter["house-num"], lagnaMoon["house-num"]) in [1,4,7,10]) and (lagnaJupiter["retro"] == 0):
        IsGajaKesariYogaPresent = True
        #update the Rule
        Name = "GajaKesari"
        Rule = f'''Jupiter [House number : {lagnaJupiter["house-num"]}] is in kendra from Moon[House number : {lagnaMoon["house-num"]}] in Native's Kundali. And Jupiter is not retrograde.'''

        benefics = charts["D1"]["classifications"]["benefics"].copy()
        malefics = charts["D1"]["classifications"]["malefics"].copy()
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = lagnaJupiter["Aspected-by"]
        conjuncts = lagnaJupiter["conjuncts"]
        benefics_aspectingJupiter = list(set(benefics).intersection(aspectedby))
        benefics_conjunctJupiter = list(set(benefics).intersection(conjuncts))
        malefics_aspectingJupiter = list(set(malefics).intersection(aspectedby))
        malefics_conjunctJupiter = list(set(malefics).intersection(conjuncts))

        if (len(benefics_aspectingJupiter)>0) or (len(benefics_conjunctJupiter)>0):
            Rule = f'''{Rule}Jupiter is associated by Benefics by conjunction or aspect.'''
            good_cnt = good_cnt + 1
        
        #If any malefic is aspecting or conjunct with Jupiter then Gajakesari yoga is weakened
        if (len(malefics_aspectingJupiter)>0) or (len(malefics_conjunctJupiter)>0):
            Name = "Weak GajaKesari"
            Rule = f'''{Rule}But Jupiter is afflicted by Malefics.'''
            cnt = cnt + 1
        
        Rule = f'''{Rule}Hence a {Name} Yoga is formed.'''

        #Moon should not be present in the 6th, 8th & 12th houses. it weakens the yoga
        if ((lagnaMoon["house-num"] == 6) or (lagnaMoon["house-num"] == 8) or (lagnaMoon["house-num"] == 12)):
            Note = f'''Moon is present in dushtana House which weakens the yoga. '''
            cnt = cnt + 1

        #The Moon should be at least four houses away from the Sun. Else effects of this yoga weakens
        lagnaSunHouse = charts["D1"]["planets"]["Sun"]["house-num"]
        lagnaMoonHouse = lagnaMoon["house-num"]
        sunToMoon = gen.housediff(lagnaSunHouse, lagnaMoonHouse)
        if (sunToMoon < 4) or (sunToMoon > 9):
            Note = f'''{Note}Moon is present within 4 houses with respect to the Sun which weakens the yoga. '''
            cnt = cnt + 1
            relevant_planets.append("Su")

        #Moon should not be debilitated (Scorpio)
        if(lagnaMoon["sign"] == "Scorpio"):
            Note = f'''{Note}Moon is debilitated, which weakens this yoga. '''
            cnt = cnt + 1

        #Gaja Kesari Yoga should not be formed in Makara as Jupiter acts debilitated in Makara Rashi.
        if(lagnaJupiter["sign"] == "Capricorn"):
            Note = f'''{Note}Jupiter is debilitated, which weakens this yoga. '''
            cnt = cnt + 1
        
        #If Jupiter or Moon is in Pushkar Navamsa or Bhag, the good results of Gajakesari will increase significantly.
        #Check Pushkara navamsha for Jupiter
        if(True == gen.isPushkaraNavamsha(lagnaJupiter["nakshatra"], lagnaJupiter["pada"])):
            Note = f'''{Note}Jupiter is in Pushkara Navamsa, which strengthens this yoga. '''
            good_cnt = good_cnt + 1
        #Check Pushkara navamsha for Moon
        if(True == gen.isPushkaraNavamsha(lagnaMoon["nakshatra"], lagnaMoon["pada"])):
            Note = f'''{Note}Moon is in Pushkara Navamsa, which strengthens this yoga. '''
            good_cnt = good_cnt + 1
        #Check Pushkara Bhag for Jupiter
        if(True == gen.isPushkaraBhaga(lagnaJupiter["sign-tatva"], lagnaJupiter["pos"]["deg"])):
            Note = f'''{Note}Jupiter is in Pushkara Bhaga, which strengthens this yoga. '''
            good_cnt = good_cnt + 1
        #Check Pushkara Bhag for Moon
        if(True == gen.isPushkaraBhaga(lagnaMoon["sign-tatva"], lagnaMoon["pos"]["deg"])):
            Note = f'''{Note}Moon is in Pushkara Bhaga, which strengthens this yoga. '''
            good_cnt = good_cnt + 1

        if(lagnaMoon["sign"] == "Taurus"):
            Note = f'''{Note}Moon is exhalted, which strengthens this yoga. '''
            good_cnt = good_cnt + 1

        if(lagnaJupiter["sign"] == "Cancer"):
            Note = f'''{Note}Jupiter is exhalted, which strengthens this yoga. '''
            good_cnt = good_cnt + 1

        Note = f'''{Note}Benefic planets aspecting Jupiter: {benefics_aspectingJupiter} and conjunct benefics: {benefics_conjunctJupiter}. Malefic planets aspecting Jupiter: {malefics_aspectingJupiter} and conjunct malefics: {malefics_conjunctJupiter}.
        Consider all these points [{good_cnt} positive and {cnt} negative] carefully before concluding the results of this Gajakesari yoga.'''

        #getting full list of relevant planets for this yoga        
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[lagnaJupiter["house-num"]-1] = "yellow"
        colorlist[lagnaMoon["house-num"]-1] = "yellow"
        dc.create_SimpleYogaDoshaChart(charts["D1"],"GAJAKESARI",relevant_planets, colorlist)

        #Update the results of Gajakesari Yoga
        Results = f'''The word Gajakesari means Gaja for Elephant, and Kesari means Lion. Both Elephant and Lion are powerful and represent authority and intelligence. 
        People with Gaja Kesari Yoga seek good wealth, courage, respect from others and are generally good speakers.
        You will never have to worry about money if you have a strong Gajakesari Yoga in your horoscope chart. Even when there are anxious moments and finances are unstable, you will receive last-minute monetary help, putting an end to your anxiety.
        The effects of Gajakesari Yoga are not just limited to monetary gains. ith this yoga, you will be a courageous and happy person who is full of life and vigour. This yoga will make you a leader who can motivate people and change their lives through your inspirational speeches.'''

        #Update the yogadosha sections
        data.yogadoshas["GAJAKESARI"] = {}
        data.yogadoshas["GAJAKESARI"]["name"] = Name
        data.yogadoshas["GAJAKESARI"]["type"] = "Yoga"
        data.yogadoshas["GAJAKESARI"]["exist"] = IsGajaKesariYogaPresent
        data.yogadoshas["GAJAKESARI"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["GAJAKESARI"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["GAJAKESARI"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["GAJAKESARI"]["Source"] = "https://astrotalk.com/astrology-blog/know-who-can-seek-benefits-of-gajakesari-yoga-as-per-astrology/"   
    
    return IsGajaKesariYogaPresent

#ChandraMangala Yoga - Mars and  Moon conjunct in D1 chart
def ChandraMangalaYoga(charts):
    IsChandraMangalaYogaPresent = False
    Name = ""
    Rule = ""
    Results = ""
    Note = ""
    bad_cnt = 0
    good_cnt = 0
    relevant_planets = ["Ma", "Mo"]

    #Check for existance of this yoga
    lagnamars = charts["D1"]["planets"]["Mars"]
    lagnamoon = charts["D1"]["planets"]["Moon"]

    if(lagnamars["sign"] == lagnamoon["sign"]):
        IsChandraMangalaYogaPresent = True
        Name = "Chandra Mangala"
        Rule = "In native's chart Moon is conjunct with Mars. So Chandra Mangala Yoga is formed."

        #if Moon is debilitated then Effects reduce
        if(lagnamoon["sign"] == "Scorpio"):
            Note = f'''{Note}Moon is debilitated, which weakens this yoga. '''
            bad_cnt = bad_cnt + 1

        if(lagnamoon["sign"] == "Taurus"):
            Note = f'''{Note}Moon is exhalted, which strengthens this yoga. '''
            good_cnt = good_cnt + 1

        #If Mars is debilitates. then Effects reduce
        if(lagnamars["sign"] == "Cancer"):
            Note = f'''{Note}Mars is debilitated, which weakens this yoga. '''
            bad_cnt = bad_cnt + 1

        if(lagnamars["sign"] == "Capricorn"):
            Note = f'''{Note}Mars is exhalted, which strengthens this yoga. '''
            good_cnt = good_cnt + 1

        benefics = charts["D1"]["classifications"]["benefics"].copy()
        malefics = charts["D1"]["classifications"]["malefics"].copy()
        malefics.append("Rahu")
        malefics.append("Ketu")
        aspectedby = lagnamars["Aspected-by"]
        conjuncts = lagnamars["conjuncts"]
        benefics_aspectingMars = list(set(benefics).intersection(aspectedby))
        benefics_conjunctMars = list(set(benefics).intersection(conjuncts))
        malefics_aspectingMars = list(set(malefics).intersection(aspectedby))
        malefics_conjunctMars = list(set(malefics).intersection(conjuncts))

        if (len(benefics_aspectingMars)>0) or (len(benefics_conjunctMars)>0):
            Note = f'''{Note}Moon and Mars are associated by Benefics by conjunction or aspect.'''
            good_cnt = good_cnt + 1
        
        #If any malefic is aspecting or conjunct with Mars
        if (len(malefics_aspectingMars)>0) or (len(malefics_conjunctMars)>0):
            Note = f'''{Note}Moon and Mars is afflicted by Malefics.'''
            bad_cnt = bad_cnt + 1

        #if mars or moon is a malefic in this chart then this yoga weakens and if benefics then it strengthens
        if("Mars" in benefics):
            Note = f'''{Note}In this chart Mars is a benefic planet and '''
            good_cnt = good_cnt + 1
        elif("Mars" in malefics):
            Note = f'''{Note}In this chart Mars is a malefic planet and '''
            bad_cnt = bad_cnt + 1
        else:
            Note = f'''{Note}In this chart Mars is a neutral planet and '''
        
        if("Moon" in benefics):
            Note = f'''{Note}Moon is a benefic planet. '''
            good_cnt = good_cnt + 1
        elif("Moon" in malefics):
            Note = f'''{Note}Moon is a malefic planet. '''
            bad_cnt = bad_cnt + 1
        else:
            Note = f'''{Note}Moon is a neutral planet. '''

        Note = f'''{Note}Benefic planets aspecting Moon and Mars: {benefics_aspectingMars} and conjunct benefics: {benefics_conjunctMars}. Malefic planets aspecting Moon and Mars: {malefics_aspectingMars} and conjunct malefics: {malefics_conjunctMars}.
        Consider all these points [{good_cnt} positive and {bad_cnt} negative] carefully before concluding the results of this Chandra Mangala yoga.'''

        #getting full list of relevant planets for this yoga        
        for planet in aspectedby:
            relevant_planets.append(planet[0:2])
        for planet in conjuncts:
            relevant_planets.append(planet[0:2])
        colorlist = ["pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink","pink"]
        colorlist[lagnamars["house-num"]-1] = "yellow"
        dc.create_SimpleYogaDoshaChart(charts["D1"],"CHANDRAMANGALA",relevant_planets, colorlist)
        
        #Update the results of Gajakesari Yoga
        Results = f'''Chandra Mangal Yoga is significant in many ways. Apart from financial gains, the native gains a great deal of respect and fame in society. The Moon is associated with riches, happiness and mental strength, whereas Mars is associated with the ability to work hard and achieve all of your life's objectives.
        This Yoga gives birth to a person who is immensely wealthy, clever, and powerful. He has a high level of self-assurance, which allows him to operate effectively in even the most difficult conditions. Because this is a wealth-related Yoga, a person born under this sign is capable of making money on his own. The native is also likely to feel irritable as a result of this Yoga. The native may become obstinate due to the relationship between Mars and the Moon. The native will be brave and capable of solving issues more effectively. Others will not be able to assist the native. The native will make his or her own way in life. This Yoga has a bad impact on the local mother.
        '''

        if(lagnamars["house-num"] == 1):
            Results = f'''{Results}The Chandra Mangal Yoga in the first house will bring the best results in terms of name, popularity, stature, and success in public life and politics. At a higher level, natives may be involved in administrative or defence services.
            '''
        elif(lagnamars["house-num"] == 2):
            Results = f'''{Results}The Moon-Mars conjunction in the second house has the potential to make the native a millionaire and provide them with a life of luxury and riches.
            '''
        elif(lagnamars["house-num"] == 3):
            Results = f'''{Results}Chandra-Mangal yoga in the third house bestows the highest levels of valour, vigour and courage on the inhabitants, enabling them to attain any life goals or ambitions.
            '''
        elif(lagnamars["house-num"] == 4):
            Results = f'''{Results}This Yoga combination in the fourth house brings amenities such as automobiles, property, and more than one house, as well as a large number of agricultural products.
            '''
        elif(lagnamars["house-num"] == 5):
            Results = f'''{Results}The Moon-Mars conjunction in the 5th house bestows pleasure and success in creative endeavours, artistic careers, and love affairs.
            '''
        elif(lagnamars["house-num"] == 6):
            Results = f'''{Results}Moon-Mars in the 6th house brings enmity, lawsuits, legal issues, divorces and other problems. It can, however, help you win competitions in sports, academics or examinations.
            '''
        elif(lagnamars["house-num"] == 7):
            Results = f'''{Results}The Chandra-Mangal yoga in the 7th house is likely to provide positive outcomes and benefits from marriage, but there will be some health issues for the husband, as well as a lack of mutual trust and understanding.
            '''
        elif(lagnamars["house-num"] == 8):
            Results = f'''{Results}This conjunction in the 8th house indicates gains from in-laws, as well as riches and property received through inheritance or as a gift from the government.
            '''
        elif(lagnamars["house-num"] == 9):
            Results = f'''{Results}They will strive to make money in a noble and honest manner. They will pose a serious challenge to their rivals.
            This conjunction in the 9th house brings Raj Yog to dignitaries with a rich culture and class, making natives renowned and occasionally famous in their line of work.
            '''
        elif(lagnamars["house-num"] == 10):
            Results = f'''{Results}They will strive to make money in a noble and honest manner. They will pose a serious challenge to their rivals.
            In the 10th house, the Moon-Mars conjunction is favourable for becoming a doctor or surgeon. It provides a significant boost to native's careers, particularly in public or mass transactions.
            '''
        elif(lagnamars["house-num"] == 11):
            Results = f'''{Results}They will strive to make money in a noble and honest manner. They will pose a serious challenge to their rivals.
            If the Moon-Mars conjunction happens in the 11th house, you can become exceedingly wealthy from a young age after the age of 28. With a lot of wealth and power in life, you'll have a lot of money every day.
            '''
        elif(lagnamars["house-num"] == 12):
            Results = f'''{Results}Chandra Mangal Yoga in the 12th house leads to religious enlightenment and salvation in old age, but it also provides earnings from foreign resources or foreign places in the early and intermediate stages of life, particularly in the import-export business.
            '''
        else:
            Results = f'''{Results}It should not come here. The results are not valid. 
            '''


        #Update the yogadosha sections
        data.yogadoshas["CHANDRAMANGALA"] = {}
        data.yogadoshas["CHANDRAMANGALA"]["name"] = Name
        data.yogadoshas["CHANDRAMANGALA"]["type"] = "Yoga"
        data.yogadoshas["CHANDRAMANGALA"]["exist"] = IsChandraMangalaYogaPresent
        data.yogadoshas["CHANDRAMANGALA"]["Rule"] = gen.iterativeReplace(Rule,"\n ", "\n")
        data.yogadoshas["CHANDRAMANGALA"]["Result"] = gen.iterativeReplace(Results,"\n ", "\n").replace("\n","\n        ") 
        data.yogadoshas["CHANDRAMANGALA"]["Note"] = gen.iterativeReplace(Note,"\n ", "\n")
        data.yogadoshas["CHANDRAMANGALA"]["Source"] = "https://www.mypandit.com/kundli/yoga/chandra-mangal/"  
    
    return IsChandraMangalaYogaPresent

#Main function to load and compute all yogas and doshas and update the json file
def ComputeYogaDoshas(charts):
    #Get the existing Data from Yogadosha json file.
    #js.load_yogadoshas()
    data.charts["yogadoshas"] = []

    #Lets check for various Yogas
    #Pancha-mahapurusha yogas
    if(RuchakaYoga(data.charts)==True): #Ruchaka by Mars
        data.charts["yogadoshas"].append("Ruchaka Panchamahapurusha Yoga")    
    if(BhadraYoga(data.charts)==True):  #Bhadra by Mercury
        data.charts["yogadoshas"].append("Bhadra Panchamahapurusha Yoga") 
    if(HamsaYoga(data.charts)==True):    #Hamsa by Jupiter
        data.charts["yogadoshas"].append("Hamsa Panchamahapurusha Yoga")
    if(MalavyaYoga(data.charts)==True):    #Malavya by Venus
        data.charts["yogadoshas"].append("Malavya Panchamahapurusha Yoga")   
    if(SasaYoga(data.charts)==True):    #Sasa by Saturn
        data.charts["yogadoshas"].append("Sasa Panchamahapurusha Yoga")

    #Vipareeta Raja yogas
    if(HarshaYoga(data.charts)==True): #HarshaYoga by Dusthana Lord in 6th house
        data.charts["yogadoshas"].append("Harsha Vipareeta RajaYoga")
    if(SaralaYoga(data.charts)==True): #SaralaYoga by Dusthana Lord in 8th house
        data.charts["yogadoshas"].append("Sarala Vipareeta RajaYoga")
    if(VimalaYoga(data.charts)==True): #VimalaYoga by Dusthana Lord in 12th house
        data.charts["yogadoshas"].append("Vimala Vipareeta RajaYoga")
    
    #Gaja Kesari Yoga
    if(GajaKesariYoga(data.charts)==True): #GajaKesari by Moon and Jupiter
        data.charts["yogadoshas"].append("GajaKesari Yoga")

    #Chandra Mangala Yoga
    if(ChandraMangalaYoga(data.charts)==True): #Chandramangala by Moon and Mars
        data.charts["yogadoshas"].append("ChandraMangala Yoga")
    
    #Kaal Sarpa Doshas
    if(AnantaKaalSarpaDosha(data.charts)==True): #AnantaKaalSarpaDosha Rahu ketu axis (1-7)
        data.charts["yogadoshas"].append("Ananta Kaala Sarpa Dosha")
    elif(KulikaKaalSarpaDosha(data.charts)==True): #KulikaKaalSarpaDosha Rahu ketu axis (2-8)
        data.charts["yogadoshas"].append("Kulika Kaala Sarpa Dosha")
    elif(VasukiKaalSarpaDosha(data.charts)==True): #VasukiKaalSarpaDosha Rahu ketu axis (3-9)
        data.charts["yogadoshas"].append("Vasuki Kaala Sarpa Dosha")
    elif(ShankhapalaKaalSarpaDosha(data.charts)==True): #ShankhapalaKaalSarpaDosha Rahu ketu axis (4-10)
        data.charts["yogadoshas"].append("Shankhapala Kaala Sarpa Dosha")
    elif(PadamKaalSarpaDosha(data.charts)==True): #PadamKaalSarpaDosha Rahu ketu axis (5-11)
        data.charts["yogadoshas"].append("Padam Kaala Sarpa Dosha")
    elif(MahapadmaKaalSarpaDosha(data.charts)==True): #MahapadmaKaalSarpaDosha Rahu ketu axis (6-12)
        data.charts["yogadoshas"].append("Mahapadma Kaala Sarpa Dosha")
    elif(TakshakaKaalSarpaDosha(data.charts)==True): #TakshakaKaalSarpaDosha Rahu ketu axis (7-1)
        data.charts["yogadoshas"].append("Takshaka Kaala Sarpa Dosha")
    elif(KarkotakKaalSarpaDosha(data.charts)==True): #KarkotakKaalSarpaDosha Rahu ketu axis (8-2)
        data.charts["yogadoshas"].append("Karkotak Kaala Sarpa Dosha")
    elif(ShankhachurKaalSarpaDosha(data.charts)==True): #ShankhachurKaalSarpaDosha Rahu ketu axis (9-3)
        data.charts["yogadoshas"].append("Shankachur Kaala Sarpa Dosha")
    elif(GhatakKaalSarpaDosha(data.charts)==True): #GhatakKaalSarpaDosha Rahu ketu axis (10-4)
        data.charts["yogadoshas"].append("Ghatak Kaala Sarpa Dosha")
    elif(VishadharaKaalSarpaDosha(data.charts)==True): #VishadharaKaalSarpaDosha Rahu ketu axis (11-5)
        data.charts["yogadoshas"].append("Vishadhara Kaala Sarpa Dosha")
    elif(SheshanagaKaalSarpaDosha(data.charts)==True): #SheshanagaKaalSarpaDosha Rahu ketu axis (12-6)
        data.charts["yogadoshas"].append("Sheshanaga Kaala Sarpa Dosha")
    else:
        print("No Kaal sarpa dosha")

    js.dump_yogadoshas_injson()   
    return
    


if __name__ == "__main__":
    ComputeYogaDoshas(data.charts)
    #print(yogadoshas)