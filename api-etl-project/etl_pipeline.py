import pandas as pd
import sqlite3
import requests
from datetime import datetime
import os

print("API + Sales Analytics Pipeline")
os.makedirs('data', exist_ok=True)

#live api call
print("Fetching LIVE API data...")
response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.json()

api_df = pd.DataFrame(users)
api_df = api_df[['id', 'name', 'email', 'address']].copy()
api_df['city'] = api_df['address'].apply(lambda x: x['city'])
api_df.to_excel('data/live_api_users.xlsx', index=False)
print(f"LIVE API: {len(api_df)} real users fetched")

#professional sales data
print("Creating enterprise sales...")
sales_data = []
for i in range(1000):
    sales_data.append({
        'order_id': f"ORD{i+1}",
        'sales_rep_id': users[i%10]['id'],
        'sales_rep_name': users[i%10]['name'],
        'region': ['North', 'South', 'East', 'West'][i%4],
        'product': ['Laptop', 'Phone', 'Tablet'][i%3],
        'quantity': 1 + (i%5),
        'price': 30000 + (i%70000),
        'total_sales': 0
    })

df = pd.DataFrame(sales_data)
df['total_sales'] = df['quantity'] * df['price']
df.to_excel('data/raw_sales.xlsx', index=False)
print(f"1000 sales records created")

#clean + merge excel (vlookup)
print("Data cleaning...")
df_clean = df[df['total_sales'] > 0].copy()
df_clean['region_clean'] = df_clean['region'].str.upper()
df_clean['high_value'] = df_clean['total_sales'] > df['total_sales'].quantile(0.8)

#merge api data
final_df = df_clean.merge(api_df[['id', 'name', 'city']], 
                         left_on='sales_rep_id', right_on='id', how='left')
final_df.drop('id', axis=1, inplace=True)

pivot = final_df.pivot_table(values='total_sales', 
                           index='region_clean', 
                           columns='high_value', 
                           aggfunc='sum', fill_value=0)
pivot.to_excel('data/sales_pivot.xlsx')
print("Excel pivot created!")

#sql analytics
print("SQL database...")
conn = sqlite3.connect('data/sales_api.db')
final_df.to_sql('sales_performance', conn, if_exists='replace', index=False)

query = """
SELECT region_clean, sales_rep_name, 
       SUM(total_sales) as rep_revenue,
       COUNT(*) as orders 
FROM sales_performance 
GROUP BY region_clean, sales_rep_name 
ORDER BY rep_revenue DESC LIMIT 10
"""
top_performers = pd.read_sql(query, conn)
top_performers.to_csv('data/top_sales_reps.csv', index=False)
conn.close()

print("\nTOP 10 PERFORMING SALES REPS:")
print(top_performers.head(10))
print("\nCOMPLETE! Check data/ folder")