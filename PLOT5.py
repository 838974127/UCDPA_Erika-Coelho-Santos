import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

Tradegoods_servs_ImportsxExports_Australia = pd.read_csv(r"C:\CSV FILES\Trade in goods and services_Imports_Australia.csv")

x = Tradegoods_servs_ImportsxExports_Australia['Year'].head(11)
y1 = Tradegoods_servs_ImportsxExports_Australia['Imports'].head(11)
y2 = Tradegoods_servs_ImportsxExports_Australia['Exports'].head(11)

# Plot of Trade of Goods and Services_Imports versus Exports per year in Australia.

plt.plot(x,y1, marker="<", linestyle="-", color="darkblue", label="Imports")
plt.plot(x,y2,marker=">", linestyle="-.", color="red", label='Exports')
plt.title("Plot of Trade of Goods and Services_Imports x Exports per year in Australia")
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.show()

print(Tradegoods_servs_ImportsxExports_Australia.head(11))
