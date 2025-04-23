import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    'EMPID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Gender': ['M', 'F', 'F', 'M', 'F', 'M', 'M', 'F'],
    'Age': [25, 30, 28, 45, 38, 26, 31, 29],
    'Sales': [200, 150, 220, 300, 250, 180, 275, 160],
    'BMI': ['Normal', 'Overweight', 'Underweight', 'Normal', 'Overweight', 'Normal', 'Normal', 'Underweight'],
    'Income': [40000, 42000, 39000, 58000, 50000, 45000, 54000, 41000]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Employee Data:")
print(df)

# Create Box Plot for numeric attributes
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['Age', 'Sales', 'Income']])
plt.title('Box Plot of Age, Sales, and Income')
plt.grid(True)
plt.show()
