import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r'C:\Users\BlueworksADM1\OneDrive\Documents\PYTHON\Data-project-1\adult.data.csv')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts

    # What is the average age of men?
    average_age_men = average_age_men=df[df['sex']=='Male']['age'].mean()


    # What is the percentage of people who have a Bachelor's degree?
    bachelor =( df['education']=='Bachelors').sum()
    total = len(df)
    percentage_bachelors =( bachelor/total)*100
  

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advanced_education= df['education'].isin(['Bachelors','Masters' ,'Doctorate'])
    higher_education = df[advanced_education]
    lower_education = df[~advanced_education]

    # percentage with salary >50K for educated
    sum_rich_high=( higher_education['salary']=='>50K').sum()
    total_rich_high = len(higher_education)
    higher_education_rich = (sum_rich_high/total_rich_high)*100

    #percentage with salary >50k for not educated

    sum_rich_low=( lower_education['salary']=='>50K').sum()
    total_rich_low = len(lower_education)
    lower_education_rich = (sum_rich_low/total_rich_low)*100



    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    #dataframe of those who work low hours 
    lowhours= df[df['hours-per-week']== min_work_hours]


    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(lowhours)
    richminworkerssum= (lowhours['salary']=='>50K').sum()

    rich_percentage = (richminworkerssum/num_min_workers)*100

    # What country has the highest percentage of people that earn >50K?
    #First look at all the data for individuals earning more than 50k
    
    high_salary= df[df['salary']=='>50K']
    country_high_salary_counts = high_salary['native-country'].value_counts()
    
    country_counts = df['native-country'].value_counts()
    percentages = ( country_high_salary_counts / country_counts) * 100

    highest_earning_country = percentages.idxmax()

    #
    highest_earning_country_percentage = percentages.max()

    # Identify the most popular occupation for those who earn >50K in India.
    high_india=high_salary[high_salary['native-country']=='India']
    counts= high_india['occupation'].value_counts()

    top_IN_occupation = counts.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation}