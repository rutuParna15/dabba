import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load tips dataset
tips = sns.load_dataset("tips")

# Display top 10 records
print("Top 10 Records:")
print(tips.head(10))

# Group data by day and sum tips
tips_by_day = tips.groupby("day")["tip"].sum().reset_index()

# Plot bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x="day", y="tip", data=tips_by_day, palette="Blues_d")
plt.title("Total Tips by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Tip Amount")
plt.grid(True)
plt.show()
