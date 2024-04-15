
import pandas as pd

file_path = 'C:/Users/Montre/Desktop/data analyst/pandas 🐼/archive2/practise_proj2.csv'


# Use pandas to read the CSV file
data = pd.read_csv(file_path)

#drop unnecessary column
data = data.drop('Ref.' , axis =1 )

#print(data.describe())

#identify columns with "[]"
columns_to_clean = []
for column in data.columns:
    #print(column)
    dirty = False
    for row in data[column] :
        #print(row)
        if "[" in str(row):
            dirty = True
    if (dirty == True):
        columns_to_clean.append(column)



print(columns_to_clean)



#remove references from peak and all time peak columns
for column  in columns_to_clean:
    for i, row in enumerate(data[column]) :
        cleaned_row =str(row).split("[")[0]
        #print(row,column)
        data.at[i, column] = cleaned_row
        print(data.at[i, column])
        #print(data.loc[row, column])



    #row = row
#print(data["Peak"])





print(data.dtypes)

new_file_path = 'C:/Users/Montre/Desktop/data analyst/pandas 🐼/archive2/3.csv'
data.to_csv(new_file_path, index=False)

#print(data)