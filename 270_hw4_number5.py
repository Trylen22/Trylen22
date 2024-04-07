import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('270 data/body_fat.xlsx', sheet_name='fat')

# Body Fat vs Weight
plt.figure(figsize=(8, 6))
plt.scatter(df['WEIGHT'], df['BODYFAT (BROZEK)'])
plt.xlabel('Weight')
plt.ylabel('Body Fat (Brozek)')
plt.title('Body Fat vs Weight')
plt.grid(True)
#plt.show()

# Body Fat vs Height
plt.figure(figsize=(8, 6))
plt.scatter(df['HEIGHT'], df['BODYFAT (BROZEK)'])
plt.xlabel('Height')
plt.ylabel('Body Fat (Brozek)')
plt.title('Body Fat vs Height')
plt.grid(True)
#plt.show()

# Body Fat vs Circumference
plt.figure(figsize=(8, 6))
plt.scatter(df['NECK'], df['BODYFAT (BROZEK)'], color='red', marker='o', label='Neck')
plt.scatter(df['THIGH'], df['BODYFAT (BROZEK)'], color='blue', marker='s', label='Thigh')
plt.scatter(df['BICEPS'], df['BODYFAT (BROZEK)'], color='green', marker='^', label='Biceps')
plt.xlabel('Circumference')
plt.ylabel('Body Fat (Brozek)')
plt.title('Body Fat vs Circumference')
plt.legend()
plt.grid(True)
plt.show()