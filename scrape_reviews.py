from google_play_scraper import Sort, reviews
import pandas as pd
# Define the banks and their app IDs
apps = {
    "CBE": 'com.combanketh.mobilebanking' , 
    "BOA": 'com.boa.boaMobileBanking',  
    "Dashen":'com.dashen.dashensuperapp'  
}

def scrape_reviews(app_id):
    result, _ = reviews(
        app_id,
        lang='en',
        country='ET',
        sort=Sort.MOST_RELEVANT,
        count=400  # Number of reviews to scrape
    )
    return result

all_reviews = []

for bank, app_id in apps.items():
    bank_reviews = scrape_reviews(app_id)
    for review in bank_reviews:
        review['bank'] = bank
        all_reviews.append(review)

# Convert to DataFrame
df = pd.DataFrame(all_reviews)

# Preprocessing
df = df.drop_duplicates(subset=['content', 'userName'])  # Remove duplicates
df = df.dropna(subset=['content', 'score', 'at'])        # Remove rows with missing essential data

# Normalize date
df['date'] = pd.to_datetime(df['at']).dt.strftime('%Y-%m-%d')

# Select and rename columns
df_clean = df.rename(columns={
    'content': 'review',
    'score': 'rating',
    'date': 'date',
    'bank': 'bank'
})
df_clean['source'] = 'Google Play'
df_clean = df_clean[['review', 'rating', 'date', 'bank', 'source']]

# Save cleaned data
df_clean.to_csv('reviews_clean.csv', index=False)
print("Preprocessing completed! Cleaned reviews saved to reviews_clean.csv.")