# Load necessary library
library(ggplot2)

# Create the employee data frame
employee_data <- data.frame(
  EMPID = c(101, 102, 103, 104, 105, 106),
  Gender = c("Male", "Female", "Male", "Female", "Male", "Female"),
  Age = c(25, 30, 45, 28, 35, 40),
  Sales = c(200, 150, 300, 180, 250, 220),
  BMI = c("Normal", "Overweight", "Underweight", "Normal", "Overweight", "Normal"),
  Income = c(50000, 60000, 45000, 52000, 58000, 61000)
)

# View the data frame
print("Employee Data:")
print(employee_data)

# Create a table of BMI counts
bmi_counts <- table(employee_data$BMI)

# Create a pie chart
pie(bmi_counts,
    main = "BMI Distribution of Employees",
    col = rainbow(length(bmi_counts)),
    labels = paste(names(bmi_counts), round(100 * bmi_counts / sum(bmi_counts), 1), "%")
)
