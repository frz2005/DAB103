#import libraries
import pandas as pd
import numpy as np
import plotly_express as px
#importing the dataset
direct_marketing = pd.read_csv('https://query.data.world/s/lqrsaugj7kwkyazkvydowjuxjrybxx', sep=';')
# New_Name a dictionary
# key = old name
# value = new name
dict = {'age': 'Age',
        'job': 'Job',
        'marital': 'Marital',
        'education': 'Education',
        'default' : 'Credit',
        'housing': 'Housing_loan',
        'loan' : 'Personal_loan',
        'contact' : 'Call_type',
        'month' : 'Last_month',
        'day_of_week': 'Last_weekday',
        'duration': 'LastCall_Dur',
        'campaign' : 'NewCampaign_CallNo',
        'pdays' : 'Campaign_Intervals_Day',
        'previous': 'PrevCampaign_CallNo',
        'poutcome' : 'PrCampaign_Result',
        'y' : 'Campaign_Success'      
       }

# call rename () method
direct_marketing.rename(columns=dict, inplace=True)

#plot 4 variables using plotly express bar chart and presentation theme colors
fig13 = px.bar(dm_Last_month, x='Last_month', y='Count',
              color_discrete_sequence=['#009999'])
fig13.update_layout(xaxis_title_text='Months of the last call of the Client',
                   yaxis_title_text='Count',
                  title_text = 'Last month')
fig13.show()

dm_Last_weekday = pd.DataFrame(direct_marketing.groupby(['Last_weekday']).size()).reset_index() #creating a dataframe consisting of the variable and its count
dm_Last_weekday = dm_Last_weekday.rename(columns={0:'Count'}).sort_values('Count') #renaming the column to Count and sorting them

fig14 = px.bar(dm_Last_weekday, x='Last_weekday', y='Count',
              color_discrete_sequence=['#009999'])
fig14.update_layout(xaxis_title_text='Week day of the last call of the Client',
                   yaxis_title_text='Count',
                  title_text = 'Last weekday')
fig14.show()

dm_PrCampaign_Result = pd.DataFrame(direct_marketing.groupby(['PrCampaign_Result']).size()).reset_index() #creating a dataframe consisting of the variable and its count
dm_PrCampaign_Result = dm_PrCampaign_Result.rename(columns={0:'Count'}).sort_values('Count') #renaming the column to Count and sorting them

fig15 = px.bar(dm_PrCampaign_Result, x='PrCampaign_Result', y='Count',
              color_discrete_sequence=['#009999'])
fig15.update_layout(xaxis_title_text='Previous campaign result of the contact with clients',
                   yaxis_title_text='Count',
                  title_text = 'The result of the previous campaign')
fig15.show()

dm_Campaign_Success = pd.DataFrame(direct_marketing.groupby(['Campaign_Success']).size()).reset_index() #creating a dataframe consisting of the variable and its count
dm_Campaign_Success = dm_Campaign_Success.rename(columns={0:'Count'}).sort_values('Count') #renaming the column to Count and sorting them

fig16 = px.bar(dm_Campaign_Success, x='Campaign_Success', y='Count',
              color_discrete_sequence=['#009999'])
fig16.update_layout(xaxis_title_text='The success for this campaign',
                   yaxis_title_text='Count',
                  title_text = 'The success status for the campaign')
fig16.show()