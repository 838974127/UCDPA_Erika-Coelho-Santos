import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

cropproduction_rice_Australia = pd.read_csv(r"C:\CSV FILES\Crop production of Rice_Australia_2010_2020.csv")

x = cropproduction_rice_Australia['Year'].head(11)
y1 = cropproduction_rice_Australia['Value'].head(11)

#Plot of Crop production of Rice per year in Australia.

plt.plot(x,y1, marker="o", linestyle="-", color="darkblue", label="Value")
plt.title("Plot of Crop production of Rice per year in Australia")
plt.xlabel("Year")
plt.ylabel("Crop Production of Rice in Australia_Tonne_Ha")
plt.legend()
plt.tight_layout()
plt.show()

print(cropproduction_rice_Australia.head(11))



