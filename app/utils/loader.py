import streamlit as st
import pandas as pd

@st.cache_data
# =========================================
# LOAD DATASET
# =========================================

def load_dataset(file):

    try:

        # =====================================
        # PRIMARY LOAD ATTEMPT
        # =====================================

        df = pd.read_csv(
            file,
            encoding='latin1'
        )

    except Exception:

        try:

            # =================================
            # SECONDARY UTF-8 ATTEMPT
            # =================================

            df = pd.read_csv(
                file,
                encoding='utf-8'
            )

        except Exception as e:

            raise Exception(
                f"Unable to load dataset: {e}"
            )

    # =====================================
    # EMPTY DATASET CHECK
    # =====================================

    if df.empty:

        raise Exception(
            "Uploaded dataset is empty."
        )

    # =====================================
    # REMOVE UNNAMED COLUMNS
    # =====================================

    df = df.loc[
        :,
        ~df.columns.str.contains(
            '^Unnamed',
            case=False
        )
    ]

    return df
