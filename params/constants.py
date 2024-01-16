from enum import Enum

class DatasetName(Enum):
    ml_genome_scores = "ml_genome_scores"
    ml_genome_tags = "ml_genome_tags"
    ml_links = "ml_links"
    ml_movies = "ml_movies"
    ml_ratings = "ml_ratings"
    ml_tags = "ml_tags"
    tmbd_movies = "tmbd_movies"
    tmbd_credits = "tmbd_credits"
    
    
DATASET_PATHS = {
    DatasetName.ml_genome_scores: "/Users/kevingregory/Desktop/programs/kaggle_data/movie_lens/genome-tags.csv",
    DatasetName.ml_genome_tags: "/Users/kevingregory/Desktop/programs/kaggle_data/movie_lens/genome-tags.csv",
    DatasetName.ml_links: "/Users/kevingregory/Desktop/programs/kaggle_data/movie_lens/links.csv",
    DatasetName.ml_movies: "/Users/kevingregory/Desktop/programs/kaggle_data/movie_lens/movies.csv",
    DatasetName.ml_ratings: "/Users/kevingregory/Desktop/programs/kaggle_data/movie_lens/ratings.csv",
    DatasetName.ml_tags: "/Users/kevingregory/Desktop/programs/kaggle_data/movie_lens/tags.csv",
    DatasetName.tmbd_movies: "/Users/kevingregory/Desktop/programs/kaggle_data/tmdb/tmdb_5000_movies.csv",
    DatasetName.tmbd_credits: "/Users/kevingregory/Desktop/programs/kaggle_data/tmdb/tmdb_5000_credits.csv"
}