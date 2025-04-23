import seaborn as sns
import matplotlib.pyplot as plt

# Load tips dataset
tips = sns.load_dataset("tips")

# Display top 10 records
print("Top 10 Records:")
print(tips.head(10))

# Plot histogram of tip for each day
g = sns.FacetGrid(tips, col="day", col_wrap=2, height=4)
g.map(sns.histplot, "tip", bins=10, color="skyblue", edgecolor="black")
g.set_titles("Day: {col_name}")
g.fig.suptitle("Histogram of Tip Amount by Day", y=1.05)
plt.show()
