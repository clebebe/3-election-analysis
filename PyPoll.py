import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis","election_analysis.txt")

#initialize vote counter
total_votes = 0

#initialize list of candidates
candidate_options = []

#initialize dictionary to keep vote count for each candidate
candidate_votes = {}

#winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    # to do: read and analyze the data
    file_reader = csv.reader(election_data)

    #read header row // skips the head row for the upcoming for loop
    headers = next(file_reader)
    

    for row in file_reader:
        #loop through each row in csv file and sum vote count
        #(same as counting total # of rows less header row)
        total_votes += 1

        #read candidate name for eacdh row then add to the list of candiates
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
        
            #track each candidate's vote 
            candidate_votes[candidate_name] = 0

        #adds vote count for corresponding candidate for each row
        candidate_votes[candidate_name] +=1

    with open(file_to_save, "w") as txt_file:

        #print election results to the text file
        election_results = (
            f"Election Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
        )

        print(election_results, end="")

        txt_file.write(election_results)

        # loop through each candidate's total votes and calculate vote percentage
        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            
            # determine winning vote count and its candidate
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

            #print each candidate's vote results
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results,end="")
            txt_file.write(candidate_results)

        #printing winning candidate summary
        winning_candidate_summary = (
            f"-----------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n")

        #print winning candidate summary to text file    
        txt_file.write(winning_candidate_summary)

        