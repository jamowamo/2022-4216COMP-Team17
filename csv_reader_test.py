import csv
import matplotlib.pyplot as plt
date = []
league = []
team_name = []
banning_orders = []

epl_teams = []
epl_banning_orders = []

champ_teams = []
champ_banning_orders = []

with open('banning_orders.csv', 'r') as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)

    for row in f:
        row = row.split(',') #Comma indicates the next row on a line
        date.append(row[0]) #Reads in the text on a line before the comma
        league.append(row[1])#reads the data on a line after the comma
        if row[1] == 'Premier League':
            epl_teams.append(row[2])
            epl_banning_orders.append(int(row[3]))
        if row[2] == 'Championship':
            champ_teams.append(row[2])
            champ_banning_orders.append(int(row[3]))

fig, ax = plt.subplots() #Creates the figure 
fig.suptitle("Premier League", fontsize=18) #Sets the suptitle
ax.set_title("Banning orders in 2015", fontsize=14) #Sets the title
ax.set_xlabel("Team name", fontsize=8) #sets the x label to year
ax.set_ylabel("Number of banning orders", fontsize=12) # ^
ax.plot(epl_teams, epl_banning_orders, 'mD:', label='squares') #plots year values along the x axis and total_fans across the y axis. adds squares as the legend for the plotted line
plt.xticks(rotation = 270)

ax.set_yticks(range(0,150,10))
# ax.set_xlim(0,150) #Sets the lower and upper limit of x axis
ax.set_ylim(0,150) #y axis limit

# ax.xaxis.grid() can be used if only an x axis grid is desired
# ax.yaxis.grid() ^

ax.grid(True) #Creates an x and y axis grid
# ax.legend() #Displays the legend

# while True:
    #io = input("\nEnter 'Yes' if you would you like to view the graph. If no, please enter 'q'")
    #if io == 'q':
     #   break
    #if io == 'Yes':

plt.show()
