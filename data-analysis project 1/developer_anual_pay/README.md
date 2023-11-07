## In this Project I was asked to confirm whether on-site workers in the US are getting paid more than remote workers
## TOOLS : Google Sheets , Tableau
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

## On the other hand more coding experience does not translate to bigger salaries

![Programmers Annual Salary vs Years of Excperience](programmers_annual_salary.png)

## To further explain we partitioned the graph to 3 smaller one with some help of Tableau

<div class='tableauPlaceholder' id='viz1699358467224' style='position: relative'><noscript><a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ZN&#47;ZNNSN8SBH&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;ZNNSN8SBH' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ZN&#47;ZNNSN8SBH&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>   

### After a lot of studying and online searching we come at these conclusions :

### Between 0-12 years of coding experience the salary is increasing with experience . The average salary varies from 95-180k per year
![Salary for coding experience 0-12 years](sal_exp1.png)


### Between 13-28 years of coding experience the salary remains the same . The average salaray varies around 160-180k per year
![Salary for coding experience 12-28 years](sal_exp2.png)

### This is mainly because experience reaches the highest cap firms are willing to pay for a position . Extra experience further than 13 years is considered unimportant

### For 28+ years of coding experience on the other hand . Salaries are on the decline .
![Salary for coding experience 28+ years](sal_exp3.png)

### As we previously discussed coding experience has a positive correlation with age . At these ranges companies are willing to pay less for that particular group of people as aging seems more important than knowledge.

## This means that age affect directly salaries . To ensure a fair comparison between Remote , On-site and hybrid workers we need to transform data so they are not affected by data. 

### We transform the data to be equally distributed 

![Final Transformed Data](Final_Transformed_Salaries.png)

## We can see that in the first place come hybrid workers with an annual average salary of 168k
## At second places come Remote workers at 150k
## And last , On-site workers have the lowert salaries on average (133k)
