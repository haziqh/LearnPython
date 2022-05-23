import pandas as pd


df = pd.read_csv(r'C:\Users\Haziq\Downloads\Documents\Misc\Unredeemed_Keys2.csv')

# Change file path here accordingly

# If file is tab delimited, can replace with df = pd.read_table('input.txt') for '\t'

df.to_excel('output.xlsx', 'Sheet1')

# Change file or sheet name here

# Add 'index=False' to remove index column

