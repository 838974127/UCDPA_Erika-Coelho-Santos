import pandas as pd
cropproduction = pd.read_csv(r"C:\CSV FILES\Crop productionWheat  Maize  Rice  Soybean, Tonneshectare, 2010 – 2021.csv")
print(cropproduction.head(51))

print(cropproduction.tail(51))

print(cropproduction.columns)

cropproduction.shape

cropproduction.dtypes

cropproduction.info()

zero_fill_data = cropproduction.fillna(0)
print(cropproduction)

zero_fill_data.isnull().sum()
print(cropproduction)

cropproduction_filled = cropproduction.fillna(method = "ffill",axis=0).fillna(0)

cropproduction_filled.isnull().sum()
print(cropproduction)

cropproduction_row = cropproduction.dropna(axis=0)

cropproduction_row.shape
print(cropproduction_row)

cropproduction_col = cropproduction.dropna(axis=1)

cropproduction_col.shape
print(cropproduction_col)

cropproduction.duplicated()

cropproduction.info()

cropproduction.loc[0:50,"LOCATION":"Value"]

cropproduction.loc[[100,200,300,400,500,600,700,800,900,1000]]

cropproduction.iloc[0:50,0:7]

# REPLACING MISSING VALUES AT FLAG CODES COLUMN
cropproduction.fillna(value=0, inplace=True)
print(cropproduction)

import pandas as pd
Exports = pd.read_csv(r"C:\CSV FILES\Trade in goods and servicesExports.csv")
print(Exports.head(51))

#Use functions to create reusable code
Exports.info()

import pandas as pd
Imports = pd.read_csv(r"C:\CSV FILES\Trade in goods and servicesImports.csv")
print(Imports.head(51))

#Use functions to create reusable code
Imports.info()
print(Imports)

#SORTING AND INDEXING THE DATAFRAME
df = pd.DataFrame([2010, 2011, 2012, 2013, 2014], index=[100, 200, 300, 400, 500],
                  columns=['TIME'])
df.sort_index()
print(df)

#SORTING AND INDEXING THE DATAFRAME
df2 = pd.DataFrame(['RICE', 'WHEAT', 'MAIZE', 'SOYBEAN'], index=[50, 25, 35, 45],
                  columns=['SUBJECT'])
df2.sort_index()
print(df2)

#GROUPING THE DATAFRAME

CROPPRODUCTION_AUSTRALIA = pd.DataFrame({'CROPYIELD': ['RICE', 'WHEAT',
                              'MAIZE', 'SOYBEAN'],
                   'AMOUNT_IN_10_YEARS': [115.119, 21.644, 76.734, 17.841]})
print(CROPPRODUCTION_AUSTRALIA)

# ITERROWS THE DATA FRAME
#EXPORTS_x_IMPORTS_IRL_in_ten_years
df = pd.DataFrame([[1263.715, 1037.035]], columns=['float', 'float'])
row = next(df.iterrows())[1]
print(row)

# ITERROWS THE DATA FRAME
#EXPORTS_x_IMPORTS_IRL_in_ten_years

df1 = pd.DataFrame([[1263.715, 1037.035]], columns=['float', 'float'])
df2 = pd.DataFrame([['EXPORTS_IRL', 'IMPORTS_IRL']], columns=['str', 'str'])
row = next(df.iterrows())[1]
print(row)
print(df1)
print(df2)

# EMERGING TWO DATAFRAMES
# EXPORTS & IMPORTS - TRADE OF GOODS AND SERVICES IN IRELAND - IRL - MEASURE = PC_GDP.
# CROP PRODUCTION IN IRELAND - IRL - MEASURE = PC_GDP.

TRADEGOODSERV_EXP = pd.DataFrame(
    {'LOCATION_EXP': ['IRL', 'IRL', 'IRL', 'IRL', 'IRL', 'IRL', 'IRL', 'IRL', 'IRL', 'IRL', 'IRL'],
     'SUBJECT_EXP': ['EXP', 'EXP', 'EXP', 'EXP', 'EXP', 'EXP', 'EXP', 'EXP', 'EXP', 'EXP', 'EXP'],
     'value_EXP': [103.0552758, 103.7158107, 104.5166416, 103.6900936, 109.8394784, 121.9558008, 121.2052858,
                   119.7305543, 122.2980151, 126.067883, 127.6398744],
     'TIME_EXP': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]})
TRADEGOODSERV_IMP = pd.DataFrame(
    {'LOCATION_IMP': ['IRL', 'IRL', 'IRL', 'IRL', 'IRL', 'IRL', 'IRL', 'IRL', 'IRL', 'IRL', 'IRL'],
     'SUBJECT_IMP': ['IMP', 'IMP', 'IMP', 'IMP', 'IMP', 'IMP', 'IMP', 'IMP', 'IMP', 'IMP', 'IMP'],
     'value_IMP': [86.43259266, 84.90317448, 87.03321954, 84.87868194, 91.80936538, 93.16454495, 105.5657295,
                   97.88313473, 93.92143907, 113.768928, 97.67392945],
     'TIME-IMP': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]})

print(TRADEGOODSERV_EXP)

print(TRADEGOODSERV_IMP)

print(TRADEGOODSERV_EXP.merge(TRADEGOODSERV_IMP, left_on='LOCATION_EXP', right_on='LOCATION_IMP'))

# EMERGING TWO DATAFRAMES
# EXPORTS & IMPORTS - TRADE OF GOODS AND SERVICES IN IRELAND - IRL - MEASURE = PC_GDP.
# CROP PRODUCTION IN IRELAND - IRL - MEASURE = PC_GDP.

import pandas as pd
cropproduction = pd.read_csv(r"C:\CSV FILES\Crop productionWheat  Maize  Rice  Soybean, Tonneshectare, 2010 – 2021.csv")
print(cropproduction.head(51))

import pandas as pd
Exports = pd.read_csv(r"C:\CSV FILES\Trade in goods and servicesExports.csv")
print(Exports.head(51))

import pandas as pd
Imports = pd.read_csv(r"C:\CSV FILES\Trade in goods and servicesImports.csv")
print(Imports.head(51))

pd.concat([cropproduction,Exports,Imports], axis=0)


#USING FUNCTIONS TO CREATE REUSABLE CODE

df = pd.DataFrame({"EXP_VALUE_X_TIME": [103.055276, 103.715811, 104.516642, 103.690094, 109.839478, 121.955801, 121.205286, 119.730554, 122.298015, 126.067883, 127.639874, 104.516642, 103.690094], "B": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2012, 2013]})
df.to_numpy()
print(df)













