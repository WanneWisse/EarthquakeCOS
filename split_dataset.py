import pandas as pd

# Load your DataFrame
df = pd.read_csv('tweets.csv')
df = df[df['language'] != 'en'] 
# Calculate the number of rows in each part
num_rows = len(df)
rows_per_part = num_rows // 5

# Split the DataFrame into five parts
parts = [df[i * rows_per_part:(i + 1) * rows_per_part] for i in range(5)]

# Save each part to a separate CSV file
for i, part in enumerate(parts):
    part.to_csv(f'part_{i+1}.csv', index=False)
