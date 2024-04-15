import pandas as pd

file_path = 'C:/Users/Montre/Desktop/data analyst/pandas 🐼/archive2/3.csv'


# Use pandas to read the CSV file
data = pd.read_csv(file_path)





for column in data.columns:
    if ("gross" in column):
        #print(column)
        for i,row in enumerate(data[column]) :
            data.at[i,column] = row.replace("$", "")
            data.at[i, column] = data.at[i,column].replace(",", "")

            #print(data.at[i,column])




#Check if all types are of correct
#print(data.dtypes)



#rename columns
data.rename(columns={'Actual gross in local currency': 'Actual gross in local currency'}, inplace=True)
data.rename(columns={'Adjusted gross in dollars': 'Adjusted gross in dollars'} , inplace=True)

#convert columns types
data['Actual gross in local currency'] = pd.to_numeric(data['Actual gross in local currency'], errors='coerce')
data['Adjusted gross in dollars'] = pd.to_numeric(data['Adjusted gross in dollars'], errors='coerce')
data['Average gross'] = pd.to_numeric(data['Average gross'], errors='coerce')
data['Shows'] = pd.to_numeric(data['Shows'], errors='coerce')


print(data.dtypes)

#iterate on columns
actual_gross = True
adjusted_gross = False
print(data.columns)
for i in range(data.shape[0]):
    print(f"for row : {i}  num of shows is {data.loc[i,'Shows']} , num of average gross is {data.loc[i,'Average gross']} ,actual gross {data.loc[i,'Actual gross in local currency']} , adjusted gross  {data.loc[i,'Adjusted gross in dollars']}")
actual_gross = round(data['Shows'] == (data['Actual gross in local currency']//100) // (data['Average gross']//100))
adjusted_gross = round(data['Shows'] == (data['Adjusted gross in dollars']//100) //  (data['Average gross']//100))

print(actual_gross,adjusted_gross)

data['number of average gross in dollars'] = round(data['Adjusted gross in dollars'] //  data['Shows'])
print(data['number of average gross in dollars'])


new_file_path = 'C:/Users/Montre/Desktop/data analyst/pandas 🐼/archive2/4.csv'
data.to_csv(new_file_path, index=False)


