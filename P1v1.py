# importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import researchpy as rp
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from dataprep.eda import *
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
  
# print Data frame
display(direct_marketing)

#exploring the dataset
type (direct_marketing)
direct_marketing.shape
direct_marketing.head()
direct_marketing.tail()
direct_marketing.info()

#plotting the variables
#starting with numerical variables using px (plotly_express)

fig1 = px.histogram(direct_marketing['Age'], nbins=24, title='Age Distribution',
                   color_discrete_sequence=['#E31737']) #color is based on the theme of the presentation file
fig1.update_layout(xaxis_title_text='Age(years)',
    bargap=0.05, # gap between bars of adjacent location coordinates
    showlegend= False)
fig1.show()

fig2 = px.histogram(direct_marketing['LastCall_Dur'], 
                    nbins=60, title='Last Call Duration Distribution',
                   color_discrete_sequence=['#E31737'])
fig2.update_layout(xaxis_title_text='Last Call Duration (seconds)',
    bargap=0.05, # gap between bars of adjacent location coordinates
    showlegend= False)
fig2.show()

fig3 = px.histogram(direct_marketing['NewCampaign_CallNo'], 
                    nbins=60, title='Distribution of the times that a client has been contacted',
                   color_discrete_sequence=['#E31737'])
fig3.update_layout(xaxis_title_text='Frequency of client contact (times)',
    bargap=0.05, # gap between bars of adjacent location coordinates
    showlegend= False)
fig3.show()

fig4 = px.histogram(direct_marketing['Campaign_Intervals_Day'], 
                    nbins=60, title='Distribution of the days between the last two campaigns contact with clients',
                   color_discrete_sequence=['#E31737'])
fig4.update_layout(xaxis_title_text='Interval (days)',
    bargap=0.05, # gap between bars of adjacent location coordinates
    showlegend= False)
fig4.show()

fig5 = px.histogram(direct_marketing['PrevCampaign_CallNo'], 
                    nbins=60, title='Distribution of the number of the client calls during the last campign',
                   color_discrete_sequence=['#E31737'])
fig5.update_layout(xaxis_title_text='Number of times',
    bargap=0.05, # gap between bars of adjacent location coordinates
    showlegend= False)
fig5.show()

#now starting to plot the categorical variables using plotly_express barchart

dm_job = pd.DataFrame(direct_marketing.groupby(['Job']).size()).reset_index() #creating a dataframe consisting of the variable and its count
dm_job = dm_job.rename(columns={0:'Count'}).sort_values('Count') #renaming the column to Count and sorting them

fig6 = px.bar(dm_job, x='Job', y='Count',
              color_discrete_sequence=['#009999'])
fig6.update_layout(xaxis_title_text='Jobs',
                   yaxis_title_text='Count',
                  title_text = 'Clients Jobs')
fig6.show()

dm_Marital = pd.DataFrame(direct_marketing.groupby(['Marital']).size()).reset_index() #creating a dataframe consisting of the variable and its count
dm_Marital = dm_Marital.rename(columns={0:'Count'}).sort_values('Count') #renaming the column to Count and sorting them

fig7 = px.bar(dm_Marital, x='Marital', y='Count',
              color_discrete_sequence=['#009999'])
fig7.update_layout(xaxis_title_text='Marital statuses of clients',
                   yaxis_title_text='Count',
                  title_text = 'Marital Status')
fig7.show()

dm_Education = pd.DataFrame(direct_marketing.groupby(['Education']).size()).reset_index() #creating a dataframe consisting of the variable and its count
dm_Education = dm_Education.rename(columns={0:'Count'}).sort_values('Count') #renaming the column to Count and sorting them

fig8 = px.bar(dm_Education, x='Education', y='Count',
              color_discrete_sequence=['#009999'])
fig8.update_layout(xaxis_title_text='Education statuses of clients',
                   yaxis_title_text='Count',
                  title_text = 'Education Status')
fig8.show()

dm_Credit = pd.DataFrame(direct_marketing.groupby(['Credit']).size()).reset_index() #creating a dataframe consisting of the variable and its count
dm_Credit = dm_Credit.rename(columns={0:'Count'}).sort_values('Count') #renaming the column to Count and sorting them

fig9 = px.bar(dm_Credit, x='Credit', y='Count',
              color_discrete_sequence=['#009999'])
fig9.update_layout(xaxis_title_text='Default credit history of clients',
                   yaxis_title_text='Count',
                  title_text = 'Default credit')
fig9.show()

dm_Housing_loan = pd.DataFrame(direct_marketing.groupby(['Housing_loan']).size()).reset_index() #creating a dataframe consisting of the variable and its count
dm_Housing_loan = dm_Housing_loan.rename(columns={0:'Count'}).sort_values('Count') #renaming the column to Count and sorting them

fig10 = px.bar(dm_Housing_loan, x='Housing_loan', y='Count',
              color_discrete_sequence=['#009999'])
fig10.update_layout(xaxis_title_text='Active house loan status of clients',
                   yaxis_title_text='Count',
                  title_text = 'Active house loan status')
fig10.show()

dm_Personal_loan = pd.DataFrame(direct_marketing.groupby(['Personal_loan']).size()).reset_index() #creating a dataframe consisting of the variable and its count
dm_Personal_loan = dm_Personal_loan.rename(columns={0:'Count'}).sort_values('Count') #renaming the column to Count and sorting them

fig11 = px.bar(dm_Personal_loan, x='Personal_loan', y='Count',
              color_discrete_sequence=['#009999'])
fig11.update_layout(xaxis_title_text='Active personal loan status of clients',
                   yaxis_title_text='Count',
                  title_text = 'Active personal loan status')
fig11.show()

dm_Call_type = pd.DataFrame(direct_marketing.groupby(['Call_type']).size()).reset_index() #creating a dataframe consisting of the variable and its count
dm_Call_type = dm_Call_type.rename(columns={0:'Count'}).sort_values('Count') #renaming the column to Count and sorting them

fig12 = px.bar(dm_Call_type, x='Call_type', y='Count',
              color_discrete_sequence=['#009999'])
fig12.update_layout(xaxis_title_text='Clients device type',
                   yaxis_title_text='Count',
                  title_text = 'Clients device type')
fig12.show()

dm_Last_month = pd.DataFrame(direct_marketing.groupby(['Last_month']).size()).reset_index() #creating a dataframe consisting of the variable and its count
dm_Last_month = dm_Last_month.rename(columns={0:'Count'}).sort_values('Count') #renaming the column to Count and sorting them

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

dm_numeric = direct_marketing.loc[:,['Age', #creating a dataframe including all numeric variables
                                     'LastCall_Dur', 
                                     'NewCampaign_CallNo', 
                                     'Campaign_Intervals_Day','PrevCampaign_CallNo']]

plot_correlation(dm_numeric)