import pandas as pd
import oracledb

# Load your data
df = pd.read_csv('reviews_with_sentiment.csv')

# Connect to Oracle
connection = oracledb.connect(
    user="SYSTEM",
    password="selah24434",
    dsn="localhost/XEPDB1"  # Adjust DSN as needed
)
cursor = connection.cursor()

# Insert banks and get their IDs
banks = df['bank'].unique()
bank_id_map = {}
for bank in banks:
    cursor.execute("INSERT INTO BANKS (name) VALUES (:1)", [bank])
    cursor.execute("SELECT id FROM BANKS WHERE name = :1", [bank])
    bank_id_map[bank] = cursor.fetchone()[0]

# Insert reviews
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO REVIEWS (review, rating, review_date, bank_id, source, sentiment_label, sentiment_score)
        VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6, :7)
    """, [
        row['review'],
        int(row['rating']),
        row['date'],
        bank_id_map[row['bank']],
        row['source'],
        row['sentiment_label'],
        float(row['sentiment_score'])
    ])

connection.commit()
cursor.close()
connection.close()
print("Data inserted into Oracle database.")