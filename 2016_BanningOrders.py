import csv
import matplotlib.pyplot as plt

date = []
league = []

champ_teams_2017 = []
champ_banning_orders_2017 = []

with open('banning_orders_table.csv', 'r') as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)

for row in f:
    row = row.split(',') #Comma indicates the next row on a line
    date.append(row[0]) #Reads and writes to the list the text on a line until it hits a comma
    league.append(row[1])

    if row[1] == 'Championship' and row[0] == '07-Aug-17':
            champ_teams_2017.append(row[2])
            champ_banning_orders_2017.append(int(row[3]))

fig, ax = plt.subplots() #Creates the figure 
fig.suptitle("Championship", fontsize=18) #Sets the suptitle
ax.set_title("Banning orders in 2017", fontsize=14) #Sets the title
ax.set_xlabel("Team name", fontsize=8) #sets the x label to year
ax.set_ylabel("Number of banning orders", fontsize=12)
ax.bar(champ_teams_2017,champ_banning_orders_2017)
plt.xticks(rotation = 270)

ax.set_yticks(range(0,150,5))
# ax.set_xlim(0,150) #Sets the lower and upper limit of x axis
ax.set_ylim(0,150) #y axis limit

ax.yaxis.grid()

plt.show()