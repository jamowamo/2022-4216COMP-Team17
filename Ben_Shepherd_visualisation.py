import csv
import matplotlib.pyplot as plt

date = []
league = []

epl_teams_2015 = []
epl_banning_orders_2015 = []
champ_teams_2015 = []
champ_banning_orders_2015 = []
efl_one_teams_2015 = []
efl_one_banning_orders_2015 = []
efl_two_teams_2015 = []
efl_two_banning_orders_2015 = []
national_league_teams_2015 = []
national_league_banning_orders_2015 = []
other_clubs_2015 = []
other_clubs_banning_orders_2015 = []

epl_teams_2016 = []
epl_banning_orders_2016 = []
champ_teams_2016 = []
champ_banning_orders_2016 = []
efl_one_teams_2016 = []
efl_one_banning_orders_2016 = []
efl_two_teams_2016 = []
efl_two_banning_orders_2016 = []
national_league_teams_2016 = []
national_league_banning_orders_2016 = []
other_clubs_2016 = []
other_clubs_banning_orders_2016 = []

epl_teams_2017 = []
epl_banning_orders_2017 = []
champ_teams_2017 = []
champ_banning_orders_2017 = []
efl_one_teams_2017 = []
efl_one_banning_orders_2017 = []
efl_two_teams_2017 = []
efl_two_banning_orders_2017 = []
national_league_teams_2017 = []
national_league_banning_orders_2017 = []
other_clubs_2017 = []
other_clubs_banning_orders_2017 = []

epl_teams_2018 = []
epl_banning_orders_2018 = []
champ_teams_2018 = []
champ_banning_orders_2018 = []
efl_one_teams_2018 = []
efl_one_banning_orders_2018 = []
efl_two_teams_2018 = []
efl_two_banning_orders_2018 = []
national_league_teams_2018 = []
national_league_banning_orders_2018 = []
other_clubs_2018 = []
other_clubs_banning_orders_2018 = []

with open('banning_orders_table.csv', 'r') as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)

    for row in f:
        row = row.split(',') #Comma indicates the next row on a line
        date.append(row[0]) #Reads and writes to the list the text on a line until it hits a comma
        league.append(row[1])
        if row[1] == 'Premier League' and row[0] == '08-Sept-15':
            epl_teams_2015.append(row[2])
            epl_banning_orders_2015.append(int(row[3]))
        if row[1] == 'Championship' and row[0] == '08-Sept-15':
            champ_teams_2015.append(row[2])
            champ_banning_orders_2015.append(int(row[3]))
        if row[1] == 'League One' and row[0] == '08-Sept-15':
            efl_one_teams_2015.append(row[2])
            efl_one_banning_orders_2015.append(int(row[3]))
        if row[1] == 'League Two' and row[0] == '08-Sept-15':
            efl_two_teams_2015.append(row[2])
            efl_two_banning_orders_2015.append(int(row[3]))
        if row[1] == 'National League' and row[0] == '08-Sept-15':
            national_league_teams_2015.append(row[2])
            national_league_banning_orders_2015.append(int(row[3]))
        if row[1] == 'Other clubs' and row[0] == '08-Sept-15':
            other_clubs_2015.append(row[2])
            other_clubs_banning_orders_2015.append(int(row[3]))

        if row[1] == 'Premier League' and row[0] == '01-Aug-16':
            epl_teams_2016.append(row[2])
            epl_banning_orders_2016.append(int(row[3]))
        if row[1] == 'Championship' and row[0] == '01-Aug-16':
            champ_teams_2016.append(row[2])
            champ_banning_orders_2016.append(int(row[3]))
        if row[1] == 'League One' and row[0] == '01-Aug-16':
            efl_one_teams_2016.append(row[2])
            efl_one_banning_orders_2016.append(int(row[3]))
        if row[1] == 'League Two' and row[0] == '01-Aug-16':
            efl_two_teams_2016.append(row[2])
            efl_two_banning_orders_2016.append(int(row[3]))
        if row[1] == 'National League' and row[0] == '01-Aug-16':
            national_league_teams_2016.append(row[2])
            national_league_banning_orders_2016.append(int(row[3]))
        if row[1] == 'Other clubs' and row[0] == '01-Aug-16':
            other_clubs_2016.append(row[2])
            other_clubs_banning_orders_2016.append(int(row[3]))

        if row[1] == 'Premier League' and row[0] == '07-Aug-17':
            epl_teams_2017.append(row[2])
            epl_banning_orders_2017.append(int(row[3]))
        if row[1] == 'Championship' and row[0] == '07-Aug-17':
            champ_teams_2017.append(row[2])
            champ_banning_orders_2017.append(int(row[3]))
        if row[1] == 'League One' and row[0] == '07-Aug-17':
            efl_one_teams_2017.append(row[2])
            efl_one_banning_orders_2017.append(int(row[3]))
        if row[1] == 'League Two' and row[0] == '07-Aug-17':
            efl_two_teams_2017.append(row[2])
            efl_two_banning_orders_2017.append(int(row[3]))
        if row[1] == 'National League' and row[0] == '07-Aug-17':
            national_league_teams_2017.append(row[2])
            national_league_banning_orders_2017.append(int(row[3]))
        if row[1] == 'Other clubs' and row[0] == '07-Aug-17':
            other_clubs_2017.append(row[2])
            other_clubs_banning_orders_2017.append(int(row[3]))

        if row[1] == 'Premier League' and row[0] == '01-Aug-18':
            epl_teams_2018.append(row[2])
            epl_banning_orders_2018.append(int(row[3]))
        if row[1] == 'Championship' and row[0] == '01-Aug-18':
            champ_teams_2018.append(row[2])
            champ_banning_orders_2018.append(int(row[3]))
        if row[1] == 'League One' and row[0] == '01-Aug-18':
            efl_one_teams_2018.append(row[2])
            efl_one_banning_orders_2018.append(int(row[3]))
        if row[1] == 'League Two' and row[0] == '01-Aug-18':
            efl_two_teams_2018.append(row[2])
            efl_two_banning_orders_2018.append(int(row[3]))
        if row[1] == 'National League' and row[0] == '01-Aug-18':
            national_league_teams_2018.append(row[2])
            national_league_banning_orders_2018.append(int(row[3]))
        if row[1] == 'Other clubs' and row[0] == '01-Aug-18':
            other_clubs_2018.append(row[2])
            other_clubs_banning_orders_2018.append(int(row[3]))



    fig, ax = plt.subplots() #Creates the figure 
