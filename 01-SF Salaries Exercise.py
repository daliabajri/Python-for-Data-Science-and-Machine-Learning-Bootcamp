#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[54]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[55]:


# Read the CSV file into a df

sal = pd.read_csv('Salaries.csv')


# ** Check the head of the DataFrame. **

# In[56]:


sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[57]:


sal.info()


# **What is the average BasePay ?**

# In[84]:


# Caluclate the average BasePay

sal['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[85]:


# Caluclate the highest amount of OvertimePay
sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[60]:


# Filter the datadrame to get the job title of JOSEPH DRISCOLL 

job_title = sal.loc[sal['EmployeeName'] == 'JOSEPH DRISCOLL', 'JobTitle'].values[0]

# Convert the job title 

job_title = job_title.upper()




print("Job Title of JOSEPH DRISCOLL: ",job_title)


# In[88]:


# Filter the datadrame to get the job title of JOSEPH DRISCOLL 
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[61]:


# Filter the df to get the row for JOSEPH DRISCOLL
jd_row = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']

#Get the vlaue of 'TotalPayBenefits' for JOSEPH DRISCOLL
jd_pay = jd_row['TotalPayBenefits'].values[0]

#Get the data type of 'TotalPayBenefits'

pay_data_type = jd_row['TotalPayBenefits'].dtype

print(jd_pay)
print(pay_data_type)


# In[90]:


# Filter the df to get the row for JOSEPH DRISCOLL
sal[sal['EmployeeName'] =='JOSEPH DRISCOLL']['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**

# In[62]:


# Sort the df by the 'TotalPayBenefits ' column in decending order

sal_sorted = sal.sort_values('TotalPayBenefits', ascending=False)

# Get the name of the highest paid person 

highest_paid_person = sal_sorted.iloc[0]['EmployeeName']

print(highest_paid_person)


# In[93]:


sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]


# In[94]:


sal.loc[sal['TotalPayBenefits'].idxmax()]


# In[96]:


sal.iloc[sal['TotalPayBenefits'].argmax()]


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[66]:


# Sort the dataframe by the 'TotalPayBenefits' column in ascending order
sal_sorted = sal.sort_values('TotalPayBenefits')

# Get the row for the lowest paid person
lowest_paid_person_row = sal_sorted.iloc[0]

# Get the name of the lowest paid person
lowest_paid_person = lowest_paid_person_row['EmployeeName']

# Create a dataframe with lowest paid person
lowest_paid_person_df = pd.DataFrame(lowest_paid_person_row)

print(lowest_paid_person_df)


# In[97]:


sal.iloc[sal['TotalPayBenefits'].argmin()]


# In[98]:


sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[69]:


# Convert the 'Year' column to datetime type 
sal['Year'] = pd.to_datetime(sal['Year'], format='%Y')

# Filter the dataframe for the years 2011 to 2014 
sal_filtered = sal[sal['Year'].dt.year.between(2011, 2014)]

# Caluclate the average BasePay per year
average_base_pay_per_year = sal_filtered.groupby(sal_filtered['Year'].dt.year)['BasePay'].mean()

print('Average BasePay per year (2011-2014):')
print(average_base_pay_per_year)


# In[100]:


sal.groupby('Year').mean()['BasePay']


# ** How many unique job titles are there? **

# In[70]:


# Get the number of unique job titles
unique_job_titles = sal['JobTitle'].nunique()

print(unique_job_titles)


# In[101]:


sal['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[71]:


# Count the occurrences of each job title
job_title_counts = sal['JobTitle'].value_counts()

# Get the top 5 most common jobs
top_5_jobs = job_title_counts.head(5)

print('Top 5 most common jobs:')
print(top_5_jobs)


# In[103]:


sal['JobTitle'].value_counts().head(5)


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[77]:


# Filtered the df for the year 2013
sal_2013 = sal[sal['Year'] ==2013]

# Count the occurrences of each job title in 2013
job_title_counts_2013 = sal_2013['JobTitle'].value_counts()

# Count the number of job titles with only one occurrence in 2013
job_title_with_one_occurrence_2013 = job_title_counts_2013[job_title_counts_2013 ==1].count()
    
print(job_title_with_one_occurrence_2013)


# In[117]:


sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)


# In[114]:


sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1) # pretty tricky way to do this...


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[80]:


# Filter the df for job titles containing the word 'Chief'
chief_titles = sal[sal['JobTitle'].str.contains('Chief, case=False')]

# Get the number of people with 'Chief' in thier job title
num_people_with_chief_title = len(chief_titles)

print(num_people_with_chief_title)


# In[138]:


def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False


# In[139]:


print(chief_string('Chief manager-metro'))


# In[140]:


sum(sal['JobTitle'].apply(lambda x: chief_string(x)))


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[82]:


# Add a new column for the lenght of the job title string
sal['TitleLength'] = sal['JobTitle'].str.len()

# Calculate the correlation coefficient between thtile length and salary
correlation = sal['TitleLength'].corr(sal['TotalPayBenefits'])

print(correlation)


# In[144]:


# Creating 'title_len ' column out for the lenght of JobTitle
sal['title_len'] = sal['JobTitle'].apply(len)


# In[147]:


sal[['TotalPayBenefits', 'title_len']].corr()


# In[148]:


# There is no correlation 


# # Great Job!
