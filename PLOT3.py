import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

cropproduction_rice_Brazil = pd.read_csv(r"C:\CSV FILES\Crop production of Rice_Brazil_2010_2020.csv")

x = cropproduction_rice_Brazil['Year'].head(11)
y1 = cropproduction_rice_Brazil['Value'].head(11)

# Plot of Crop production of Rice per year in Brazil.

plt.plot(x,y1, marker="o", linestyle="-", color="darkgreen", label="Value")
plt.title("Plot of Crop production of Rice per year in Brazil")
plt.xlabel("Year")
plt.ylabel("Crop Production of Rice in Brazil_Tonne_Ha")
plt.legend()
plt.show()

print(cropproduction_rice_Brazil.head(11))




