from lib.film import Film

class FilmRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all films
    def all(self):
        rows = self._connection.execute('SELECT * from films')
        films = []
        for row in rows:
            item = Film(row["id"], row["title"], row["release_year"])
            films.append(item)
        return films

"""     # Find a single film by their id
    def find(self, film_id):
        rows = self._connection.execute(
            'SELECT * from films WHERE id = %s', [film_id])
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, artist):
        self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [
                                 artist.name, artist.genre])
        return None

    # Delete an artist by their id
    def delete(self, artist_id):
        self._connection.execute(
            'DELETE FROM artists WHERE id = %s', [artist_id])
        return None """