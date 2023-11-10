import pandas as pd # in case of error, install pnadas using: pip install pandas
import random

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

i = 100

while i>0:

    new_data = {
        'Temp': random.randint(300,600),
        'Humd': random.randint(300,600),
        'Label': 0
    }

    i = i-1
    df = df.append(new_data, ignore_index=True)

# Step 3: Save the DataFrame to a new CSV file
df.to_csv("data_final.csv", index=False)