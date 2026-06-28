import streamlit as st


def page_header():

    st.markdown(
        """
        <div class="hero-card">

            <div class="hero-left">

                <div class="hero-title">
                    Enterprise RAG Knowledge Assistant
                </div>

                <div class="hero-subtitle">
                    AI-powered Enterprise Knowledge Search Platform
                </div>

            </div>

            <div class="hero-right">

                <div class="status-badge">
                    Backend Connected
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

def search_panel():
    """
    Enterprise Search Panel
    """

    st.markdown(
        """
        <div class="search-card">

            <div class="search-title">
                Ask Your Enterprise Knowledge Base
            </div>

            <div class="search-subtitle">
                Search across HR policies, employee handbook, IT security,
                training guides and other enterprise documents.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    question = st.text_area(
        "",
        placeholder="Example: What is the leave approval process?",
        height=120,
        label_visibility="collapsed",
    )

    col1, col2, col3 = st.columns([2, 1, 2])

    with col2:
        search = st.button(
            "Search Knowledge",
            use_container_width=True,
        )

    return question, search

def answer_card(answer: str):
    """
    Display the generated AI response.
    """

    if not answer:
        answer = "The generated response will appear here."

    st.markdown(
        f"""
        <div class="answer-card">

            <div class="answer-title">
                Generated Response
            </div>

            <div class="answer-body">
                {answer}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )