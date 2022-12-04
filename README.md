# Election Analysis

## Project Overview
Colorado Board of Elections, in addition to analyses on candidates' votes, would like to further gain information on the participating counties' vote status. More specifically:

1. Vote turnout for each participating county.
2. Calculate the percentage of votes per county against total number of votes. 
3. Determine which county had highest number of votes.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.7, Visual Studio Code 1.73.1

## Election Audit Results
The results of the election shows the following: 

- Total number of votes in the congressional election: 
    - 369,711 <br>
    
        ![Total Number of Votes for the Election](Analysis/Total_Votes.jpg)

- The participating counties were: 

    - Jefferson with 38,855 number of votes, or 10.5% of the total votes.
    - Denver with 306,055 number of votes, or 82.8% of the total votes.
    - Arapahoe with 24,801 number of votes, or 6.7% of the total votes. <br>

        ![Vote analysis on Participating Counties](Analysis/County_Votes.jpg)

- The county with largest number of votes:

    - Denver, with 306,055 number of votes, or 82.8% of the total votes. <br>

        ![County with Largest number of votes](Analysis/County_Turnout.jpg)

- The voting results on cadidates were:

    - Charles Casper Stockham received 85,213 number of votes, or 23.0% of total votes
    - Diana DeGette received 272,892 number of votes, or 73.8% of total votes
    - Raymon Anthony Doane received 11,606 number of votes, or 3.1% of total votes<br>

        ![Vote Results for Each Candidate](Analysis/Candidate_Votes.jpg)

- The winner of the election by popular vote was:  

    - Diana DeGette, with 272,892 number of votes, or 73.8% of total votes.<br>

      ![Winning Candiate](Analysis/Winner_Votes.jpg)

## Election-Audit Summary

The script used on this congressional election can be used to analyze any election with some modifications. 