# Election_Analysis

## Proyect Overview
A Colorado Board of Elections employee: Tom, assigned the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes for each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.7, Visual Studio Code 1.60.2

## Election-Audit Results
The analysis of the election shows that:

![Total votes](https://user-images.githubusercontent.com/90433064/136664725-38b9c138-dd62-4c20-93c0-18853ac4b2f1.png)

- There were 369,711 votes cast in the election.

- These are the number of votes and percentage of the total for each county.

![County Votes](https://user-images.githubusercontent.com/90433064/136729237-d11d468f-16cd-4607-96b0-3d7c8d0220a5.png)

- The largest number of votes, was represented in the county of Denver, with a total of 306,055 votes.

![Largest num of votes](https://user-images.githubusercontent.com/90433064/136729378-76229ebd-f143-4114-b6f6-60487af17579.png)

- The candidates were:

![Candidate options](https://user-images.githubusercontent.com/90433064/136664787-af4751ab-846a-481d-80dd-f8fa847a7425.png)

  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

- The candidate results were:

![Candidate results](https://user-images.githubusercontent.com/90433064/136664950-58909c7f-748a-4d7c-9f37-27e2b6ff3e9e.png)

  - Charles Casper Stockham received 23.0% of the vote, with 85,213 votes.
  - Diana DeGette received 73.8% of the vote, with 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote, with 11,606 votes.

- The winner of the election was:

![Winning candidate 1](https://user-images.githubusercontent.com/90433064/136665044-366a1208-2303-44d8-835c-1832244957d6.png)

![Winning candidate 2](https://user-images.githubusercontent.com/90433064/136665051-8e995635-f1ec-4ed8-9e98-1ee2467cb3c2.png)

   - Diana DeGette, who received 73.8% of the vote with 272,892 votes.

## Challenge Overview

![Outcome election_analysis_complete](https://user-images.githubusercontent.com/90433064/136729908-e73a3e93-6bf4-4853-80d6-bd786d1c580d.png)

## Election-Audit Summary
This election-audit has been a very helpful and practical tool for the people in charge of the administration of the election results, since we worked with a data of almost 400,000 elements that in other cases could have taken much more time to concentrate  and to be able to analyze it.

The results gave us very important information for all involved in the elections, since they show which counties we should pay attention for future elections, and / or what strategies have worked for the candidate and the party, to replicate the model in some other counties.

Actually this script can be used from every moment of the election: from when the voter cast his vote, to the moment of every County / State has its own results; meaning that this code can be used in every type of election, from a county to a country. We only have to modify the code, and create a loop that runs into every range that we would like to analyze to get the result about.

We could also go deeper, and to get the result of absentism, by getting the total of people who can cast a vote, and deducted by the final total votes. This kind of information is very important as well for the candidates, and for the political parties, because this indicator could be a target for future campaigns, in order to generate enough interest in the people to go out and cast their vote on their favor.
