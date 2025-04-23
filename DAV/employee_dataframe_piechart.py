import pandas as pd
import matplotlib.pyplot as plt

# Sample data for employees
data = {
    'EMPID': [101, 102, 103, 104, 105, 106],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Age': [25, 30, 45, 28, 35, 40],
    'Sales': [200, 150, 300, 180, 250, 220],
    'BMI': ['Normal', 'Overweight', 'Underweight', 'Normal', 'Overweight', 'Normal'],
    'Income': [50000, 60000, 45000, 52000, 58000, 61000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("Employee Data:")
print(df)

# Plotting Pie Chart for BMI distribution
bmi_counts = df['BMI'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(bmi_counts, labels=bmi_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('BMI Distribution of Employees')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
