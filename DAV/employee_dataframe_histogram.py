import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    'EMPID': [101, 102, 103, 104, 105, 106],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Age': [25, 30, 45, 28, 35, 40],
    'Sales': [200, 150, 300, 180, 250, 220],
    'BMI': ['Normal', 'Overweight', 'Underweight', 'Normal', 'Overweight', 'Normal'],
    'Income': [50000, 60000, 45000, 52000, 58000, 61000]
}

df = pd.DataFrame(data)

# Display DataFrame
print("Employee Data:")
print(df)

# Histogram of Sales
plt.figure(figsize=(8, 5))
plt.hist(df['Sales'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Sales')
plt.xlabel('Sales')
plt.ylabel('Number of Employees')
plt.grid(True)
plt.show()
