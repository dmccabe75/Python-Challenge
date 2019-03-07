import os
import csv
import collections

poll_data = os.path.join("..", "PyPoll", "election_data.csv")

with open(poll_data, newline="") as csvfile:
    electionresults = csv.reader(csvfile, delimiter=",")
    next(electionresults, None)
    
    Total_Votes = 0
    Khan = 0
    Correy = 0
    Li = 0
    OTooley = 0

    for record in electionresults:

        Total_Votes +=1
        if record[2] == "Khan":
            Khan += 1
        elif record[2] == "Correy":
            Correy += 1
        elif record[2] == "Li":
            Li += 1
        elif record[2] == "O'Tooley":
            OTooley +=1 
            pass
        
    Khan_pct = round(Khan/Total_Votes*100)
    Correy_pct = round(Correy/Total_Votes*100)
    Li_pct = round(Li/Total_Votes*100)
    OTooley_pct = round(OTooley/Total_Votes*100)    


    
    print("Election Results")
    print("---------------------")
    print("Total Votes:" + str(Total_Votes))
    print("---------------------")
    print ("Khan: " + str(Khan_pct) +"%  (" + str(Khan) + ")")
    print("Correy: " + str(Correy_pct) +"%  (" + str(Correy) +")") 
    print("Li: " + str(Li_pct) + "%  (" + str(Li) + ")")
    print("O'Tooley: " + str(OTooley_pct) + "% (" + str(OTooley) + ")")
    print("-----------------------")
    print("Winner: Khan")
    print("-----------------------")
 

output_file = os.path.join("pypoll_output.txt")
with open(output_file, 'w') as text_file:
    writer = csv.writer(text_file)
    writer.writerow("Election Results")
    writer.writerow("---------------------")
    writer.writerow("Total Votes:" + str(Total_Votes))
    writer.writerow("---------------------")
    writer.writerow("Khan: " + str(Khan_pct) +"%  (" + str(Khan) + ")")
    writer.writerow("Correy: " + str(Correy_pct) +"%  (" + str(Correy) +")") 
    writer.writerow("Li: " + str(Li_pct) + "%  (" + str(Li) + ")")
    writer.writerow("O'Tooley: " + str(OTooley_pct) + "% (" + str(OTooley) + ")")
    writer.writerow("-----------------------")
    writer.writerow("Winner: Khan")
    writer.writerow("-----------------------")
    
   


