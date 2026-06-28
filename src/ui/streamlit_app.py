import streamlit as st

from src.ui.styles import load_css

from src.ui.components import (
    page_header,
    search_panel,
    answer_card,
    source_card,
    metric_cards,
)


def main():

    st.set_page_config(
        page_title="Enterprise RAG",
        layout="wide",
    )

    load_css()

    page_header()

    # -------------------------
    # Search Section
    # -------------------------

    question, search = search_panel()

    # -------------------------
    # Response + Sources
    # -------------------------

    left, right = st.columns([2, 1])

    with left:

        answer_card("")

    with right:

        source_card()

    # -------------------------
    # Metrics
    # -------------------------

    metric_cards()