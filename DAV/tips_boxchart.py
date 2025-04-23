import seaborn as sns
import matplotlib.pyplot as plt

# Load the 'tips' dataset
tips = sns.load_dataset("tips")

# Display top 10 records
print("Top 10 Records:")
print(tips.head(10))

# Plot boxplot of tips vs day
plt.figure(figsize=(8, 5))
sns.boxplot(x="day", y="tip", data=tips, palette="pastel")
plt.title("Boxplot of Tips by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Tip Amount")
plt.grid(True)
plt.show()
