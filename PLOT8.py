import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

Tradegoods_servs_imports_exports = pd.read_csv(r"C:\CSV FILES\Trade in goods and services_Imports_Exports_countries.csv")

x = Tradegoods_servs_imports_exports['Country'].head(11)
y1 = Tradegoods_servs_imports_exports['Imports'].head(11)
y2 = Tradegoods_servs_imports_exports['Exports'].head(11)

# Plot of Trade of Goods and Services_Imports in Australia_sum_from 2010_to 2020.

plt.plot(x,y1, marker="<", linestyle="-", color="darkred", label="Imports")
plt.plot(x,y2,marker=">", linestyle="-.", color="lime", label='Exports')
plt.title("Plot of Trade of Goods and Services_Imports x Exports_Countries_GDP Per Capita")
plt.xlabel("Country")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.show()

print(Tradegoods_servs_imports_exports.head(11))