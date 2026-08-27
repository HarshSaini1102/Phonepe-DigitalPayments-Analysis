# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 12:25:54 2026

@author: Harsh
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

#loading data and displaying its structure 

print('\nPhonepe digital payments data analysis')
State_Txn_users = pd.read_excel(r"C:/Users/Harsh/Downloads/phonepe-pulse_raw-data_q12018-to-q22021-v0-1-5-1720351752.xlsx",
                              sheet_name='State_Txn and Users')


print("\nTop 5 rows of State_Txn and Users:\n\n",State_Txn_users.head(5))

State_TxnSplit = pd.read_excel(r"C:/Users/Harsh/Downloads/phonepe-pulse_raw-data_q12018-to-q22021-v0-1-5-1720351752.xlsx",
                              sheet_name='State_TxnSplit')

print("\nLast 10 rows of State_TxnSplit:\n\n",State_TxnSplit.tail(10))

State_DeviceData = pd.read_excel(r"C:/Users/Harsh/Downloads/phonepe-pulse_raw-data_q12018-to-q22021-v0-1-5-1720351752.xlsx",
                              sheet_name='State_DeviceData')

print('\n10 rows from the middle of State_DeviceData:\n\n',State_DeviceData.iloc[int(State_DeviceData.shape[0]/2):int((State_DeviceData.shape[0]/2)+10)])

District_txn_users = pd.read_excel(r"C:/Users/Harsh/Downloads/phonepe-pulse_raw-data_q12018-to-q22021-v0-1-5-1720351752.xlsx",
                              sheet_name='District_Txn and Users')

print("\nTop 10 rows of District_txn and Users:\n\n",District_txn_users.head(10))
print("\nLast 10 rows of District_Txn and Users:\n\n",District_txn_users.tail(10))

District_Demographics = pd.read_excel(r"C:/Users/Harsh/Downloads/phonepe-pulse_raw-data_q12018-to-q22021-v0-1-5-1720351752.xlsx",
                              sheet_name='District Demographics')
print("\nEvery 10 row from District Demographics:\n\n",District_Demographics.iloc[::10,])

# Each dataset summary statistics 

print("\nSummary statistics of State_Txn and Users:\n\n",State_Txn_users.describe())
print("\nSummary statistics of State_TxnSplit:\n\n",State_TxnSplit.describe())
print("\nSummary statistics of State_DeviceData:\n\n",State_DeviceData.describe())
print('\nSummary statistics of District_Txn and Users:\n\n',District_txn_users.describe())
print('\nSummary statistics of District Demographics:\n\n',District_Demographics.describe())

# Datatypes of each columns in each dataset
print("\nDatatypes of each columns in State_Txn and Users:\n\n",State_Txn_users.dtypes,sep='')
print("\nDatatypes of each columns in State_TxnSplit:\n\n",State_TxnSplit.dtypes,sep='')
print("\nDatatypes of each columns in State_DeviceData:\n\n",State_DeviceData.dtypes,sep='')
print("\nDatatypes of each columns in District_Txn and Users:\n\n",District_txn_users.dtypes,sep='')
print("\nDatatypes of each columns in District Demographics:\n\n",District_Demographics.dtypes,sep='')

#identifying missing values in each dataset
print("\nColumns with amount of missing values in State_Txn and Users:\n\n",State_Txn_users.isnull().sum(),sep='')
print("\nColumns with amount of missing values in State_TxnSplit:\n\n",State_TxnSplit.isnull().sum(),sep='')
print("\nColumns with amount of missing values in State_DeviceData:\n\n",State_DeviceData.isnull().sum(),sep='')
print("\nColumns with amount of missing values in District_Txn and Users:\n\n",District_txn_users.isnull().sum(),sep='')
print("\nColumns with amount of missing values in District Demographics:\n\n",District_Demographics.isnull().sum(),sep='')

#number of rows with missing values 
print("\nNumber of rows with missing values in State_Txn and Users:\n\n",State_Txn_users[State_Txn_users.isnull().any(axis=1)].shape[0],sep='')
print("\nNumber of rows with missing values in State_TxnSplit:\n\n",State_TxnSplit[State_TxnSplit.isnull().any(axis=1)].shape[0],sep='')
print('\nNumber of rows with missing values in State_DeviceData:\n\n',State_DeviceData[State_DeviceData.isnull().any(axis=1)].shape[0])
print('\nNumber of rows with missing values in District_Txn and Users:\n\n',District_txn_users[District_txn_users.isnull().any(axis=1)].shape[0])
print('\nNumber of rows with missing values District Demographics:\n\n',District_Demographics[District_Demographics.isnull().any(axis=1)].shape[0])

