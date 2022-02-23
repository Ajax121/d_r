"""test"""
import pandas as pd
from recommender import random_recomm
def test_recomm():
    """test"""
    recom = random_recomm()
    assert len(recom)==10
