# Create the employee data frame
employee_data <- data.frame(
  EMPID = c(101, 102, 103, 104, 105, 106),
  Gender = c("Male", "Female", "Male", "Female", "Male", "Female"),
  Age = c(25, 30, 45, 28, 35, 40),
  Sales = c(200, 150, 300, 180, 250, 220),
  BMI = c("Normal", "Overweight", "Underweight", "Normal", "Overweight", "Normal"),
  Income = c(50000, 60000, 45000, 52000, 58000, 61000)
)

# View data
print("Employee Data:")
print(employee_data)

# Histogram of Sales
hist(employee_data$Sales,
     main = "Histogram of Sales",
     xlab = "Sales",
     col = "skyblue",
     border = "black")
