import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

def safe_print(text):
    print(text.encode('ascii', errors='ignore').decode())

# Load the processed reviews with sentiment
df = pd.read_csv('reviews_with_sentiment.csv')
# Count of each sentiment per bank
sentiment_counts = df.groupby(['bank', 'sentiment_label']).size().unstack(fill_value=0)
print(sentiment_counts)

avg_rating = df.groupby('bank')['rating'].mean()
print(avg_rating)

for bank in df['bank'].unique():
    # Top words
    reviews = df[df['bank'] == bank]['review'].str.cat(sep=' ').lower().split()
    common_words = Counter(reviews).most_common(10)
    print(f"Top words for {bank}: {common_words}")

    # Sample positive and negative reviews
    pos_reviews = df[(df['bank'] == bank) & (df['sentiment_label'] == 'positive')]['review']
    neg_reviews = df[(df['bank'] == bank) & (df['sentiment_label'] == 'negative')]['review']
    if not pos_reviews.empty:
        safe_print(f"{bank} - Sample Positive Review: {pos_reviews.iloc[0]}")
    else:
        print(f"{bank} - No positive reviews found.")
    if not neg_reviews.empty:
        safe_print(f"{bank} - Sample Negative Review: {neg_reviews.iloc[0]}")
    else:
        print(f"{bank} - No negative reviews found.")

    # Generate Word Cloud
    text = df[df['bank'] == bank]['review'].str.cat(sep=' ')
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud for {bank}')
    plt.savefig(f'wordcloud_{bank}.png')
    plt.show()

# Sentiment distribution per bank (stacked bar chart)
sentiment_counts.plot(kind='bar', stacked=True)
plt.title('Sentiment Distribution per Bank')
plt.xlabel('Bank')
plt.ylabel('Number of Reviews')
plt.legend(title='Sentiment')
plt.tight_layout()
plt.savefig('sentiment_distribution.png')
plt.show()

# Bank-specific insights
bank_insights = {
    "CBE": {
        "Drivers": ["fast", "easy", "reliable"],
        "Pain Points": ["occasional crashes", "login issues"],
        "Recommendation": "Focus on fixing crash bugs and improving login stability."
    },
    "BOA": {
        "Drivers": ["simple interface"],
        "Pain Points": ["frequent errors", "slow performance"],
        "Recommendation": "Prioritize performance optimization and error handling."
    },
    "Dashen": {
        "Drivers": ["good service", "fast transactions"],
        "Pain Points": ["update issues", "support delays"],
        "Recommendation": "Improve update process and customer support response time."
    }
}

for bank, insights in bank_insights.items():
    print(f"\n{bank} Insights:")
    for key, value in insights.items():
        print(f"- {key}: {', '.join(value) if isinstance(value, list) else value}")