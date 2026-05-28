import pandas as pd


# =========================================
# GENERATE AI INSIGHTS
# =========================================

def generate_ai_insights(df):

    insights = []

    rows, cols = df.shape

    # =====================================
    # DATASET SIZE
    # =====================================

    insights.append(
        f"Dataset contains {rows} rows and {cols} columns."
    )

    # =====================================
    # MISSING VALUES
    # =====================================

    missing_values = (
        df.isnull().sum().sum()
    )

    insights.append(
        f"Dataset contains {missing_values} missing values."
    )

    # =====================================
    # NUMERIC INSIGHTS
    # =====================================

    numeric_columns = df.select_dtypes(
        include=['int64', 'float64']
    ).columns

    if len(numeric_columns) > 0:

        variance_series = (
            df[numeric_columns]
            .var()
            .sort_values(
                ascending=False
            )
        )

        highest_variance = (
            variance_series.index[0]
        )

        insights.append(
            f"'{highest_variance}' shows the highest variability in the dataset."
        )

        highest_mean = (
            df[numeric_columns]
            .mean()
            .sort_values(
                ascending=False
            )
            .index[0]
        )

        insights.append(
            f"'{highest_mean}' has the highest average values among numeric features."
        )

    # =====================================
    # CATEGORICAL INSIGHTS
    # =====================================

    categorical_columns = df.select_dtypes(
        include=['object']
    ).columns

    if len(categorical_columns) > 0:

        for column in categorical_columns[:3]:

            try:

                top_category = (
                    df[column]
                    .value_counts()
                    .index[0]
                )

                insights.append(
                    f"Most common value in '{column}' is '{top_category}'."
                )

            except Exception:

                continue

    # =====================================
    # DUPLICATE ANALYSIS
    # =====================================

    duplicates = (
        df.duplicated().sum()
    )

    insights.append(
        f"Dataset contains {duplicates} duplicate rows."
    )

    return insights