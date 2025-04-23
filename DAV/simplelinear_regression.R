# Sample data
years_experience <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
salary <- c(35000, 40000, 45000, 50000, 60000, 65000, 70000, 75000, 80000, 85000)

# Create a data frame
data <- data.frame(years_experience, salary)

# Build the linear regression model
model <- lm(salary ~ years_experience, data = data)

# Summary of the model
summary(model)

# Plotting the data points
plot(data$years_experience, data$salary,
     main = "Salary vs Years of Experience",
     xlab = "Years of Experience",
     ylab = "Salary",
     pch = 16,
     col = "blue")

# Adding regression line
abline(model, col = "red", lwd = 2)

# Predict salary for 5.5 years of experience
predicted_salary <- predict(model, data.frame(years_experience = 5.5))
cat("Predicted salary for 5.5 years of experience is:", round(predicted_salary), "\n")
