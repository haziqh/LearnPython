import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as oxl

maternal_deaths_by_state = r'C:\Users\Haziq\Downloads\Work\Coding Practice\Number_and_rate_Maternal_deaths_by_state_2010-2018.xlsx'

df = pd.read_excel(maternal_deaths_by_state)

sum_column = df['Maternal deaths'] + df['Maternal mortality ratio']
df['col3'] = sum_column
print(df.describe())

# Describes some useful stats on the data: print(df.describe())

x = df['Year']
y = df['Maternal mortality ratio']
plt.plot(x,y)
plt.show()
