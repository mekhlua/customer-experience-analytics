# customer-experience-analytics
 Google Play Reviews Analysis for Ethiopian Fintech Apps (CBE, BOA, Dashen)
Customer Experience Analytics for Fintech Apps
Overview
This project analyzes Google Play Store reviews for the mobile banking apps of three major Ethiopian banks:

Commercial Bank of Ethiopia (CBE)
Bank of Abyssinia (BOA)
Dashen Bank
The goal is to uncover drivers of customer satisfaction and pain points, and to provide actionable recommendations for app improvement.

Project Structure
scrape_reviews.py – Scrapes reviews from Google Play Store and preprocesses them.
analyze_sentiment.py – Performs sentiment analysis on reviews using VADER.
thematic_analysis.py – Extracts keywords and themes from reviews.
insert_to_oracle.py – Inserts cleaned and analyzed data into Oracle XE database.
analyze_insights.py – Analyzes, visualizes, and summarizes insights and recommendations.
reviews_clean.csv – Cleaned review data.
reviews_with_sentiment.csv – Review data with sentiment labels.
wordcloud_*.png, sentiment_distribution.png – Visualizations.
How to Run
Install requirements:
pip install -r requirements.txt

Scrape and preprocess reviews:
python scrape_reviews.py

Run sentiment analysis:
python analyze_sentiment.py

Run thematic analysis:
python thematic_analysis.py

Insert data into Oracle XE:
Ensure Oracle XE is running and tables are created in XEPDB1.
Update credentials in insert_to_oracle.py if needed.
python insert_to_oracle.py

Analyze and visualize insights:
python analyze_insights.py

Key Findings
CBE: Fast, easy, reliable; occasional crashes and login issues.
BOA: Simple interface; frequent errors and slow performance.
Dashen: Good service, fast transactions; update issues and support delays.
See the analyze_insights.py output and generated plots for more details.

Recommendations
CBE: Focus on fixing crash bugs and improving login stability.
BOA: Prioritize performance optimization and error handling.
Dashen: Improve update process and customer support response time.
Requirements
Python 3.x
pandas, matplotlib, wordcloud, vaderSentiment, oracledb, scikit-learn
Oracle XE (for database storage)