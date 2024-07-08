# Brooks Roberts
# 7/7/24
# 8 Assignment

import mysql.connector

# Connect to the movies database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="movies_user",
    password="popcorn",
    database="movies"
)

# Create a cursor object to execute SQL queries
cursor = db_connection.cursor()

def show_films(cursor, title):
   # method to execute an inner join on all tables,
   #    iterate over the dataset and output the results to the terminal window.

   # inner join query

   query = """
        SELECT film_name AS Name, film_director AS Director,
               genre_name AS Genre, studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """
   cursor.execute(query)
   # get the results from the cursor object
   films = cursor.fetchall()
    
   print(f"\n-- {title} --")

   # Iterate over the data set and display results
   for film in films:
       name, director, genre, studio = film
       print(f"Film Name: {name}, Director: {director}, Genre: {genre}, Studio: {studio}")

# Display film information before inserting
show_films(cursor, "DISPLAYING FILMS")

# Insert a new record for the film "Avatar"
insert_query = """
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
cursor.execute(insert_query, ("Avatar", "2009", "162", "James Cameron", 1, 2))

# Display film information after inserting
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Update the genre of "Alien" to "Horror"
update_query = """
    UPDATE film
    SET genre_id = 1
    WHERE film_name = 'Alien'
"""
cursor.execute(update_query)

# Display film information after the update
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

# Delete the movie "Gladiator"
delete_query = """
    DELETE FROM film
    WHERE film_name = 'Gladiator'
"""
cursor.execute(delete_query)

# Display film information after the deletion
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")