#Percentage of missing values for each column that has missing values 
print('\n\nPercentage of missing for each column of State_Txn and Users with missing values:\n')
print((State_Txn_users.isnull().mean()*100).loc[lambda x:x>0])

print('\n\nPercentage of missing for each column of State_TxnSplit with missing values:\n')
print((State_TxnSplit.isnull().mean()*100).loc[lambda x:x>0])

print('\n\nPercentage of missing for each column of State_DeviceData with missing values:\n')
print((State_DeviceData.isnull().mean()*100).loc[lambda x:x>0])

print('\n\nPercentage of missing for each column of District_Txn and Users with missing values:\n')
print((District_txn_users.isnull().mean()*100).loc[lambda x:x>0])

print('\n\nPercentage of missing for each column of District Demographics with missing values:\n')
print((District_Demographics.isnull().mean()*100).loc[lambda x:x>0])


#columns with highest percentage of missing values in each dataset 
print('\n\nColumn with highest percentage of missing values in State_Txn and Users:\n')
print((State_Txn_users.isnull().mean()*100).loc[lambda x:x>0].sort_values(ascending=False).head(1))

print('\n\nColumn with highest percentage of missing values in State_TxnSplit:\n')
print((State_TxnSplit.isnull().mean()*100).loc[lambda x:x>0].sort_values(ascending=False).head(1))

print('\n\nColumn with highest percentage of missing values in State_DeviceData:\n')
print((State_DeviceData.isnull().mean()*100).loc[lambda x:x>0].sort_values(ascending=False).head(1))

print('\n\nColumn with highest percentage of missing values in District_Txn and Users:\n')
print((District_txn_users.isnull().mean()*100).loc[lambda x:x>0].sort_values(ascending=False).head(1))

print('\n\nColumn with highest percentage of missing values in District Demographics:\n')
print((District_Demographics.isnull().mean()*100).loc[lambda x:x>0].sort_values(ascending=False).head(1))

#Total number state and total number of districts
print('\n\nTotal number of states:')
print(District_txn_users['State'].nunique())

print('\n\nTotal number of districts:')
print(District_txn_users['District'].nunique())

#State with highest number of districts 
print("\n\nState with the highest number of districts:\n\n")
print(District_Demographics.groupby('State').agg(district_count=('District','count')).sort_values(by='district_count',ascending=False).head(1))

#Exploratory Data Analysis 
# calculating total number of transactions and total transaction amount for each state over years
print("\n\nTotal number of transactions and total transaction amount for each state over years:\n\n")
print(State_Txn_users.groupby(['State','Year'])['Transactions','Amount (INR)'].sum().reset_index())

#top 5 states with the highest amount of transaction volumes
print('\nTop 5 states with the highest amoount of transaction volumes:\n')
print(State_Txn_users.groupby('State')['Transactions'].sum().reset_index().sort_values(by='Transactions',ascending=False).head(5))

#top 5 states with the lowest transaction volumes
print('\nTop 5 states with the lowest amoount of transaction volumes:\n')
print(State_Txn_users.groupby('State')['Transactions'].sum().reset_index().sort_values(by='Transactions',ascending=False).tail(5))

# most frequent transaction type for each state and quarter
a = State_TxnSplit.groupby(['State','Quarter','Transaction Type'])['Transactions'].sum().reset_index(name='count')
most_freq = a.loc[a.groupby(['State','Quarter'])['count'].idxmax()]

print('\n\nMost frequent transaction type for each state and quarter:\n')
print(most_freq)


#device brand with the highest number of users each state
b = State_DeviceData.groupby(['State','Brand'])['Registered Users'].sum().reset_index(name='brand_users')
most_freq_brand = b.loc[b.groupby('State')['brand_users'].idxmax()]
print('\n\nMost frequent brands for each state:\n')
print(most_freq_brand)

# calculating district with the highest population per state 
c = District_Demographics.groupby('State')['Population'].idxmax().reset_index(drop=True)
d = District_Demographics.loc[c]
print('\n\nDistrict with the highest population for each state:\n')
print(d)

#creating a column chart depicting district with the highest population
d['State_district'] = d['State'] + '-' + d['District']
d = d.sort_values(by='Population',ascending=False)

plt.figure(figsize=(12,8))

