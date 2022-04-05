import csv
import matplotlib.pyplot as plt

date = []
league = []

epl_teams = []
epl_banning_orders = []

champ_teams = []
champ_banning_orders = []

efl_one_teams = []
efl_one_banning_orders = []

efl_two_teams = []
efl_two_banning_orders = []

national_league_teams = []
national_league_banning_orders = []

other_clubs = []
other_clubs_banning_orders = []

with open('banning_orders_table.csv', 'r') as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)

    for row in f:
        row = row.split(',') #Comma indicates the next row on a line
        date.append(row[0]) #Reads and writes to the list the text on a line until it hits a comma
        league.append(row[1])
        if row[1] == 'Premier League' and row[0] == '08-Sept-15':
            epl_teams.append(row[2])
            epl_banning_orders.append(int(row[3]))
        if row[1] == 'Championship' and row[0] == '08-Sept-15':
            champ_teams.append(row[2])
            champ_banning_orders.append(int(row[3]))
        if row[1] == 'League One' and row[0] == '08-Sept-15':
            efl_one_teams.append(row[2])
            efl_one_banning_orders.append(int(row[3]))
        if row[1] == 'League Two' and row[0] == '08-Sept-15':
            efl_two_teams.append(row[2])
            efl_two_banning_orders.append(int(row[3]))
        if row[1] == 'National League' and row[0] == '08-Sept-15':
            national_league_teams.append(row[2])
            national_league_banning_orders.append(int(row[3]))
        if row[1] == 'Other clubs' and row[0] == '08-Sept-15':
            other_clubs.append(row[2])
            other_clubs_banning_orders.append(int(row[3]))

fig, ax = plt.subplots() #Creates the figure 
fig.suptitle("Premier League", fontsize=18) #Sets the suptitle
ax.set_title("Banning orders in 2015", fontsize=14) #Sets the title
ax.set_xlabel("Team name", fontsize=8) #sets the x label to year
ax.set_ylabel("Number of banning orders", fontsize=12)
# ax.plot(epl_teams, epl_banning_orders, 'mD:', label='squares') #plots year values along the x axis and total_fans across the y axis. adds squares as the legend for the plotted line
ax.bar(champ_teams,champ_banning_orders)
plt.xticks(rotation = 270)

ax.set_yticks(range(0,150,5))
# ax.set_xlim(0,150) #Sets the lower and upper limit of x axis
ax.set_ylim(0,150) #y axis limit

# ax.xaxis.grid() can be used if only an x axis grid is desired
ax.yaxis.grid()

# ax.grid(True) #Creates an x and y axis grid
# ax.legend() #Displays the legend

# while True:
    #io = input("\nEnter 'Yes' if you would you like to view the graph. If no, please enter 'q'")
    #if io == 'q':
     #   break
    #if io == 'Yes':

plt.show()