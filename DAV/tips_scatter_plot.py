import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Display top 10 records
print("Top 10 Records:")
print(tips.head(10))

# Scatter plot of tip vs day (with jitter)
plt.figure(figsize=(8, 5))
sns.stripplot(x="day", y="tip", data=tips, jitter=True, palette="Set2", edgecolor="gray")
plt.title("Scatter Plot of Tips by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Tip Amount")
plt.grid(True)
plt.show()
