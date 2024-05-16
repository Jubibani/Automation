import pandas as pd

# Specify the file path
file_path = r'C:\Quickie-Automation\pow.scripts\QuickiePow\modules\auto\login_sites\login_user\login_for_sites\login_for_sites.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the content of the DataFrame
print(df)
