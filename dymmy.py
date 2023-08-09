from scipy.stats import rankdata
somelist = [450, 450, 525, 548, 314, 484, 321, 434, 500, 353, 607, 529]
#rankorderofsomelist = [sorted(somelist).index(x) for x in somelist]
rankorderofsomelist = rankdata(somelist, method='dense')
maxrank = max(rankorderofsomelist)
bhavarank = [(maxrank+1)-x for x in rankorderofsomelist]
print(bhavarank)
