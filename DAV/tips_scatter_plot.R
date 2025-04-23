# Install and load necessary packages
if (!require(ggplot2)) install.packages("ggplot2")
if (!require(readr)) install.packages("readr")
if (!require(dplyr)) install.packages("dplyr")

library(ggplot2)
library(readr)
library(dplyr)

# Load tips dataset from GitHub
tips <- read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Display top 10 records
cat("Top 10 Records:\n")
print(head(tips, 10))

# Scatter plot (jittered) of tips vs day
ggplot(tips, aes(x = day, y = tip)) +
  geom_jitter(width = 0.2, height = 0, color = "steelblue", alpha = 0.7) +
  theme_minimal() +
  ggtitle("Scatter Plot of Tips by Day") +
  xlab("Day of the Week") +
  ylab("Tip Amount")
