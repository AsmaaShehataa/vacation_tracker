#!/usr/bin/env python3

import pandas as pd

# Open the file
excel_file = "Lynks_db.xlsx"

df = pd.read_excel(excel_file)

print(df.head(30))

#No truncation in display 
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# Save the entire DataFrame to a new Excel file
df.to_excel("output_file.xlsx", index=False)

# total number of emp
print("Total number of employees:", len(df))

