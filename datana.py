import pandas as pd
import matplotlib.pyplot as plt
import requests as rr
url = 'https://tutorials.technology/data/world-population.csv'
response = rr.get(url)

with open('world-population.csv', 'wb') as csv_file:
    csv_file.write(response.content)

population = pd.read_csv('world-population.csv', index_col=0)
plot = population.plot(title='World Population', lw=2, colormap='jet', marker='.', markersize=10)
plot.set_xlabel("Year")
plot.set_ylabel("Population")
plt.savefig('population.png')