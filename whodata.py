import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('TB_data_dictionary_2018-06-21.csv', index_col=0)
data.pie()
plt.show()