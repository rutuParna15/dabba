import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Sample weekly data (same as in R)
cases = [500, 1500, 3500, 7000, 12000, 25000, 45000, 80000, 
         120000, 180000, 250000, 300000, 350000, 420000, 500000]

# Start date
start_date = datetime(2020, 3, 1)

# Create list of weekly dates
dates = [start_date + timedelta(weeks=i) for i in range(len(cases))]

# Create DataFrame
df = pd.DataFrame({'Date': dates, 'Cases': cases})
df.set_index('Date', inplace=True)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Cases'], marker='o', linestyle='-')
plt.title('COVID-19 Weekly Case Trend', color='darkred')
plt.xlabel('Date')
plt.ylabel('Total Positive Cases')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
