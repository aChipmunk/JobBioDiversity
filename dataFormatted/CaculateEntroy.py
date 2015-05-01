import csv
import math

inf = csv.reader(open('2014dataFormatted.csv',"rU"))
# Data file containing Bureau of Labor Statistics

fileWriter = open('2014Entropy.csv','wb')
wr = csv.writer(fileWriter)
label = ["State","TotalEmp","CaculatedTotalEmp","Diff", "NumOfJobsWithNoData", "AverageEmployedPerMissingJob","entropy", "NormalizedEntropy"]
wr.writerow(label)
#creates a CSV writer called wr, which will write to a file called "theDifference.csv." whith a header to store our values

counter = 0
categoriesMissing = 0
currentState = "none"
currentStateOld = ""
stateTotalEmployed = 0
entropy = float(0)
#creates a series of counters.  "counter" is the sum of all of the sub-jobs.  categoriesMissing is for the difference between the 
#given stateTotalEmployed from the BLS, and the value from counter.  These values are rest when we detect that we have moved to the 
#data from a new state.  This check is conducted by setting "currentState" to the value from the state name colum in the BLS data, 
#and setting the previous value to to currentStateOld.  If currentStateOld differes from current state, then we know we have moved 
#to the data from a new state

for row in inf:
	currentStateOld = currentState
	currentState = row[2]

	if currentState == currentStateOld:
		#this will only run if we are working with the data from the same state.  If so, we add to the "counter" value.
		if int( str(row[3])[3:] ) != 0:
			#this will only run if we are not looking at a major categoy job.
			counter = counter + int(row[6])
			if int(row[6])==0:
				categoriesMissing = categoriesMissing + 1
				#add 1 to categoriesMissing if there is no data from this job.
			if int(row[6]) != 0:
				#add to the entropy caculation if data is available.
				if stateTotalEmployed != 0:
					entropy = entropy - ((float(row[6])/stateTotalEmployed) * math.log(float(row[6])/stateTotalEmployed))
	if currentState != currentStateOld:
		#this will only run upon switching to data from a new state.
		if currentStateOld != "none":
			NormalizedEntropy = 0
			AveEmployed = 0
			if categoriesMissing > 0:
				AveEmployed = float(stateTotalEmployed-counter)/float(categoriesMissing)
			if stateTotalEmployed > 0:
				entropy = entropy - (float(categoriesMissing) * (float(AveEmployed)/float(stateTotalEmployed)) * math.log((float(AveEmployed)/float(stateTotalEmployed))))
				NormalizedEntropy = entropy/math.log(stateTotalEmployed)
			data = currentStateOld,stateTotalEmployed,counter, stateTotalEmployed-counter, categoriesMissing, AveEmployed, entropy, NormalizedEntropy
			wr.writerow(data)
			stateTotalEmployed = int(row[6])
			counter = 0
			categoriesMissing = 0
			entropy = float(0)
			#this writes to the CSV, and then resets the values of the counters.