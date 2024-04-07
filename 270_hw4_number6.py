import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('270 data/body_fat.xlsx', sheet_name='fat')

# Calculate the average weight and body fat for each age group
age_groups = df['AGE'].apply(lambda x: (x // 10) * 10)
grouped_data = df.groupby(age_groups).agg({'WEIGHT': 'mean', 'BODYFAT (BROZEK)': 'mean'}).reset_index()
grouped_data['AGE'] = grouped_data['AGE'].astype(str) + 's'

# Create a bar plot with two series
plt.figure(figsize=(10, 6))
bar_width = 0.35
opacity = 0.8

index = range(len(grouped_data))
plt.bar(index, grouped_data['WEIGHT'], bar_width, alpha=opacity, color='b', label='Weight')
plt.bar([i + bar_width for i in index], grouped_data['BODYFAT (BROZEK)'], bar_width, alpha=opacity, color='r', label='Body Fat')

plt.xlabel('Age Group')
plt.ylabel('Average Value')
plt.title('Average Weight and Body Fat by Age Group')
plt.xticks([i + bar_width/2 for i in index], grouped_data['AGE'])
plt.legend()
plt.grid(True)
plt.show()