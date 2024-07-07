# Brooks Roberts
# 7/7/24
# 7 Assignment

import mysql.connector

# Connect to database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="movies_user",
    password="popcorn",
    database="movies"    
)

# Create a cursor object to execute SQL queries
cursor = db_connection.cursor()

# Query 1: Select all fields from the studio table
cursor.execute("SELECT * FROM studio")
studio_records = cursor.fetchall()
print("\n-- DISPLAYING Studio RECORDS --")
for record in studio_records:
    print(f"Studio ID: {record[0]}, Studio Name: {record[1]}")

# Query 2: Select all fields from the genre table
cursor.execute("SELECT * FROM genre")
genre_records = cursor.fetchall()
print("\n-- DISPLAYING Genre RECORDS --")
for record in genre_records:
    print(f"Genre ID: {record[0]}, Genre Name: {record[1]}")

# Query 3: Select movie names and runtimes where runtime is less than two hours (120 minutes)
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
short_movies = cursor.fetchall()
print("\n-- DISPLAYING Short Film RECORDS --")
for movie in short_movies:
    print(f"Film Name: {movie[0]}, Runtime: {movie[1]}")

# Query 4: Get a list of film names and directors grouped by director
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
films_directors = cursor.fetchall()
print("\n-- DISPLAYING Director RECORDS in Order --")
for film_director in films_directors:
    print(f"Film Name: {film_director[0]}, Director: {film_director[1]}")

# Close the database connection
db_connection.close()
