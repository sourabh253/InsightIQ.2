import pandas as pd


# =========================================
# DETECT COLUMN TYPES
# =========================================

def detect_column_types(df):

    numeric_columns = []

    categorical_columns = []

    datetime_columns = []

    text_columns = []

    id_columns = []

    boolean_columns = []

    for column in df.columns:

        dtype = str(df[column].dtype)

        # =====================================
        # NUMERIC DETECTION
        # =====================================

        if pd.api.types.is_numeric_dtype(
            df[column]
        ):

            numeric_columns.append(column)

        # =====================================
        # BOOLEAN DETECTION
        # =====================================

        elif pd.api.types.is_bool_dtype(
            df[column]
        ):

            boolean_columns.append(column)

        # =====================================
        # DATETIME DETECTION
        # =====================================

        else:

            try:

                converted = pd.to_datetime(
                    df[column],
                    errors='raise'
                )

                datetime_columns.append(
                    column
                )

                continue

            except Exception:

                pass

        # =====================================
        # ID COLUMN DETECTION
        # =====================================

        unique_ratio = (
            df[column].nunique()
            / len(df)
        )

        if unique_ratio > 0.9:

            id_columns.append(column)

        # =====================================
        # TEXT COLUMN DETECTION
        # =====================================

        avg_length = (
            df[column]
            .astype(str)
            .str.len()
            .mean()
        )

        if avg_length > 30:

            text_columns.append(column)

        else:

            categorical_columns.append(
                column
            )

    return {

        "numeric": numeric_columns,

        "categorical": categorical_columns,

        "datetime": datetime_columns,

        "text": text_columns,

        "id": id_columns,

        "boolean": boolean_columns
    }
