#library
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

#Import Dataset & define Dataframe
url = "https://query.data.world/s/lqrsaugj7kwkyazkvydowjuxjrybxx"

df = pd.read_csv(url, sep = ";")

# Show dataframe
df
df.head()
df.describe()

# Rename Columns' Names
# New_Name a dictionary
# key = old name
# value = new name
dict = {'age': 'Age',
        'job': 'Job',
        'martial': 'Martial',
        'education': 'Education',
        'default' : 'Credit',
        'housing': 'Housing_loan',
        'loan' : 'Personal_loan',
        'contact' : 'Call_type',
        'month' : 'Last_month',
        'day_of_week': 'last_weekday',
        'duration': 'lastCall_Dur',
        'campaign' : 'NewCampaign_CallNo',
        'pdays' : 'Campaign_Intervals_Day',
        'previous': 'PrevCampaign_CallNo',
        'poutcome' : 'PrCampaign_Result',
        'y' : 'Campaign_Success'      
       }
  
# call rename () method
df.rename(columns=dict,
          inplace=True)
  
# print Data frame
display(df)


#color list for plots
color_list = ['#44546A', '#E31737', '#8497B0', '#FFC427', '#009999', '#00B0F0']




# Missing Values
# Finding total standard missing values for each feature
print(df.isnull().sum())

# Making a list of missing value types, "unknown" is shown in the dataset text file
missed_value = ["unknown"]

# reading the data again, with the defined non-standard missing value
new_df = pd.read_csv(url,sep=';', na_values = missed_value)

print(new_df.isnull().sum())