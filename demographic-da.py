import pandas as pd
import numpy as np

# Load data
dt = data = pd.read_csv('adult.data.csv')

# How many people of each race are represented in this dataset? 
race_count = data['race'].value_counts()

# What is the average age of men?
average_age_men = round(data.loc[data['sex'] == 'Male', 'age'].mean(), 1)

# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = round(len(data[data['education'] == 'Bachelors']) / len(data) * 100, 1)

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
higher_education = data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education) * 100, 1)

# What percentage of people without advanced education make more than 50K?
lower_education = data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
lower_education_rich = round(len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education) * 100, 1)

# What is the minimum number of hours a person works per week?
min_work_hours = data['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = len(data[data['hours-per-week'] == min_work_hours])
rich_percentage = round(len(data[(data['hours-per-week'] == min_work_hours) & (data['salary'] == '>50K')]) / num_min_workers * 100, 1)

# What country has the highest percentage of people that earn >50K and what is that percentage?
highest_earning_country = (data.loc[data['salary'] == '>50K', 'native-country'].value_counts() / data['native-country'].value_counts()).idxmax()
highest_earning_country_percentage = round((data.loc[data['salary'] == '>50K', 'native-country'].value_counts() / data['native-country'].value_counts()).max() * 100, 1)

# Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = data.loc[(data['native-country'] == 'India') & (data['salary'] == '>50K'), 'occupation'].value_counts().idxmax()

# Print results
print("Number of each race:\n", race_count)
print("Average age of men:", average_age_men)
print("Percentage with Bachelors degrees:", percentage_bachelors)
print("Percentage with higher education that earn >50K:", higher_education_rich)
print("Percentage without higher education that earn >50K:", lower_education_rich)
print("Min work time:", min_work_hours)
print("Percentage of rich among those who work fewest hours:", rich_percentage)
print("Country with highest percentage of rich:", highest_earning_country, highest_earning_country_percentage)
print("Top occupations in India:", top_IN_occupation)
