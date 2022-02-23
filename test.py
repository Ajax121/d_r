"""test"""
import pandas as pd
from recommender import random_recomm
def test_recomm():
    """test"""
    movies = pd.read_csv('data/movies.csv')
    recom = random_recomm()
    assert len(recom)==10