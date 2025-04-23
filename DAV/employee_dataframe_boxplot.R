# Create the data
EMPID <- c(101, 102, 103, 104, 105, 106, 107, 108)
Gender <- c("M", "F", "F", "M", "F", "M", "M", "F")
Age <- c(25, 30, 28, 45, 38, 26, 31, 29)
Sales <- c(200, 150, 220, 300, 250, 180, 275, 160)
BMI <- c("Normal", "Overweight", "Underweight", "Normal", "Overweight", "Normal", "Normal", "Underweight")
Income <- c(40000, 42000, 39000, 58000, 50000, 45000, 54000, 41000)

# Create a DataFrame
employee_df <- data.frame(EMPID, Gender, Age, Sales, BMI, Income)

# View the data
print(employee_df)

# Boxplot for Age, Sales, and Income
boxplot(employee_df$Age, employee_df$Sales, employee_df$Income,
        names = c("Age", "Sales", "Income"),
        main = "Boxplot of Age, Sales, and Income",
        col = c("skyblue", "orange", "lightgreen"))
