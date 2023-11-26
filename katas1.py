# https://www.kaggle.com/code/janiobachmann/price-of-avocados-pattern-recognition-analysis/notebook
# pip install pandas
import pandas as pd
# Replace 'your_file.csv' with the actual path to your CSV file
file_path = 'avocado.csv/avocado.csv'
# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)
# Get a summary of the DataFrame
summary = df.describe()
# Print the summary
print(summary)