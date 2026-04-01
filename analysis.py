import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV
df = pd.read_csv("orders_export_clean.csv")

# Convert the timestamp column to datetime (replace 'Created at' with your column name)
df['Created at'] = pd.to_datetime(df['Created at'])
df['Created date'] = pd.to_datetime(df['Paid at'])

# Extract the day of the week as a new coludmn
df['Weekday'] = df['Created at'].dt.day_name()
df['Created date'] = df['Created at'].dt.date


# --- Map province abbreviations to full names ---
state_map = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
    'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota',
    'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island',
    'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
    'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
}

# Create new column with full state names
df['Billing State'] = df['Billing Province'].map(state_map)

# 5. Count orders per weekday and province
orders_per_day = df['Weekday'].value_counts()
orders_per_province = df['Billing State'].value_counts()
item_quantity = df["Item quantity"].value_counts()
item_name = df["Item name"].value_counts()
paid_date = df['Created date'].value_counts()

# 6. Show results
print(orders_per_day)
print(orders_per_province)
print(item_quantity)
print(item_name)
print(paid_date)


x = np.array(["XS", "S", "M", "L", "XL"])
y = np.array([1, 5, 8, 5, 4])

plt.bar(x,y)
plt.show()