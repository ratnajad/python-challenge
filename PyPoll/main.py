import os
import csv
file = "Resources/election_data.csv"
with open(file) as csvfile:
        data = csv.DictReader(csvfile)
        countvotes = 0
        previous_candidate = 0
        candidatelist = []
        votes_per_candidate = {}
        firsttime = 0
        for row in data:
            countvotes = countvotes + 1
            #Complete list of Candidates 
            if not row['Candidate'] in candidatelist:
                    candidatelist.append(row['Candidate'])
                    votes_per_candidate[row['Candidate']] = 1
            else:
                votes_per_candidate[row['Candidate']] += 1
        
        #Find percentage of votes per candidate and append into percentvotes list
        percent_votes = []
        for votes in votes_per_candidate.keys():
                percent_votes.append(100 * (votes_per_candidate[votes]) / countvotes)
         
        #find number of votes per candidate and append into votes_per_candidateList list
        votes_per_candidateList = []
        for votes in votes_per_candidate.keys():
                votes_per_candidateList.append(votes_per_candidate[votes])
        max_key = max(votes_per_candidate, key = votes_per_candidate.get)
        
output_string = (
        f'Election Results\n'
        f'--------------------------------\n'
        f'Total Votes: {countvotes}\n'
        f'--------------------------------\n'
        f'{candidatelist[0]}: {percent_votes[0]:.3f}% ({votes_per_candidateList[0]})\n'
        f'{candidatelist[1]}: {percent_votes[1]:.3f}% ({votes_per_candidateList[1]})\n'
        f'{candidatelist[2]}: {percent_votes[2]:.3f}% ({votes_per_candidateList[2]})\n'
        f'{candidatelist[3]}: {percent_votes[3]:.3f}% ({votes_per_candidateList[3]})\n'
        f'--------------------------------\n'
        f'Winner: {max_key}\n'
        f'--------------------------------\n'
)
with open('analysis/output2.txt', "w") as txt_file:
        txt_file.write(output_string)

print(output_string)