import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as oxl

df = pd.read_excel(r"C:\Users\Haziq\Downloads\Book1.xlsx", engine= 'openpyxl')
print(df)

# rounds the sum of X values by 2 decimal places:        x = round(sum(list(df['X values'])), 2)

x = list(df['X values'])
y = list(df['Y values'])

print(x)
print(y)

plt.figure(figsize=(10, 10))
plt.style.use('seaborn')
plt.scatter(x, y, marker='*', s=100, edgecolors='black', c='yellow')
plt.title('Excel sheet to Scatter Plot')
plt.show()
