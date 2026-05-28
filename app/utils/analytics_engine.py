import pandas as pd


# =========================================
# NUMERIC SUMMARY
# =========================================

def generate_numeric_summary(
    df,
    numeric_columns
):

    summary = {}

    for column in numeric_columns:

        try:

            summary[column] = {
                "mean": round(df[column].mean(), 2),
                "median": round(df[column].median(), 2),
                "min": round(df[column].min(), 2),
                "max": round(df[column].max(), 2),
                "std": round(df[column].std(), 2)
            }

        except Exception:

            continue

    return summary


# =========================================
# CORRELATION MATRIX
# =========================================

def generate_correlation(df):

    numeric_df = df.select_dtypes(
        include=['int64', 'float64']
    )

    # Avoid empty correlation issues
    if numeric_df.shape[1] < 2:

        return pd.DataFrame()

    correlation = numeric_df.corr()

    return correlation
