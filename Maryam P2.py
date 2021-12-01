# Age -> Age_Groups
age_ranges = [15,30,45,65,100]
age_labels = ['Young','Adult','Mid-aged','Senior']
direct_marketing['Age_Group'] = pd.cut(direct_marketing['Age'], bins=age_ranges, labels=age_labels, right=False)

# Plotting Age_Groups distribution
dm_Age_Group = pd.DataFrame(direct_marketing.groupby(['Age_Group']).size()).reset_index() 
dm_Age_Group = dm_Age_Group.rename(columns={0:'Count'}).sort_values('Count') 
fig17 = px.bar(dm_Age_Group, x='Age_Group', y='Count',
              color_discrete_sequence=['#009999'])
fig17.update_layout(xaxis_title_text='Age Group',
                   yaxis_title_text='Count',
                  title_text = 'The age group status for the campaign')
fig17.show()


# cleaning and transforming NewCampaign_CallNo
Q1 = direct_marketing['NewCampaign_CallNo'].quantile(0.25)
Q3 = direct_marketing['NewCampaign_CallNo'].quantile(0.75)
IQR = Q3 - Q1
#calculating whiskers
whis_low = (Q1 - 1.5 * IQR)
whis_high = (Q3 + 1.5 * IQR)
#filtering the outliers
direct_marketing_NewCampaign = direct_marketing.loc[direct_marketing['NewCampaign_CallNo'] > whis_low]
direct_marketing_NewCampaign = direct_marketing_NewCampaign.loc[direct_marketing_NewCampaign['NewCampaign_CallNo'] < whis_high]


#new distribution of "NewCampaign_CallNo" variable
fig3_2 = px.histogram(direct_marketing_NewCampaign['NewCampaign_CallNo'], 
                    nbins=10, title='Distribution of the times that a client has been contacted',
                   color_discrete_sequence=['#E31737'])
fig3_2.update_layout(xaxis_title_text='Frequency of client contact (times)',
    bargap=0.05, # gap between bars of adjacent location coordinates
    showlegend= False)
fig3_2.show()

# cleaning and transforming LastCall_Dur
Q1 = direct_marketing['LastCall_Dur'].quantile(0.25)
Q3 = direct_marketing['LastCall_Dur'].quantile(0.75)
IQR = Q3 - Q1
#calculating whiskers
whis_low = (Q1 - 1.5 * IQR)
whis_high = (Q3 + 1.5 * IQR)
#filtering the outliers
direct_marketing_LastCall_Dur = direct_marketing.loc[direct_marketing['LastCall_Dur'] > whis_low]
direct_marketing_LastCall_Dur = direct_marketing_LastCall_Dur.loc[direct_marketing_LastCall_Dur['LastCall_Dur'] < whis_high]

#new distribution of "LastCall_Dur" variable after cleaning
fig2_2 = px.histogram(direct_marketing_LastCall_Dur['LastCall_Dur'], 
                    nbins=100, title='Last Call Duration Distribution',
                   color_discrete_sequence=['#E31737'])
fig2_2.update_layout(xaxis_title_text='Last Call Duration (seconds)',
    bargap=0.05, # gap between bars of adjacent location coordinates
    showlegend= False)
fig2_2.show()
