import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load cleaned reviews
df = pd.read_csv('reviews_clean.csv')

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_label(score):
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

df['sentiment_score'] = df['review'].apply(lambda x: analyzer.polarity_scores(str(x))['compound'])
df['sentiment_label'] = df['sentiment_score'].apply(get_sentiment_label)

df.to_csv('reviews_with_sentiment.csv', index=False)
print("Sentiment analysis completed! Results saved to reviews_with_sentiment.csv.")