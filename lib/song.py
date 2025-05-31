class Song:
    count = 0                    # Total songs created
    genres = set()               # All genres encountered
    artists = set()              # All artists encountered
    genre_count = {}             # Counts per genre
    artist_count = {}            # Counts per artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment total song count
        Song.count += 1

        # Add genre and artist to sets
        Song.genres.add(genre)
        Song.artists.add(artist)

        # Increment genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Increment artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
