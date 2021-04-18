# Plot of Trade of Goods and Services_Imports in Australia_sum_from 2010_to 2020.

import matplotlib.pyplot as plt

Country = ['Australia', 'Brazil', 'Spain', 'GBR', 'Ireland', 'Italy', 'Poland', 'Portugal', 'USA']
GDP_Per_Capita = [211.6711, 117.3748, 330.1810, 336.3511, 1037.0350, 298.7284, 519.1966, 438.6399, 157.6629]

New_Colors = ['blue', 'green', 'yellow', 'purple', 'orange', 'red', 'pink', 'brown', 'black']
plt.bar(Country, GDP_Per_Capita, color=New_Colors)
plt.title('Trade of Goods and Services_Imports_Countries GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Imports_GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show()

# Plot of Trade of Goods and Services_Exports in Australia_sum_from 2010_to 2020.

import matplotlib.pyplot as plt

Country = ['Australia', 'Brazil', 'Spain', 'GBR', 'Ireland', 'Italy', 'Poland', 'Portugal', 'USA']
GDP_Per_Capita = [214.202618, 109.600648, 356.496126, 321.654482, 1263.714714, 320.381407, 541.334536, 429.319600,
                  126.907190]

New_Colors = ['blue', 'green', 'yellow', 'purple', 'orange', 'red', 'pink', 'brown', 'black']
plt.bar(Country, GDP_Per_Capita, color=New_Colors)
plt.title('Trade of Goods and Services_Exports_Countries GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Exports_GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show()
