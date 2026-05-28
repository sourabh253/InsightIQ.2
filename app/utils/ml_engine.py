from sklearn.cluster import KMeans

from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import IsolationForest

import pandas as pd


# =========================================
# PERFORM CLUSTERING
# =========================================

def perform_clustering(
    df,
    max_clusters=3
):

    numeric_df = df.select_dtypes(
        include=['int64', 'float64']
    )

    # =====================================
    # REMOVE MISSING VALUES
    # =====================================

    numeric_df = numeric_df.dropna()

    # =====================================
    # NEED AT LEAST 2 FEATURES
    # =====================================

    if numeric_df.shape[1] < 2:

        return None

    # =====================================
    # LIMIT FEATURES
    # =====================================

    numeric_df = numeric_df.iloc[:, :5]

    # =====================================
    # STANDARDIZATION
    # =====================================

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(
        numeric_df
    )

    # =====================================
    # CLUSTER MODEL
    # =====================================

    model = KMeans(
        n_clusters=max_clusters,
        random_state=42,
        n_init=10
    )

    clusters = model.fit_predict(
        scaled_data
    )

    numeric_df = numeric_df.copy()

    numeric_df['Cluster'] = clusters

    return numeric_df


# =========================================
# ANOMALY DETECTION
# =========================================

def detect_anomalies(df):

    numeric_df = df.select_dtypes(
        include=['int64', 'float64']
    )

    numeric_df = numeric_df.dropna()

    # Need enough features
    if numeric_df.shape[1] < 2:

        return None

    # Limit dimensions
    numeric_df = numeric_df.iloc[:, :5]

    model = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    anomalies = model.fit_predict(
        numeric_df
    )

    numeric_df = numeric_df.copy()

    numeric_df['Anomaly'] = anomalies

    return numeric_df
