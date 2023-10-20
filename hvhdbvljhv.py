import pandas as pd

# Sample DataFrame
data = pd.read_csv("./application.csv")
df = pd.DataFrame(data)
output_file = "./abc.csv"

df['Date'] = pd.to_datetime(df['Time Created']).dt.strftime('%Y-%m-%dT')
df['Time'] = pd.to_datetime(df['Time Created']).dt.strftime(' %H:%M:%S.%f')

# Save the modified DataFrame to a new CSV file
df.to_csv(output_file, index=False)

print("Date and time separated and saved to", output_file)
# Function to calculate End Time
