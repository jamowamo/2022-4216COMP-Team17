import csv
import matplotlib.pyplot as plt
import numpy as np

#Lists being declared to hold data
Offence = []
league = []

Offence_Type = []
Number_Of_Offences = []

with open('Offence_Type_Table2010.csv', 'r') as f:
    csv_reader = csv.reader(f) #Csv reader being setup
    header_row = next(csv_reader)
    print(header_row)

    for row in f:
        row = row.split(',') #Comma indicates the the end of that row and that a new one is afer that
        Offence.append(row[1]) #Reads and writes to the list the text on a line until it hits a comma
        league.append(row[2])
  
        if row[0] == 'Offence':
            Offence_Type.append(row[1])
            Number_Of_Offences.append(int(row[2]))
        
fig, ax = plt.subplots() #Creates the figure 
fig.suptitle("By Killian Keogh", fontsize=12) #Sets the suptitle
ax.set_title("Offences By Type 2010/2011", fontsize=14) #Sets the title
ax.set_xlabel("Offence Name", fontsize=5) #sets the x label to year
ax.set_ylabel("Number of Offences by Type 2010/2011", fontsize=12)
ax.bar(Offence_Type,Number_Of_Offences)
plt.xticks(rotation = 270)

ax.set_yticks(range(0,1100,75))
# ax.set_xlim(10, 90) #Sets the lower and upper limit of x axis
ax.set_ylim(0,1300) #y axis limit


plt.show()