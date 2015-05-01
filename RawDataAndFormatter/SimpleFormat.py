import csv
import math

inf = csv.reader(open('2004raw.csv',"rU"))
# Data file containing Bureau of Labor Statistics

fileWriter = open('2004dataFormatted.csv','wb')
wr = csv.writer(fileWriter)
label = ["AREA", "ST", "STATE", "OCC_CODE", "OCC_TITLE", "OCC_GROUP", "TOT_EMP","EMP_PRSE"]
wr.writerow(label)

i = 0

for row in inf:
	i = i + 1
	if i > 1:
		if row[6] == "**":
			row[6] = 0
		if row[7] == "**":
			row[7] = 0

# This filters out junk values for the fraction of total employment per job type.
		row[6] = str(row[6]).replace(',','')
		data = row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]
		wr.writerow(data)
