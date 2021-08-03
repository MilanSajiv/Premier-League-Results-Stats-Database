# Premier-League-Results-Stats-Database

## Introduction: 

This python script extracts data from the Premier League Official website, from 2011-12 season to 2020-21 season. The purpose of the data is to feed into a machine learning model in order to predict the results and stats of each game for the upcoming football season.  

## Python Script Details:

MY_PL_PRJ.py, uses the Selenium and pandas libraries. Using Selenium the program opens the premier league website and its corresponding links to scrape the necessary data by finding the it’s xpath to collect the match details and the stats of the match such as Result, possession, shots on target corners and offsides. This data is written to separate  csv files based on the season. 

## Data:

Final_Results: This folder contains the 10 csv files which corresponds to each premier league season. Each file contains approximately 220-230 rows with detailed descriptions of the matches, which include the following details of both home and away team:

- Date
- Teams
- Scores
- Possession
- Shots on target
- Shots
- Touches
- Passes
- Tackles
- Clearance
- Corners
- Offsides
- Yellow Card
- Red Cards
