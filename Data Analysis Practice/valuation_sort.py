import pandas as pd

'''
valuation = []

valuation.sort()

print(valuation)
'''

def sorting(filename):
  infile = open(filename)
  words = []

  for line in infile:
    temp = line.split()
    for i in temp:
      words.append(i)

  infile.close()

  words.sort()

  outfile = open("result.txt", "w")

  for i in words:
    outfile.writelines(i)
    outfile.writelines(" ")

  outfile.close()

sorting(r'C:\Users\Haziq\Downloads\Documents\Misc\random_numbers_practice.txt')

