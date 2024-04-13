In this project we have a dataset scraped from  https://en.wikipedia.org/wiki/List_of_highest-grossing_concert_tours_by_women 
which reflects most sucessful concerts by women artists

First we read the csv file 

import pandas as pd

file_path = 'C:/Users/Montre/Desktop/data analyst/pandas 🐼/archive2/practise_proj2.csv'


# Use pandas to read the CSV file
data = pd.read_csv(file_path)
