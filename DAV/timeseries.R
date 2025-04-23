# Load required library
install.packages("lubridate")  # Only needed if not already installed
library(lubridate)

# Sample weekly data (you can replace this with real dataset)
cases <- c(500, 1500, 3500, 7000, 12000, 25000, 45000, 80000, 
           120000, 180000, 250000, 300000, 350000, 420000, 500000)

# Set the start date of the data
start_date <- ymd("2020-03-01")

# Create the time series object (weekly frequency)
covid_ts <- ts(cases, 
               start = decimal_date(start_date), 
               frequency = 365.25 / 7)

# Plot the graph (directly shown in RStudio or R GUI)
plot(covid_ts, 
     xlab = "Weekly Data", 
     ylab = "Total Positive Cases",
     main = "COVID-19 Weekly Case Trend", 
     col.main = "darkred")
