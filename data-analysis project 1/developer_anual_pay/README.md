## In this Project I was asked to confirm whether on-site workers are getting paid more than remote ones
### The dataset comes from Stack Overflow and is labeled as "stack-overflow-developer-survey-2023"
### This dataset represents developers from across the globe , their working experience , working style , learning progress  ,salary e.t.c

![raw csv for data analysis](raw_table.png)

### First we need to identify which  data are useful for our analysis scenario and which are not





### We choose the columns:   "Main branch" (Developer as professional job)

### "Age" for better understanding 

### "Employment"( Full time , part time)

### "Remote Work" (On-Site , Hybrid , Remote)

### "YearsCodePRo" (represents years of coding experience in a firm )

### "Currency(US Dollars , Euros e.t.c.)

### "Converted Comp Yearly" (annual salary in USD)




![csv after column feature](dataset_after_column_feature.png)

## Our first hypothesis suggests the initial hypothesis is False and remote workers actually get paid more .
### We need to filter data so we are sure we havent made any mistakes and we are not biased. 
### We identify that salaries between countries differ a lot and and so are the numbers of people for each country 
### As Entries are more than enough , Filter USA only citizens will solve this problem 
### We also need to filter any  Null values that may exist in the sheet. 
### As "Employement" (full-time , part-time , contract) highly affects  payment we need to make sure that data are equally distributed
