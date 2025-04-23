# Assuming 'dataz' is your dataset
dataset <- read.csv("D:/Engineering/Sem 6/DAV/viva/50_Startups.csv")

# Convert 'State' column into a factor
dataset$State <- factor(dataset$State,
                        levels = c('New York', 'California', 'Florida'),
                        labels = c(1, 2, 3))

# Load necessary package
library(caTools)

# Split the data into training and test sets
set.seed(123)
split <- sample.split(dataset$Profit, SplitRatio = 0.8)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

# Fit the Multiple Linear Regression model
regressor <- lm(formula = Profit ~ ., data = training_set)

# Predicting the Test set results
y_pred <- predict(regressor, newdata = test_set)

# Display the predicted values and the model summary
print("Predicted Profit Values:")
print(y_pred)

print("Model Summary:")
summary(regressor)

# Plot Actual vs Predicted Profits
plot(test_set$Profit, y_pred,
     main = "Actual vs Predicted Profits",
     xlab = "Actual Profit",
     ylab = "Predicted Profit",
     pch = 19, col = "blue")
abline(a = 0, b = 1, col = "red", lwd = 2)  # Line y = x


# Residuals (error between actual and predicted)
residuals <- test_set$Profit - y_pred

# Plot Residuals
plot(y_pred, residuals,
     main = "Residuals vs Predicted Profits",
     xlab = "Predicted Profit",
     ylab = "Residuals",
     pch = 19, col = "darkgreen")
abline(h = 0, col = "red", lty = 2)


# Standard diagnostic plots (4-in-1)
par(mfrow = c(2, 2))  # Plot in 2x2 grid
plot(regressor)
par(mfrow = c(1, 1))  # Reset layout
