# Install and load necessary packages
if (!require(ggplot2)) install.packages("ggplot2")
if (!require(readr)) install.packages("readr")
if (!require(dplyr)) install.packages("dplyr")

library(ggplot2)
library(readr)
library(dplyr)

# Load tips dataset from GitHub
tips <- read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Show top 10 records
cat("Top 10 Records:\n")
print(head(tips, 10))

# Plot faceted histogram of tip by day
ggplot(tips, aes(x = tip)) +
  geom_histogram(binwidth = 0.5, fill = "skyblue", color = "black") +
  facet_wrap(~day) +
  theme_minimal() +
  ggtitle("Histogram of Tip Amount by Day") +
  xlab("Tip Amount") +
  ylab("Count")
