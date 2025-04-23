# Install necessary packages if not installed
if (!require(ggplot2)) install.packages("ggplot2")
if (!require(dplyr)) install.packages("dplyr")
if (!require(readr)) install.packages("readr")

library(ggplot2)
library(dplyr)
library(readr)

# Load tips dataset from GitHub
tips <- read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Display top 10 records
cat("Top 10 Records:\n")
print(head(tips, 10))

# Summarize total tips by day
tips_by_day <- tips %>%
  group_by(day) %>%
  summarise(total_tip = sum(tip))

# Plot bar chart
ggplot(tips_by_day, aes(x = day, y = total_tip, fill = day)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  ggtitle("Total Tips by Day") +
  xlab("Day of the Week") +
  ylab("Total Tip Amount")
