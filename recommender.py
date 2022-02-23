"""sdsd"""
import pandas as pd
def random_recomm(k=10):
    """
    ads
    """
    d_f = pd.read_csv('data/movies.csv')
    return d_f['title'].sample(k)
print(random_recomm())
