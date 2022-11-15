import os
import csv

#file path to load
csvpath = os.path.join("PyPoll/Resources/election_data.csv")

#file path to export
txtwrite = os.path.join("PyPoll/analysis/election_results.txt")

line = "-------------------------"

#Declare variables
candidate_list = []
total_votes = 0 
election_dict = {}
winning_candidate = ""
winning_count = 0

#Read file and open election data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    #Begin for loop to iterate through data
    for row in csvreader:
        
        #counter
        total_votes += 1
        candidate_name = row[2]

        #Add candidates to list if not present in candidate list
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            election_dict[candidate_name] = 0
        election_dict[candidate_name] += 1

with open(txtwrite, "w") as txt_file:

    #Print to terminal total votes
    election_results = (
    f"Election Results \n"
    f"{line}\n"
    f"Total votes: {total_votes:}\n"
    f"{line}\n")
    print(election_results, end="")
    
    #save to txt file
    txt_file.write(election_results)

    #iterate through candidate list and find vote count and vote percentage
    for candidate_name in election_dict:
        votes = election_dict[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        candidate_results = (f"{candidate_name}: {vote_percentage:.3f}%  ({votes:})\n")
        print(candidate_results)

        #save to txt file
        txt_file.write(candidate_results)

        #Winning candidate results
        if (votes>winning_count):
            winning_count = votes
            winning_candidate = candidate_name

    #Print to terminal and save in txt file
    winner = (
    f"{line}\n"
    f"Winner: {winning_candidate}\n"
    f"{line}")
    print(winner)
    txt_file.write(winner)