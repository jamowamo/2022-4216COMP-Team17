import matplotlib.pyplot as plt
import matplotlib.font_manager as mfont
team_name = []
banning_orders = []

f = open('banning_orders_epl.txt', 'r')
for row in f:
    row = row.split(',') #Comma indicates the next row on a line
    team_name.append(row[0]) #Reads in the text on a line before the comma
    banning_orders.append(int(row[1]))#reads the data on a line after the comma

fig, ax = plt.subplots() #Creates the figure 
fig.suptitle("Premier League", fontsize=18) #Sets the suptitle
ax.set_title("Banning orders in 2015", fontsize=14) #Sets the title
ax.set_xlabel("Team name", fontsize=8) #sets the x label to year
ax.set_ylabel("Number of banning orders", fontsize=12) # ^
ax.plot(team_name, banning_orders, 'mD:', label='squares') #plots year values along the x axis and total_fans across the y axis. adds squares as the legend for the plotted line
plt.xticks(rotation = 270)
# ax.set_xlim(1999,2003) #Sets the lower and upper limit of x axis
# ax.set_ylim(0,100) #y axis limit
# ax.xaxis.grid() can be used if only an x axis grid is desired
# ax.yaxis.grid() ^

ax.grid(True) #Creates an x and y axis grid
# ax.legend() #Displays the legend

plt.show() #Outputs the figure