#fig.suptitle("Premier League", fontsize=18) #Sets the suptitle
# ax.set_title("Banning orders in 2015", fontsize=14) #Sets the title
    ax.set_xlabel("Team name", fontsize=8) #sets the x label to year
    ax.set_ylabel("Number of banning orders", fontsize=12)
# ax.plot(epl_teams, epl_banning_orders, 'mD:', label='squares') #plots year values along the x axis and total_fans across the y axis. adds squares as the legend for the plotted line
# ax.bar(champ_teams,champ_banning_orders)
    plt.xticks(rotation = 270)

    ax.set_yticks(range(0,150,5))
# ax.set_xlim(0,150) #Sets the lower and upper limit of x axis
    ax.set_ylim(0,150) #y axis limit

# ax.xaxis.grid() can be used if only an x axis grid is desired
    ax.yaxis.grid()

# ax.grid(True) #Creates an x and y axis grid
# ax.legend() #Displays the legend

while True:
    done = True
    league_input = input("\nWhich league banning orders graph would you like to view?\nPremier League\nChampionship\nLeague One\nLeague Two\nNational League\nOther clubs\nTo exit, please enter 'q'\n")
    year_input = input("\nWhich year would you like to view\n2015\n2016\n2017\n2018\n")
    if league_input == 'Premier League' and year_input == '2015':
        fig.suptitle("Premier League", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2015", fontsize=14) #Sets the title
        ax.bar(epl_teams_2015,epl_banning_orders_2015)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'Championship' and year_input == '2015':
        fig.suptitle("Championship", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2015", fontsize=14) #Sets the title
        ax.bar(champ_teams_2015,champ_banning_orders_2015)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'League One' and year_input == '2015':
        fig.suptitle("League One", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2015", fontsize=14) #Sets the title
        ax.bar(efl_one_teams_2015,efl_one_banning_orders_2015)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'League Two' and year_input == '2015':
        fig.suptitle("League Two", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2015", fontsize=14) #Sets the title
        ax.bar(efl_two_teams_2015,efl_two_banning_orders_2015)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'National League' and year_input == '2015':
        fig.suptitle("National League", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2015", fontsize=14) #Sets the title
        ax.bar(national_league_teams_2015,national_league_banning_orders_2015)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'Other clubs' and year_input == '2015':
        fig.suptitle("Other clubs", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2015", fontsize=14) #Sets the title
        ax.bar(other_clubs_2015,other_clubs_banning_orders_2015)
        plt.xticks(rotation = 270)
        plt.show()
        done = False

    if league_input == 'Premier League' and year_input == '2016':
        fig.suptitle("Premier League", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2016", fontsize=14) #Sets the title
        ax.bar(epl_teams_2016,epl_banning_orders_2016)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'Championship' and year_input == '2016':
        fig.suptitle("Championship", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2016", fontsize=14) #Sets the title
        ax.bar(champ_teams_2016,champ_banning_orders_2016)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'League One' and year_input == '2016':
        fig.suptitle("League One", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2016", fontsize=14) #Sets the title
        ax.bar(efl_one_teams_2016,efl_one_banning_orders_2016)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'League Two' and year_input == '2016':
        fig.suptitle("League Two", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2016", fontsize=14) #Sets the title
        ax.bar(efl_two_teams_2016,efl_two_banning_orders_2016)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'National League' and year_input == '2016':
        fig.suptitle("National League", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2016", fontsize=14) #Sets the title
        ax.bar(national_league_teams_2016,national_league_banning_orders_2016)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'Other clubs' and year_input == '2016':
        fig.suptitle("Other clubs", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2016", fontsize=14) #Sets the title
        ax.bar(other_clubs_2015,other_clubs_banning_orders_2016)
        plt.xticks(rotation = 270)
        plt.show()
        done = False

    if league_input == 'Premier League' and year_input == '2017':
        fig.suptitle("Premier League", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2017", fontsize=14) #Sets the title
        ax.bar(epl_teams_2017,epl_banning_orders_2017)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'Championship' and year_input == '2017':
        fig.suptitle("Championship", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2017", fontsize=14) #Sets the title
        ax.bar(champ_teams_2017,champ_banning_orders_2017)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'League One' and year_input == '2017':
        fig.suptitle("League One", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2017", fontsize=14) #Sets the title
        ax.bar(efl_one_teams_2017,efl_one_banning_orders_2017)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'League Two' and year_input == '2017':
        fig.suptitle("League Two", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2017", fontsize=14) #Sets the title
        ax.bar(efl_two_teams_2017,efl_two_banning_orders_2017)
        done = False
    if league_input == 'National League' and year_input == '2017':
        fig.suptitle("National League", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2017", fontsize=14) #Sets the title
        ax.bar(national_league_teams_2017,national_league_banning_orders_2017)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'Other clubs' and year_input == '2017':
        fig.suptitle("Other clubs", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2017", fontsize=14) #Sets the title
        ax.bar(other_clubs_2017,other_clubs_banning_orders_2017)
        plt.xticks(rotation = 270)
        plt.show()
        done = False

    if league_input == 'Premier League' and year_input == '2018':
        fig.suptitle("Premier League", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2018", fontsize=14) #Sets the title
        ax.bar(epl_teams_2018,epl_banning_orders_2018)
        plt.show()
        done = False
    if league_input == 'Championship' and year_input == '2018':
        fig.suptitle("Championship", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2018", fontsize=14) #Sets the title
        ax.bar(champ_teams_2018,champ_banning_orders_2018)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'League One' and year_input == '2018':
        fig.suptitle("League One", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2018", fontsize=14) #Sets the title
        ax.bar(efl_one_teams_2018,efl_one_banning_orders_2018)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'League Two' and year_input == '2018':
        fig.suptitle("League Two", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2018", fontsize=14) #Sets the title
        ax.bar(efl_two_teams_2018,efl_two_banning_orders_2018)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'National League' and year_input == '2018':
        fig.suptitle("National League", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2018", fontsize=14) #Sets the title
        ax.bar(national_league_teams_2018,national_league_banning_orders_2018)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'Other clubs' and year_input == '2018':
        fig.suptitle("Other clubs", fontsize=18) #Sets the suptitle
        ax.set_title("Banning orders in 2018", fontsize=14) #Sets the title
        ax.bar(other_clubs_2018,other_clubs_banning_orders_2018)
        plt.xticks(rotation = 270)
        plt.show()
        done = False
    if league_input == 'q' or year_input == 'q':
        quit()