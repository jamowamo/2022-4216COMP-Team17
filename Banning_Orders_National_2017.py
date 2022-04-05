import csv
import matplotlib.pyplot as plt

date = []
league = []

national_league_teams_2017 = []
national_league_banning_orders_2017 = []

with open('banning_orders_table.csv', 'r') as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)

    for row in f:
        row = row.split(',') #Comma indicates the next row on a line
        date.append(row[0]) #Reads and writes to the list the text on a line until it hits a comma
        league.append(row[1])
  
        if row[1] == 'National League (National Division)' and row[0] == '07-Aug-17':
            national_league_teams_2017.append(row[2])
            national_league_banning_orders_2017.append(int(row[3]))
        
fig, ax = plt.subplots() #Creates the figure 
fig.suptitle("National_League_Teams", fontsize=12) #Sets the suptitle
ax.set_title("Banning orders in 2017", fontsize=14) #Sets the title
ax.set_xlabel("Team name", fontsize=8) #sets the x label to year
ax.set_ylabel("Number of banning orders", fontsize=12)
ax.plot(national_league_teams_2017, national_league_banning_orders_2017, 'mD:', label='squares') #plots year values along the x axis and total_fans across the y axis. adds squares as the legend for the plotted line

plt.xticks(rotation = 270)

ax.set_yticks(range(10,90,10))
# ax.set_xlim(10, 90) #Sets the lower and upper limit of x axis
ax.set_ylim(0,90) #y axis limit

# ax.xaxis.grid() can be used if only an x axis grid is desired
ax.yaxis.grid()

# ax.grid(True) #Creates an x and y axis grid
# ax.legend() #Displays the legend

plt.show()