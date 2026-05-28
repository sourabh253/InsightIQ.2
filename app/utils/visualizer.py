import plotly.express as px


# ============================================
# NUMERIC VISUALIZATION
# ============================================

def generate_numeric_charts(
    df,
    numeric_columns,
    max_columns=5
):

    charts = []

    # Limit excessive charts
    selected_columns = numeric_columns[
        :max_columns
    ]

    for column in selected_columns:

        try:

            # ===============================
            # HISTOGRAM
            # ===============================

            fig_hist = px.histogram(
                df,
                x=column,
                title=f"Distribution of {column}",
                marginal="box"
            )

            charts.append(fig_hist)

            # ===============================
            # BOXPLOT
            # ===============================

            fig_box = px.box(
                df,
                y=column,
                title=f"Boxplot of {column}"
            )

            charts.append(fig_box)

        except Exception:

            continue

    return charts


# ============================================
# CATEGORICAL VISUALIZATION
# ============================================

def generate_categorical_charts(
    df,
    categorical_columns,
    max_columns=5
):

    charts = []

    selected_columns = categorical_columns[
        :max_columns
    ]

    for column in selected_columns:

        try:

            # Avoid huge category explosion
            unique_count = (
                df[column].nunique()
            )

            if unique_count > 30:

                continue

            top_values = (
                df[column]
                .value_counts()
                .head(10)
                .reset_index()
            )

            top_values.columns = [
                column,
                'Count'
            ]

            fig = px.bar(
                top_values,
                x=column,
                y='Count',
                title=f"Top Categories in {column}"
            )

            charts.append(fig)

        except Exception:

            continue

    return charts


# ============================================
# DATETIME VISUALIZATION
# ============================================

def generate_datetime_charts(
    df,
    datetime_columns,
    max_columns=3
):

    charts = []

    selected_columns = datetime_columns[
        :max_columns
    ]

    for column in selected_columns:

        try:

            temp_df = df.copy()

            temp_df[column] = (
                temp_df[column]
                .astype(str)
            )

            temp_df[column] = px.data.tips()

            date_counts = (
                df[column]
                .value_counts()
                .reset_index()
            )

            date_counts.columns = [
                column,
                'Count'
            ]

            fig = px.line(
                date_counts,
                x=column,
                y='Count',
                title=f"Trend Analysis of {column}"
            )

            charts.append(fig)

        except Exception:

            continue

    return charts
