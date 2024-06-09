from enum import Enum

base_path = "/Users/kevingregory/Desktop/programs/Movie_Recommendation/data/datasets"

class DATASETS(Enum):
    ARTIST_ATTRIBUTES = "artist_attributes"
    ARTIST_TO_IMDB = "artist_to_imdb"
    IMDB_ATTRIBUTES = "imdb_attributes"
    IMDB_GENRES = "imdb_genres"
    MOVIE_GENRES = "movie_genres"
    MOVIE_TITLE_KEYWORDS = "movie_title_keywords"
    MOVIES = "movies"
    TMDB_ATTRIBUTES = "tmdb_attributes"
    TMDB_GENRES = "tmdb_genres"
    TMDB_KEYWORDS = "tmdb_keywords"
    TMDB_OVERVIEW_KEYWORDS = "tmdb_overview_keywords"
    GENOME_TAGS = "genome_tags"
    LINKS = "links"
    TAGS = "tags"
    TMDB_CREDITS = "tmdb_5000_credits"
    TMDB_MOVIES = "tmdb_5000_movies"