plt.bar(d['State_district'],d['Population'],color='blue',edgecolor='black')
plt.xticks(rotation=90)
plt.title('Districts with the highest population state wise',fontsize=15,fontweight='bold')
plt.xlabel('District State wise',fontsize=13,fontweight='bold')
plt.ylabel('Population',fontsize=13,fontweight='bold')
plt.tight_layout()
plt.show()

#average transaction value for each state 
e = District_txn_users.groupby('State')['ATV (INR)'].mean().reset_index()
print('\n\nAverage transaction value for each state:\n')
print(e)

e = e.sort_values(by='ATV (INR)',ascending=False)
print('\n\nTop 5 states with highest ATV:\n')
print(e.head(5))

print('\n\nTop 5 states with lowest ATV:\n')
print(e.tail(5))

#Total number of app opens state,year and quarter wise
f = District_txn_users.groupby(['State','Year','Quarter'])['App Opens'].sum().reset_index()
print('\n\nTotal number of app opens state,year and quarter wise:\n')
print(f)

#creating a line plot showing number of app opens overtime for a selected state Delhi
selected_state = f.loc[f['State']=="Delhi"]
selected_state['Year-Quarter'] = selected_state['Year'].astype(str) + '-Q' +selected_state['Quarter'].astype(str)

plt.figure(figsize=(12,8))
plt.plot(selected_state['Year-Quarter'],selected_state['App Opens'],marker='o',linewidth=2)
plt.xlabel('Year-Quarter',fontsize=13,fontweight='bold')
plt.ylabel('Amount of app opens',fontsize=13,fontweight='bold')
plt.title('App opens for Delhi year and quarter overtime',fontsize=15,fontweight='bold')
plt.grid(True,linestyle='-',alpha=0.5)
plt.tight_layout()
plt.show()

#creating a bar showing distribution of transaction types for each 
#state in latest quarter
import seaborn as sns

latest_year = State_TxnSplit['Year'].max()
latest_quarter = State_TxnSplit[State_TxnSplit['Year']==latest_year]['Quarter'].max()

latest_data = State_TxnSplit[(State_TxnSplit['Year']==latest_year) & (State_TxnSplit['Quarter']==latest_quarter)]
plt.figure(figsize=(14,8))
sns.set_theme(style='whitegrid')
sns.barplot(data = latest_data,
            x='State',
            y='Transactions',
            hue='Transaction Type')
plt.xlabel('State',fontsize=13,fontweight='bold')
plt.ylabel('Transactions',fontsize=13,fontweight='bold')
plt.title('Distribution of transaction type',fontsize=15,fontweight='bold')
plt.xticks(rotation=90)
plt.legend(title='Transaction Type', bbox_to_anchor=(1.02, 1), loc='upper left')

plt.tight_layout()
plt.show()

#uniquemapping between district and code
mapping = District_Demographics[['District','Code']].drop_duplicates()
print('\n\nUnique mapping between district and code:\n')
print(mapping)

#creating a csv containing unique district name and district code
print(mapping.to_csv(r'C:\Users\Harsh\Desktop\district_namem_code_mapping1.csv',index=False))

#summed values as per district level data
district_level_data = District_txn_users.groupby('State')['Transactions','Amount (INR)','Registered Users'].sum().reset_index()
State_level_data = State_Txn_users.groupby('State')['Transactions','Amount (INR)','Registered Users'].sum().reset_index()

#comparing grouped values of district and state level data
identical = district_level_data.equals(State_level_data)
print(f'Is state level data identical to district {identical}')

#finding any discrepency between district and statelevel data
#pd.testing.assert_frame_equal(district_level_data, State_level_data,check_dtype=False)

#merging state_txn_users and district demographics to find the ratio of registered users and population
merge_state_txn_users_district = pd.merge(State_Txn_users,District_Demographics,how='inner',on='State')

state_data = merge_state_txn_users_district.groupby('State')[['Registered Users','Population']].sum().reset_index()
state_data['Ratio'] = state_data['Registered Users']/state_data['Population']
print('\nRatio of total registered users and total population in each state:\n')
print(state_data['Ratio'])
#creating column chart depicting a ratio of users to population

plt.figure(figsize=(14,8))
sns.barplot(data=state_data,x='State',y='Ratio',color='skyblue')
plt.xticks(rotation=90)
plt.xlabel('State',fontsize=13,fontweight='bold')
plt.ylabel('Ratio',fontsize=13,fontweight='bold')
plt.title('State and their ratio',fontsize=15,fontweight='bold')
plt.tight_layout()
plt.show()

