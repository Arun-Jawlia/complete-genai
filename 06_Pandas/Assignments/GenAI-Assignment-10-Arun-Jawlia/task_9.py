# Mini Use Case: Sales DAta Analysis

import pandas as pd
sales = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
}

df = pd.DataFrame(sales)
print(df)

total_revenue = df['Revenue'].sum()
average_daily_revenue = df['Revenue'].mean()
highest_revenue_day = df.loc[df['Revenue'].idxmax()]
above_average_sale = df[df['Revenue'] > average_daily_revenue]


print("\n Total Revenue:", total_revenue)
print("\n Average Revenue:", average_daily_revenue)
print("\n Day with Highest Revenue:", highest_revenue_day)
print("\n Days with Revenue Above Average:", above_average_sale)

# Plot Graph
df.plot(x='Day',y='Revenue',kind='line',title='Revenue vs Day')