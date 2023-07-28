import pandas as pd
import matplotlib.pyplot as plt

plotdata = pd.DataFrame.from_dict({
            "shadvarga": {
                "Sun": 9.65,
                "Moon": 12.75,
                "Mars": 15.75,
                "Mercury": 15.95,
                "Jupiter": 18.9,
                "Venus": 12.7,
                "Saturn": 17.2,
                "Rahu": 10.3,
                "Ketu": 12.35
            },
            "saptavarga": {
                "Sun": 9.8,
                "Moon": 12.5,
                "Mars": 15.75,
                "Mercury": 15.05,
                "Jupiter": 17.175,
                "Venus": 13.5,
                "Saturn": 15.325,
                "Rahu": 10.45,
                "Ketu": 13.075
            },
            "dashavarga": {
                "Sun": 9.725,
                "Moon": 10.675,
                "Mars": 17.375,
                "Mercury": 15.65,
                "Jupiter": 16.8,
                "Venus": 15.35,
                "Saturn": 14.525,
                "Rahu": 11.35,
                "Ketu": 12.35
            },
            "shodashavarga": {
                "Sun": 9.7,
                "Moon": 10.45,
                "Mars": 17.45,
                "Mercury": 15.725,
                "Jupiter": 16.05,
                "Venus": 14.825,
                "Saturn": 15.275,
                "Rahu": 11.0,
                "Ketu": 12.1
            }
        })

ax = plotdata.plot(kind="bar",figsize=(15, 8))
ax.tick_params(axis='x', labelrotation = 0)

plt.title("Vimshopaka Bala of planets in various Varga-groups")

plt.xlabel("Planets")

plt.ylabel("Vimshopaka Bala")

for p in ax.patches:
    ax.annotate(
        str(p.get_height()), xy=(p.get_x()+0.02 , p.get_height() + 0.3), fontsize=8, rotation=90
    )

plt.savefig('vimshopakabala.png', bbox_inches='tight')
#plt.show()
