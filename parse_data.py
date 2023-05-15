import pandas as pd
import numpy as np
from datetime import datetime, timezone,date
import matplotlib.pyplot as plt

df = pd.read_csv('tweets.csv')
df['date'] = pd.to_datetime(df['date'])

min_date = df['date'].min()
max_date = df['date'].max()
print(min_date)
print(max_date)

#filtering english
#df = df[df['language'] == 'en']


#create bar per date
count_df = df.groupby(df['date'].dt.date).size()

count_df.plot.bar()

plt.title('Amount of tweets per day', fontsize=50)
plt.xlabel('Date', fontsize=40)
plt.ylabel('Amount tweets', fontsize=40)

plt.xticks(fontsize = 20, rotation=45)
plt.yticks(fontsize = 30)
plt.show()

#grouped by language
grouped_language = df.groupby(df['language']).size()
print(grouped_language.sort_values(ascending=False))



#create bar per datarange
df['date'] = df['date'].dt.date
grouped = df.groupby(df['date'])

date_first = date(2023, 2, 6)
date_second = date(2023, 2, 7)

dates_group_1 = [date_first,date_second]
rows_group_1 = []
for date_ in dates_group_1:
    rows_group_1.append(grouped.get_group(date_))
rows_group_1 = pd.concat(rows_group_1)


dates_group_2 = pd.date_range(start='2023-02-08', end='2023-02-21')
rows_group_2 = []
for date_ in dates_group_2:
    rows_group_2.append(grouped.get_group(date_.date()))
rows_group_2 = pd.concat(rows_group_2)
print(len(rows_group_2))
print(len(rows_group_1))

plt.bar(["2023-02-06 till 2023-02-07","2023-02-08 till 2023-02-21"],[len(rows_group_1),len(rows_group_2)])
plt.title('Amount of tweets per date range')
plt.xlabel('Daterange')
plt.ylabel('Amount tweets')
plt.show()