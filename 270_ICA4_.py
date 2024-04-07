import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('270 data/body_fat.xls', sheet_name='fat')

# Body Fat vs Weight
plt.figure(figsize=(8, 6))
plt.scatter(df['WEIGHT'], df['BROZEK'])
plt.xlabel('Weight')
plt.ylabel('Body Fat (Brozek)')
plt.title('Body Fat vs Weight')
plt.grid(True)
plt.show()

# Body Fat vs Height
plt.figure(figsize=(8, 6))
plt.scatter(df['HEIGHT'], df['BROZEK'])
plt.xlabel('Height')
plt.ylabel('Body Fat (Brozek)')
plt.title('Body Fat vs Height')
plt.grid(True)
plt.show()

# Body Fat vs Circumference
plt.figure(figsize=(8, 6))
plt.plot(df['NECK'], df['BROZEK'], marker='o', label='Neck')
plt.plot(df['THIGH'], df['BROZEK'], marker='s', label='Thigh')
plt.plot(df['BICEP'], df['BROZEK'], marker='^', label='Bicep')
plt.xlabel('Circumference')
plt.ylabel('Body Fat (Brozek)')
plt.title('Body Fat vs Circumference')
plt.legend()
plt.grid(True)
plt.show()