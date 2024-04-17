'''Python 

import pandas as pd

file_path = 'C:/Users/Montre/Desktop/data analyst/pandas 🐼/archive3/audible_uncleaned.csv'


# Use pandas to read the CSV file
data = pd.read_csv(file_path)


# Trim whitespace from all values in the DataFrame
data = data.map(lambda x: x.strip() if isinstance(x, str) else x)

data['author']= data['author'].str.replace("Writtenby:" , "")
data['narrator'] = data['narrator'].str.replace("Narratedby:","")

# Split the duration string into hours and minutes components
# Split the 'time' column into parts based on the 'and' separator
rows = data['time'].str.split('and')

# Iterate over each row
for i, parts in enumerate(rows):
    # Print the parts of each row
    print("Parts of row", i, ":", parts)

    # Initialize hours and minutes
    hours = 0
    minutes = 0

    # Iterate over each part within the row
    for part in parts:
        # Print each part
        print("Current part:", part)

        # Check if 'hrs' or 'hr' is present in the part
        if 'hrs' in str(part) or 'hr' in str(part):
            # Split the part to extract hours
            hours = part.split()[0]
            print("Hours:", hours)
        # Check if 'mins' or 'min' is present in the part
        elif 'mins' in str(part) or 'min' in str(part) and len(part) < 10:
            # Split the part to extract minutes
            minutes = part.split()[0]
            print("Minutes:", minutes)
        else :
            minutes = 1

    # Calculate total minutes for the row
    total_minutes = int(hours) * 60 + int(minutes)
    print("Total minutes:", total_minutes)

    # Update the 'time' column in the DataFrame with total minutes
    data.loc[i, "time"] = total_minutes
data.rename(columns={'time ': 'time in minutes'})



split_data = data['stars'].str.split('(?<=stars)', expand=True)

def extract_and_replace(value):
    if value == 'Not rated yet':
        return value
    else:
        # Extracting first number
        rating = value.split()[0]
        return float(rating)

def extract_ratings(value):
    if value is not None and value != 'Nan' :
        # Extracting number of ratings
        ratings = value.split()[0]
        return ratings
    else:
        return "0"


# Applying the function to each column
split_data.columns = ['stars', 'ratings']
#print(split_data['ratings'])
data['stars'] = data['stars'].apply(extract_and_replace)
data['ratings'] = split_data['ratings'].apply(extract_ratings)
data['ratings'] = data['ratings'].str.replace(',', '').astype(int)


#print(data['stars'])
#print(data['ratings'])
#print(split_data)



data['price'] = data['price'].str.replace("Free","0").str.replace(',', '').str.replace('.00', '').astype(float)

print(data['price'])
#print(data.loc[8,'price'])

data['language'] = data['language'].str.title()

data.to_csv('C:/Users/Montre/Desktop/data analyst/pandas 🐼/archive3/cleaned_data.csv', index=False)




'''
