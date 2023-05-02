import json
import pandas as pd

# Read the first JSON file
with open('banners.json', 'r') as f:
    data1 = json.load(f)
    
# Read the second JSON file
with open('BU.json', 'r') as f:
    data2 = json.load(f)
    
# Convert each list to a Pandas DataFrame
df1 = pd.DataFrame(data1, columns=['Banners'])
df2 = pd.DataFrame(data2, columns=['BU'])

# Concatenate the two DataFrames side by side
result = pd.concat([df1, df2], axis=1)

# Write the result to an Excel file
result.to_excel('output.xlsx', index=False)
