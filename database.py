import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('model_movies_data.db')
conn1 = sqlite3.connect('emotion_movies_data.db')

# Define the SQL query
query = 'SELECT * FROM movies'
query1 = 'SELECT * FROM movies'


# Read the query results into a DataFrame
df = pd.read_sql_query(query, conn)
df1 = pd.read_sql_query(query1, conn1)

for columns in df:
	print(columns)

for columns in df1:
	print(columns)

select_emotion = input("which emotion type- movie do you want to watch?: ")
filtered_movies = df1.loc[df1[select_emotion] == 1]

print(filtered_movies.head())