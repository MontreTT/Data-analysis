import pandas as pd
from scipy import stats
file_path = 'C:/Users/Montre/Desktop/data analyst/pandas 🐼/archive2/4.csv'


# Use pandas to read the CSV file
data = pd.read_csv(file_path)

data.drop(columns= ["Actual gross in local currency","Average gross"], inplace = True)


char = data.loc[0,'Year(s)'][4]

data['Year(s)'] = data['Year(s)'].apply(lambda x: x if char in x else x + char + x)


#print(data['Year(s)'])
char = data.loc[0,'Year(s)'][4]

data[['Start Year', 'End Year']] = data['Year(s)'].str.split(str(char), expand=True)
data['Start Year'] = pd.to_numeric(data['Start Year'], errors='coerce')
data['End Year'] = pd.to_numeric(data['End Year'], errors='coerce')






# Define threshold for outliers (e.g., Z-score > 3 or Z-score < -3)
threshold = 3



z_scores1 = stats.zscore(data['Adjusted gross in dollars'])
z_scores2 = stats.zscore(data['number of average gross in dollars'])
z_scores3 = stats.zscore(data['Shows'])
z_scores4 = stats.zscore(data['Start Year'])
z_scores5 = stats.zscore(data['End Year'])



# Find outliers
outliers1 = data['Adjusted gross in dollars'][abs(z_scores1) > threshold]
outliers2 = data['number of average gross in dollars'][abs(z_scores2) > threshold]
outliers3 = data['Shows'][abs(z_scores3) > threshold]
outliers4 = data['Start Year'][abs(z_scores4) > threshold]
outliers5 = data['End Year'][abs(z_scores5) > threshold]

print(outliers1,outliers2,outliers3,outliers4,outliers5)

data = data[['Rank', 'Peak', 'All Time Peak', 'Artist', 'Start Year', 'End Year', 'Tour title', 'Shows', 'number of average gross in dollars',  'Adjusted gross in dollars']]

data.rename(columns={'Adjusted gross in dollars': 'overall gross in $'}, inplace=True)
data.rename(columns={'number of average gross in dollars': 'average gross in $'}, inplace=True)



new_file_path = 'C:/Users/Montre/Desktop/data analyst/pandas 🐼/archive2/5.csv'
data.to_csv(new_file_path, index=False)