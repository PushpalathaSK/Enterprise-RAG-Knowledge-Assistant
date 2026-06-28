import streamlit as st

from src.ui.styles import load_css
from src.ui.components import page_header

def main():

    st.set_page_config(
        page_title="Enterprise RAG",
        layout="wide",
    )

    load_css()


    page_header()

    left, right = st.columns([2, 1])

    with left:

        from src.ui.components import (
    page_header,
    search_panel,
    answer_card,
)
        question, search = search_panel()
        answer_card("")
    with right:

        st.markdown("### Supporting Documents")

        st.info("Retrieved documents will appear here.")

        st.markdown("---")

        st.markdown("### System Information")

        st.info(
            """
Documents : 10

Chunks : 10

Embedding : MiniLM

LLM : Gemini
            """
        )