## In this Project I was asked to confirm whether on-site workers are getting paid more than remote ones
### The dataset comes from Stack Overflow and is labeled as "stack-overflow-developer-survey-2023"
### This dataset represents developers from across the globe , their working experience , working style , learning progress  ,salary e.t.c

![Alt text](relative/path/to/image.png)

### First we need to identify which  data are useful for our analysis scenario and which are not





### We choose the columns:   "Main branch" (Developer as professional job)

### "Remote Work" (On-Site , Hybrid , Remote)

### "Converted Comp Yearly" (annual salary in USD)

### "Age" for better understanding 



## Our first hypothesis suggests the initial hypothesis is False and remote workers actually get paid more .
### We need to filter data so we are sure we havent made any mistakes and we are not biased. 
### We identify that salaries between countries differ a lot and and so are the numbers of people for each country 
### As Entries are more than enough , Filter USA only citizens will solve this problem 
### We also need to filter any  Null values that may exist in the sheet. 
### As "Employement" (full-time , part-time , contract) highly affects  payment we need to make sure that data are equally distributed
