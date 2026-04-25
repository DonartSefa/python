from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv('avgIQpercountry.csv')

print(df.info())

plt.figure(figsize=(10,6))

sns.histplot(df['Average IQ'])
plt.title('Histogram of Average IQ')
plt.xlabel('Aveage IQ')
plt.ylabel('Frequency')
plt.tight_layout
plt.show()