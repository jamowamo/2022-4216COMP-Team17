import csv
import matplotlib.pyplot as plt

date = []
league = []

league_2014 = []
league_2015 = []
league_2016 = []
league_2017 = []

arrests_2014 = []
arrests_2015 = []
arrests_2016 = []
arrests_2017 = []

with open("arrest rate by competition.csv" , "r") as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)

    for row in f:
       row = row.split(',') #Comma indicates the next row on a line
       date.append(row[0]) #Reads and writes to the list the text on a line until it hits a comma
       league.append(row[1])

       if row[0] == "2014-15":
            league_2014.append(row[1])
            arrests_2014.append(row[2])
       if row[0] == "2015-16":
            league_2015.append(row[1])
            arrests_2015.append(row[2])
       if row[0] == "2015-16":
            league_2015.append(row[1])
            arrests_2015.append(row[2])
       if row[0] == "2015-16":
            league_2015.append(row[1])
            arrests_2015.append(row[2])
            
year = input("What year would you like to see visualisations for?")
if year == "2014":
     fig, ax = plt.subplots()
     fig.suptitle("By James S", fontsize=8)
     ax.set_title("Arrests by competition", fontsize=14)
     ax.set_xlabel("League", fontsize=12)
     ax.set_ylabel("Arrests", fontsize=12)
     ax.bar(league_2014, arrests_2014)   

     plt.xticks(rotation = 285)
     ax.set_yticks(range(0,600,10))
     ax.set_ylim(0, 600)
     ax.yaxis.grid()
     plt.show()

if year == "2015":

     fig, ax = plt.subplots()
     fig.suptitle("By James S", fontsize=8)
     ax.set_title("Arrests by competition in 2015", fontsize=14)
     ax.set_xlabel("League", fontsize=12)
     ax.set_ylabel("Arrests", fontsize=12)
     ax.plot(league_2015, arrests_2015,  'mD:', label = 'squares')


     plt.xticks(rotation = 285)
     ax.set_yticks(range(0,600,10))
     ax.set_ylim(0, 600)
     ax.yaxis.grid()

     plt.show()

   