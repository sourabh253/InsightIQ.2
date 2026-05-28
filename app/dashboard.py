import streamlit as st
import plotly.express as px

from utils.loader import load_dataset
from utils.detector import detect_column_types
from utils.cleaner import clean_dataset

from utils.visualizer import (
    generate_numeric_charts,
    generate_categorical_charts
)

from utils.analytics_engine import (
    generate_numeric_summary,
    generate_correlation
)

from utils.ml_engine import (
    perform_clustering
)

from utils.nlp_engine import (
    detect_review_column,
    analyze_sentiment,
    generate_sentiment_summary
)

from utils.insights import (
    generate_ai_insights
)


# PAGE CONFIG

st.set_page_config(
    page_title="InsightIQ.2",
    layout="wide"
)

# ========================================
# TITLE
# ========================================

st.title(
    "InsightIQ.2 — Analytics Engine"
)

st.markdown("""
Upload any CSV dataset and let AI automatically generate analytics, visualizations, machine learning intelligence, NLP insights, and AI-powered business intelligence.
""")

# ========================================
# SIDEBAR
# ========================================


id="j5uwr2"
st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div style='text-align: center; margin-top: 20px;'>
        <a href="https://www.linkedin.com/in/sourabh-jangid-668745341"
           target="_blank"
           style="
               text-decoration: none;
               font-size: 22px;
               font-weight: bold;
               color: #4da6ff;
           ">
           Sourabh Jangid
        </a>
    </div>
    """,
    unsafe_allow_html=True
)



st.sidebar.title(
    "InsightIQ.2"
)

st.sidebar.markdown("""
Universal AI Analytics Platform
""")

st.sidebar.info(
    "Recommended Dataset Size: Under 10,000 Rows"
)

# ========================================
# FEATURE TOGGLES
# ========================================

st.sidebar.subheader(
    "Feature Controls"
)

run_visuals = st.sidebar.checkbox(
    "Enable Visualizations",
    value=True
)

run_ml = st.sidebar.checkbox(
    "Enable ML Analysis"
)

run_nlp = st.sidebar.checkbox(
    "Enable NLP Analysis"
)

run_ai = st.sidebar.checkbox(
    "Enable AI Insights",
    value=True
)

# ========================================
# FILE UPLOADER
# ========================================

uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=['csv']
)

# ========================================
# RUN BUTTON
# ========================================

run_analysis = st.button(
    "Run AI Analysis"
)

# ========================================
# MAIN PROCESS
# ========================================

if uploaded_file is not None and run_analysis:

    try:

        # ====================================
        # LOAD DATASET
        # ====================================

        with st.spinner(
            "Loading Dataset..."
        ):

            df = load_dataset(
                uploaded_file
            )

        st.success(
            "Dataset Loaded Successfully"
        )

        # ====================================
        # CLEAN DATASET
        # ====================================

        df, missing_values = clean_dataset(
            df
        )

        # ====================================
        # DATASET SIZE LIMIT
        # ====================================

        if len(df) > 10000:

            st.error(
                """
                Bro limit your dataset 😎

                InsightIQ.2 currently supports datasets up to 10,000 rows for smooth AI analytics and better performance.
                """
            )

            st.stop()

        # ====================================
        # DATASET PREVIEW
        # ====================================

        st.subheader(
            "Dataset Preview"
        )

        st.dataframe(
            df.head()
        )

        # ====================================
        # DATASET SHAPE
        # ====================================

        st.subheader(
            "Dataset Shape"
        )

        col1, col2 = st.columns(2)

        col1.metric(
            "Rows",
            df.shape[0]
        )

        col2.metric(
            "Columns",
            df.shape[1]
        )

        # ====================================
        # COLUMN DETECTION
        # ====================================

        st.subheader(
            "Detected Column Types"
        )

        column_info = detect_column_types(
            df
        )

        numeric_columns = column_info[
            'numeric'
        ]

        categorical_columns = column_info[
            'categorical'
        ]

        datetime_columns = column_info[
            'datetime'
        ]

        text_columns = column_info[
            'text'
        ]

        col1, col2, col3, col4 = st.columns(4)

        col1.write(
            "Numeric Columns"
        )

        col1.write(
            numeric_columns
        )

        col2.write(
            "Categorical Columns"
        )

        col2.write(
            categorical_columns
        )

        col3.write(
            "Datetime Columns"
        )

        col3.write(
            datetime_columns
        )

        col4.write(
            "Text Columns"
        )

        col4.write(
            text_columns
        )

        # ====================================
        # MISSING VALUES
        # ====================================

        st.subheader(
            "Missing Values"
        )

        st.write(
            missing_values
        )

        # ====================================
        # DYNAMIC ANALYTICS
        # ====================================

        if run_visuals:

            st.header(
                "Dynamic Analytics"
            )

            # ================================
            # NUMERIC ANALYSIS
            # ================================

            if len(numeric_columns) > 0:

                st.subheader(
                    "Numeric Analysis"
                )

                limited_numeric = (
                    numeric_columns[:3]
                )

                numeric_charts = (
                    generate_numeric_charts(
                        df,
                        limited_numeric
                    )
                )

                for fig in numeric_charts:

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

            # ================================
            # CATEGORICAL ANALYSIS
            # ================================

            if len(categorical_columns) > 0:

                st.subheader(
                    "Categorical Analysis"
                )

                limited_categorical = (
                    categorical_columns[:3]
                )

                categorical_charts = (
                    generate_categorical_charts(
                        df,
                        limited_categorical
                    )
                )

                for fig in categorical_charts:

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

        # ====================================
        # AUTOMATED ANALYTICS ENGINE
        # ====================================

        st.header(
            "Automated Analytics Engine"
        )

        if len(numeric_columns) > 0:

            numeric_summary = (
                generate_numeric_summary(
                    df,
                    numeric_columns
                )
            )

            st.subheader(
                "Numeric Statistics"
            )

            st.json(
                numeric_summary
            )

            # ================================
            # CORRELATION MATRIX
            # ================================

            correlation = (
                generate_correlation(df)
            )

            if not correlation.empty:

                st.subheader(
                    "Correlation Matrix"
                )

                fig_corr = px.imshow(
                    correlation,
                    text_auto=True,
                    title="Feature Correlation Matrix"
                )

                st.plotly_chart(
                    fig_corr,
                    use_container_width=True
                )

        # ====================================
        # MACHINE LEARNING ENGINE
        # ====================================

        if run_ml:

            st.header(
                "ML Intelligence Layer"
            )

            with st.spinner(
                "Running Machine Learning..."
            ):

                cluster_df = (
                    perform_clustering(df)
                )

            if cluster_df is not None:

                st.success(
                    "Dynamic Clustering Enabled"
                )

                cluster_columns = (
                    cluster_df.columns[:2]
                )

                fig_cluster = px.scatter(
                    cluster_df,
                    x=cluster_columns[0],
                    y=cluster_columns[1],
                    color='Cluster',
                    title='Dynamic Clustering'
                )

                st.plotly_chart(
                    fig_cluster,
                    use_container_width=True
                )

            else:

                st.warning(
                    "Not enough numeric features for clustering."
                )

        # ====================================
        # NLP ENGINE
        # ====================================

        if run_nlp:

            st.header(
                "NLP Intelligence Layer"
            )

            if len(df) > 3000:

                st.warning(
                    "NLP disabled for datasets above 3000 rows."
                )

            else:

                review_column = (
                    detect_review_column(df)
                )

                if review_column is not None:

                    st.success(
                        f"Detected Review Column: {review_column}"
                    )

                    with st.spinner(
                        "Running NLP Analysis..."
                    ):

                        sentiment_df = (
                            analyze_sentiment(
                                df,
                                review_column
                            )
                        )

                    sentiment_summary = (
                        generate_sentiment_summary(
                            sentiment_df
                        )
                    )

                    sentiment_chart = (
                        px.pie(
                            names=list(
                                sentiment_summary.keys()
                            ),
                            values=list(
                                sentiment_summary.values()
                            ),
                            title='Sentiment Analysis'
                        )
                    )

                    st.plotly_chart(
                        sentiment_chart,
                        use_container_width=True
                    )

                else:

                    st.info(
                        "No review column detected."
                    )

        # ====================================
        # AI INSIGHTS ENGINE
        # ====================================

        if run_ai:

            st.header(
                "AI Insights Engine"
            )

            insights = (
                generate_ai_insights(df)
            )

            for insight in insights:

                st.success(
                    insight
                )

        # ====================================
        # COMPLETION MESSAGE
        # ====================================

        st.success(
            "AI Analysis Completed Successfully 🚀"
        )

    except Exception as e:

        st.error(
            f"Error Processing Dataset: {e}"
        )

# ========================================
# EMPTY STATE
# ========================================

else:

    st.info(
        "Upload any CSV dataset and click 'Run AI Analysis' to begin."
    )