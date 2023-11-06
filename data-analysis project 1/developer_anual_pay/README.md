## In this Project I was asked to confirm whether on-site workers are getting paid more than remote ones
### The dataset comes from Stack Overflow and is labeled as "stack-overflow-developer-survey-2023"
### This dataset represents developers from across the globe , their working experience , working style , learning progress  ,salary e.t.c

![raw csv for data analysis](raw_table.png)

### First we need to identify which  data are useful for our analysis scenario and which are not





### We choose the columns:   "Main branch" (Developer as professional job)

### "Age" for better understanding 

### "Employment"( Full time , part time)

### "Remote Work" (On-Site , Hybrid , Remote)

### "EdLevel (Degree , Bachelor's ,Master e.t.c)

### "YearsCodePRo" (represents years of coding experience in a firm )

### "Currency(US Dollars , Euros e.t.c.)

### "Converted Comp Yearly" (annual salary in USD)


![csv after column feature](dataset_after_column_feature.png)

## Now we need to compare the average salaries of Remote workers  with that of Hybrid workers and On-Site workers.

![remote work total pay comparison](remote_work-total_pay.png)



## Our first hypothesis suggests the initial hypothesis is False and remote workers actually get paid more .
### We need to filter data so we are sure we havent made any mistakes and we are not biased. 

### We identify that salaries between countries differ a lot and and so are the numbers of people for each country  so

### we decide to filter data for US citizens only

### We also need to filter any  Null values that may exist in the sheet. 

### Although "Employement" (full-time , part-time , contract) highly affects  payment we identify that in all three cases (Remote ,Hybrid , On-Site) data are equally distributed .

### As it seems though  On-Site workers still remain at the bottom of the chart .

<div style="display: flex;">
  <img src="an_rev_us_prog_chart.png" style="width: 49% height: auto;;" />
</div>


## Continuing the analysis we identify an unsual insight 
### As it seems the older someone is , the more coding experience he has , which is natural . 

![rage_vs_years_of_coding_scatterplot](age_vs_years_of_coding_scatterplot.png)

### On the other hand more coding experience does not translate to bigger salaries

![Programmers Annual Salary vs Years of Excperience](programmers_annual_salary.png)
