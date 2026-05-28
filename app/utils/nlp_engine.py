from textblob import TextBlob

import pandas as pd


# =========================================
# REVIEW COLUMN DETECTION
# =========================================

def detect_review_column(df):

    possible_columns = [

        'Review',
        'Reviews',
        'Feedback',
        'Comment',
        'Comments',
        'Text',
        'ReviewText',
        'CustomerReview',
        'Description'

    ]

    for column in df.columns:

        if column.lower() in [
            col.lower()
            for col in possible_columns
        ]:

            return column

    return None


# =========================================
# CLEAN TEXT
# =========================================

def clean_text(text):

    text = str(text)

    text = text.strip()

    return text


# =========================================
# SENTIMENT ANALYSIS
# =========================================

def analyze_sentiment(
    df,
    review_column
):

    temp_df = df.copy()

    temp_df[review_column] = (
        temp_df[review_column]
        .astype(str)
        .apply(clean_text)
    )

    def get_sentiment(text):

        polarity = TextBlob(
            text
        ).sentiment.polarity

        if polarity > 0:

            return "Positive"

        elif polarity < 0:

            return "Negative"

        else:

            return "Neutral"

    temp_df['Sentiment'] = (
        temp_df[review_column]
        .apply(get_sentiment)
    )

    return temp_df


# =========================================
# SENTIMENT SUMMARY
# =========================================

def generate_sentiment_summary(df):

    if 'Sentiment' not in df.columns:

        return None

    sentiment_counts = (
        df['Sentiment']
        .value_counts()
        .to_dict()
    )

    return sentiment_counts
