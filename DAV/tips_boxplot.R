# Install necessary packages
if (!require(ggplot2)) install.packages("ggplot2")
if (!require(dplyr)) install.packages("dplyr")
if (!require(readr)) install.packages("readr")

library(ggplot2)
library(dplyr)
library(readr)

# Load tips dataset from a GitHub source
tips <- read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Show top 10 records
cat("Top 10 Records:\n")
print(head(tips, 10))

# Plot boxplot of tip vs day
ggplot(tips, aes(x = day, y = tip, fill = day)) +
  geom_boxplot() +
  theme_minimal() +
  ggtitle("Boxplot of Tips by Day") +
  xlab("Day of the Week") +
  ylab("Tip Amount")