#merging and finding correlation between population density and transactions
merge_district_txn_district_demo = pd.merge(District_txn_users,District_Demographics,on=['State','District','Code'],how='inner')
merge_district_txn_district_demo['Population density'] = merge_district_txn_district_demo['Population']/merge_district_txn_district_demo['Area (sq km)']
clean_df = merge_district_txn_district_demo.replace([np.inf,-np.inf],np.nan).dropna(subset=['Population density','Transactions'])
corr = clean_df['Population density'].corr(clean_df['Transactions']) 
print('\n\nCorrelation between population density and transactions:',round(corr,3))

#creating a scatter plot to visualize relationship between population density and transactions

plt.figure(figsize=(12,8))
sns.set_theme(style='whitegrid')
sns.regplot(clean_df,x='Population density',y='Transactions',scatter_kws={'alpha':0.6,'color':'lightblue','s':50},
            line_kws={'color':'red','linewidth':2,'label':f'Trendline (r={corr:.2f})'})
plt.title('Correlation between population density and transactions',fontsize=15,fontweight='bold')
plt.xlabel('Population density',fontsize=13,fontweight='bold')
plt.ylabel('Transaction volume',fontsize=13,fontweight='bold')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

#calculating average transaction amount per user for each state

state_amount = State_Txn_users.groupby('State')['Amount (INR)'].sum().reset_index()

#geting latest registered uses to prevent cumulative addition
latest_year = State_Txn_users['Year'].max()
latest_quarter = State_Txn_users[State_Txn_users['Year']==latest_year]['Quarter'].max()
latest_data = State_Txn_users[(State_Txn_users['Year']==latest_year) & (State_Txn_users['Quarter']==latest_quarter)][['State','Registered Users']]

merge_df = pd.merge(state_amount,latest_data,on='State',how='inner')

merge_df['Average transaction amount per user'] = merge_df['Amount (INR)']/merge_df['Registered Users']


result = merge_df[['State','Registered Users']].sort_values(by='Registered Users',ascending=False)

print("\n\nDataframe for average transaction amount per user per state:\n")
print(result)

top_5_highest_avg_trans = result.head(5)
top_5_lowest_avg_transc = result.tail(5)

print('\nTop 5 states with highest Average transaction amount per user per state:\n')
print(top_5_highest_avg_trans)

print('\nTop 5 states with lowest Average transaction amount per user per state:\n')
print(top_5_lowest_avg_transc)

#merging State_Txn_users and State_DeviceData
merge_state_device_state_txn = pd.merge(State_Txn_users,State_DeviceData,on=['State','Year','Quarter'],how='inner')

state_users = merge_state_device_state_txn.groupby('State')['Registered Users_x'].sum().reset_index(name='Total Users')
brand_users = merge_state_device_state_txn.groupby(['State','Brand'])['Registered Users_y'].sum().reset_index(name='brand_users')

merge_state_wise_brand_users = pd.merge(state_users,brand_users,on='State',how='inner')
merge_state_wise_brand_users['Ratio'] = merge_state_wise_brand_users['brand_users']/merge_state_wise_brand_users['Total Users']
print('\nRatio of users using each device brand to the total number of registered users in each state\n')
print(merge_state_wise_brand_users)

#barchar depicting the ratio for top 5 brands
top_5_brands = merge_state_wise_brand_users.groupby('Brand')['brand_users'].sum().nlargest(5).index

plot_data = merge_state_wise_brand_users[merge_state_wise_brand_users['Brand'].isin(top_5_brands)]

plt.figure(figsize=(14,8))
sns.barplot(data=plot_data,x='State',y='Ratio',hue='Brand')
plt.title('Top 5 brands Usage ratio by state',fontsize=15,fontweight='bold',pad=15)
plt.xlabel('State',fontsize=13,fontweight='bold')
plt.ylabel('User ratio (Brand Users/Total Users)',fontsize=13,fontweight='bold')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#creating a plot for total transaction and amount overtime for a selected state

delhi_aggregated = District_txn_users[District_txn_users['State']=='Delhi'].groupby(['Year','Quarter'])[['Transactions','Amount (INR)']].sum().reset_index()
delhi_aggregated['Quarter-period'] = delhi_aggregated['Year'].astype(str) + '-Q' + delhi_aggregated['Quarter'].astype(str)
delhi_aggregated = delhi_aggregated.sort_values(by=['Year','Quarter'])

fig,(ax1,ax2) = plt.subplots(2,1,figsize=(12,8),sharex=True)
ax1.plot(delhi_aggregated['Quarter-period'],delhi_aggregated['Transactions'],color='red',marker='o',linewidth=2.5)
ax1.set_title('Delhi: Total Transactions overtime',fontsize=15,fontweight='bold')
ax1.set_ylabel('Transactions',fontsize=13,fontweight='bold')

