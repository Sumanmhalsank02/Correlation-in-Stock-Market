import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Stocks in to different dataframes
data1 = pd.read_csv(r'C:\Users\TATAPOWER.csv')
data2 = pd.read_csv(r'C:\Users\VOLTAS.csv')
data3 = pd.read_csv(r'C:\Users\APOLLOTYRE.csv')
data4 = pd.read_csv(r'C:\Users\BERGEPAINT.csv')
data5 = pd.read_csv(r'C:\Users\RBLBANK.csv')
nifty_index = pd.read_csv(r'C:\Users\Nifty50\Nifty50.csv')


# Retain the rows with Series column value as EQ/ Drop the rows with Series!= EQ
data1.drop(data1[data1['Series'] !='EQ'].index , inplace =True)
data2.drop(data2[data2['Series'] !='EQ'].index , inplace =True)
data3.drop(data3[data3['Series'] !='EQ'].index , inplace =True)
data4.drop(data4[data4['Series'] !='EQ'].index , inplace =True)
data5.drop(data5[data5['Series'] !='EQ'].index , inplace =True)

# Create a single Dataframe with the closing price of all the stocks
Data_CP = pd.concat([data1['Close Price'],
                     data2['Close Price'],
                     data3['Close Price'],
                     data4['Close Price'],
                     data5['Close Price']], axis=1)

# Rename the column names
Data_CP.columns = ['TATAPOWER_CP', 'VOLTAS_CP', 'APOLLOTYRE_CP', 'BERGEPAINT_CP', 'RBLBANK_CP']


# Another dataframe with the columns as the percentage change in the close price
Data_CP_Perc_Change = pd.concat([Data_CP['TATAPOWER_CP'].pct_change(),
                                 Data_CP['VOLTAS_CP'].pct_change(),
                                 Data_CP['APOLLOTYRE_CP'].pct_change(),
                                 Data_CP['BERGEPAINT_CP'].pct_change(),
                                 Data_CP['RBLBANK_CP'].pct_change()], axis=1)

# Rename the column names
Data_CP_Perc_Change.columns = ['TATAPOWER_PERC_CHANGE', 
                   'VOLTAS_PERC_CHANGE',
                   'APOLLOTYRE_PERC_CHANGE', 
                   'BERGEPAINT_PERC_CHANGE', 
                   'RBLBANK_PERC_CHANGE']


# Drop the 
Data_CP_Perc_Change = Data_CP_Perc_Change.dropna()


#finding the correlation between the percentage change i.e the correlation matrix
correlation = Data_CP_Perc_Change.corr()


# add a column for percentage in the daily closing prices in the nifty index
nifty_index['Nifty_Perc_Change'] = nifty_index['Close'].pct_change()
nifty_index = nifty_index.dropna()

# Using pairplot
sns.pairplot(Data_CP_Perc_Change)

# Show the plot
plt.show()
