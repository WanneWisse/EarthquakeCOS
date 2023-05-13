import pandas as pd
import numpy as np
from datetime import datetime, timezone,date
import matplotlib.pyplot as plt

df = pd.read_csv('tweets.csv')
print(df['source'])
df = df[df['language'] == 'en']
#print(a.columns)

df['date'] = pd.to_datetime(df['date'])

# count_df = df.groupby(df['date'].dt.date).size()

# # Print the resulting DataFrame
# print(count_df)

# count_df.plot.bar()

# # Set the plot title and axis labels
# plt.title('Amount of tweets per day')
# plt.xlabel('Date')
# plt.ylabel('Amount tweets')

# # Show the plot
# plt.show()
df['date'] = df['date'].dt.date
print(df)
grouped = df.groupby(df['date'])

grouped2 = df.groupby(df['date']).size()
print(grouped2)

print(grouped.groups.keys())
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
    print(type(date_))
    rows_group_2.append(grouped.get_group(date_.date()))
rows_group_2 = pd.concat(rows_group_2)
print(len(rows_group_2))
print(len(rows_group_1))

# Create a bar plot of the group sizes

# Convert the 'date' column to datetime type
# df['date'] = pd.to_datetime(df['date']).dt.tz_convert('UTC')
# print()
# 
# # Get the minimum and maximum dates
# min_date = df['date'].min()
# max_date = df['date'].max()
# print(min_date)
# print(max_date)
# print(df["language"])
# earth_quake_time = datetime(2023, 2, 6, 1, 17, 0, tzinfo=timezone.utc)
# pre_data = df[(df['date'] < earth_quake_time)]
# print(pre_data)

# # Define the step size (in minutes)
# step_size = 30

# # Round down the datetimes to the nearest step size
# df['rounded_datetime'] = pd.to_datetime(df['datetime'].dt.floor(f'{step_size}T'))