ax2.plot(delhi_aggregated['Quarter-period'],delhi_aggregated['Amount (INR)'],color='blue',marker='s',linewidth=2.5)
ax2.set_title('Delhi transaction overtime',fontsize=15,fontweight='bold')
ax2.set_ylabel('Amount (INR)',fontsize=13,fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#creating a piechart for distribution of type of transactions for a selected state and quarter
State = 'Delhi'
year = 2021 
quarter = 1 
filtered_df = State_TxnSplit[(State_TxnSplit['State']==State) & (State_TxnSplit['Quarter']==quarter)]
type_summary = filtered_df.groupby('Transaction Type')['Transactions'].sum().reset_index()
plt.figure(figsize=(8,8))
palette_color = sns.color_palette('pastel')
plt.pie(type_summary['Transactions'],labels=type_summary['Transaction Type'],autopct='%1.1f%%',
        startangle=140,colors=palette_color,wedgeprops={'edgecolor':'white','linewidth':1.5})
plt.title(f'Transaction type distribution in {State} {year}-Q{quarter}',fontsize=14,fontweight='bold',pad=20)
plt.tight_layout()
plt.show()

#creating a bar chart for population denity of districts in a selected state
selected_state = 'Delhi'
state_df = District_Demographics[District_Demographics['State']==selected_state]
state_df['Population density'] = state_df['Population']/state_df['Area (sq km)']
clean_df = state_df[['District','Population density']].replace([np.inf,-np.inf],np.nan).dropna().sort_values(by='Population density',ascending=False)
clean_df = clean_df[clean_df['Population density'] > 0]

plt.figure(figsize=(14,8))
sns.barplot(data=clean_df,x='District',y='Population density',color='red')
plt.xticks(rotation=90)
plt.title('Population density in each district of Delhi',fontsize=15,fontweight='bold')
plt.xlabel('District',fontsize=13,fontweight='bold')
plt.ylabel('Population density',fontsize=13,fontweight='bold')
plt.tight_layout()
plt.show()

#analyzing transaction data to identify any pattern

quarterly_txn = (
    State_Txn_users
    .groupby(['Year', 'Quarter'])['Transactions']
    .sum()
    .reset_index()
)

quarterly_txn['Year_Quarter'] = (
    quarterly_txn['Year'].astype(str)
    + '-Q'
    + quarterly_txn['Quarter'].astype(str)
)

print('\n\nTransactions yearly and quarterly:\n')
print(quarterly_txn)

import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))

plt.plot(
    quarterly_txn['Year_Quarter'],
    quarterly_txn['Transactions'],
    marker='o',
    linewidth=2
)

plt.title('Quarterly Transaction Volume Trend', fontsize=15,fontweight='bold')
plt.xlabel('Year and Quarter', fontsize=13,fontweight='bold')
plt.ylabel('Total Transactions', fontsize=13,fontweight='bold')

plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

quarterly_txn['QoQ Growth (%)'] = (
    quarterly_txn['Transactions']
    .pct_change() * 100
)

print('\n\nTransactions yearly and quarterly with QoQ Growth(%):\n')
print(quarterly_txn)

highest_growth = quarterly_txn.loc[
    quarterly_txn['QoQ Growth (%)'].idxmax()
]

print(
    '\nHighest growth:',
    highest_growth['Year_Quarter'],
    round(highest_growth['QoQ Growth (%)'],3)
)

largest_decline = quarterly_txn.loc[
    quarterly_txn['QoQ Growth (%)'].idxmin()
]

print(
    'Largest decline:',
    largest_decline['Year_Quarter'],
    round(largest_decline['QoQ Growth (%)'],3)
)

peak = quarterly_txn.loc[
    quarterly_txn['Transactions'].idxmax()
]

print(
    'Peak transaction volume:',
    peak['Year_Quarter'],
    peak['Transactions']
)

#as calculated earlier
merge_district_txn_district_demo = pd.merge(District_txn_users,District_Demographics,on=['State','District','Code'],how='inner')
merge_district_txn_district_demo['Population density'] = merge_district_txn_district_demo['Population']/merge_district_txn_district_demo['Area (sq km)']
clean_df = merge_district_txn_district_demo.replace([np.inf,-np.inf],np.nan).dropna(subset=['Population density','Transactions'])
corr = clean_df['Population density'].corr(clean_df['Transactions']) 
print('\nCorrelation between population density and transactions:',round(corr,3))
