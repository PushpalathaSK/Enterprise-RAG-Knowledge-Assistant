print("Components loaded from:", __file__)

import streamlit as st


# ==========================================
# Header
# ==========================================

def page_header():

    st.html("""
    <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        background:white;
        padding:25px;
        border-radius:12px;
        border:1px solid #E5E7EB;
        margin-bottom:25px;
        box-shadow:0 4px 12px rgba(0,0,0,0.05);
    ">

        <div>

            <h1 style="
                margin:0;
                color:#111827;
                font-size:42px;
                font-weight:700;
            ">
                Enterprise RAG Knowledge Assistant
            </h1>

            <p style="
                margin-top:10px;
                color:#6B7280;
                font-size:17px;
            ">
                AI-powered Enterprise Knowledge Search Platform
            </p>

        </div>

        <div style="
            background:#DCFCE7;
            color:#15803D;
            padding:12px 20px;
            border-radius:25px;
            font-weight:bold;
        ">
            Backend Connected
        </div>

    </div>
    """)


# ==========================================
# Search Panel
# ==========================================

def search_panel():

    st.html("""
    <div class="search-card">

        <div class="search-title">
            Ask Your Enterprise Knowledge Base
        </div>

        <div class="search-subtitle">
            Search across HR Policies, Employee Handbook,
            IT Security, Training Guides and Enterprise Documents.
        </div>

    </div>
    """)

    question = st.text_area(
        "Question",
        placeholder="Example: What is the leave approval process?",
        height=120,
        label_visibility="collapsed",
    )

    left, center, right = st.columns([2,1,2])

    with center:

        search = st.button(
            "Search Knowledge",
            use_container_width=True,
        )

    return question, search


# ==========================================
# Answer Card
# ==========================================

def answer_card(answer):

    if not answer:
        answer = "The generated response will appear here."

    st.html(f"""
    <div class="answer-card">

        <div class="answer-title">
            Generated Response
        </div>

        <div class="answer-body">
            {answer}
        </div>

    </div>
    """)


# ==========================================
# Source Card
# ==========================================

def source_card(documents=None):

    html = """
    <div class="answer-card">

        <div class="answer-title">
            Supporting Documents
        </div>
    """

    if not documents:

        html += """
        <div class="source-item">
            No documents retrieved yet.
        </div>
        """

    else:

        for doc in documents:

            source = doc.metadata.get("source","Unknown")

            page = doc.metadata.get("page",0)+1

            filename = source.split("\\")[-1].split("/")[-1]

            html += f"""
            <div class="source-item">

                <div class="source-name">
                    {filename}
                </div>

                <div class="source-page">
                    Page {page}
                </div>

            </div>
            """

    html += "</div>"

    st.html(html)


# ==========================================
# Metric Cards
# ==========================================

def metric_cards():

    col1,col2,col3,col4 = st.columns(4)

    metrics = [

        ("Documents","10"),

        ("Chunks","10"),

        ("Embedding","MiniLM"),

        ("LLM","Gemini"),

    ]

    cols = [col1,col2,col3,col4]

    for col,(title,value) in zip(cols,metrics):

        with col:

            st.html(f"""
            <div class="metric-card">

                <div class="metric-value">
                    {value}
                </div>

                <div class="metric-title">
                    {title}
                </div>

            </div>
            """)