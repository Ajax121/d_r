import pandas as pd
def random_recomm(k=10):
	"""ads"""
	df = pd.read_csv('data/movies.csv')
	return df['title'].sample(k)
print(random_recomm())
