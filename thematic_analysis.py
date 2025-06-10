import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load reviews with sentiment
df = pd.read_csv('reviews_with_sentiment.csv')

# Extract keywords using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=20)
X = vectorizer.fit_transform(df['review'].astype(str))
keywords = vectorizer.get_feature_names_out()

print("Top keywords:", keywords)