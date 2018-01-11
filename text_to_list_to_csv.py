'''
From a text file, clean the data, and the added it to a .csv file

'''
import csv
import re

IO = open("mytext.txt", "r")
item = IO.readlines()
cleanData = re.compile(r'(.*)\n')
sanatized = []

for i in item:
    data = cleanData.findall(i) 
    sanatized.append(data)
newList = []
for i in range(0,len(sanatized)-1):
        newList.append(sanatized[i][0].split())
        print(newList)

with open('mycsv.csv', 'w') as myfile:
    wr = csv.writer(myfile)
    for u in newList:
        wr.writerow(u)
    