
import pandas as pd

file_path = 'C:/Users/Montre/Desktop/data analyst/pandas 🐼/archive2/practise_proj2.csv'


# Use pandas to read the CSV file
data = pd.read_csv(file_path)

#drop unnecessary column
data = data.drop('Ref.' , axis =1 )

#print(data.describe())

#identify columns with "[]"
columns = []
for column in data.columns:
    dirty = False
    for row in data[column] :
        #print(row)
        if "[" in str(row):
            dirty = True
    columns.append(dirty)


print(columns)



#remove references from peak and all time peak columns
for row in data["Peak"]:
    row =str(row).split("[")[0]



    print(row)
    #row = row
#print(data["Peak"])






'''
new_file_path = 'C:/Users/Montre/Desktop/data analyst/pandas 🐼/archive2/2.csv'
data.to_csv(new_file_path, index=False)
'''
print(data)