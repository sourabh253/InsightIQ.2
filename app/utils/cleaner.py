import pandas as pd


# =========================================
# CLEAN DATASET
# =========================================

def clean_dataset(df):

    temp_df = df.copy()

    # =====================================
    # REMOVE DUPLICATES
    # =====================================

    temp_df = temp_df.drop_duplicates()

    # =====================================
    # CLEAN COLUMN NAMES
    # =====================================

    temp_df.columns = [

        col.strip().replace(
            " ",
            "_"
        )

        for col in temp_df.columns
    ]

    # =====================================
    # HANDLE MISSING VALUES
    # =====================================

    missing_values = (
        temp_df.isnull().sum()
    )

    # Numeric columns
    numeric_columns = temp_df.select_dtypes(
        include=['int64', 'float64']
    ).columns

    for column in numeric_columns:

        temp_df[column] = (
            temp_df[column]
            .fillna(
                temp_df[column].median()
            )
        )

    # Object columns
    object_columns = temp_df.select_dtypes(
        include=['object']
    ).columns

    for column in object_columns:

        temp_df[column] = (
            temp_df[column]
            .astype(str)
            .str.strip()
        )

        temp_df[column] = (
            temp_df[column]
            .replace(
                ['nan', 'None', ''],
                'Unknown'
            )
        )

    # =====================================
    # REMOVE FULLY EMPTY ROWS
    # =====================================

    temp_df = temp_df.dropna(
        how='all'
    )

    return temp_df, missing_values
