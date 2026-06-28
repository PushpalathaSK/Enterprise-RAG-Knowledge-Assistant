import streamlit as st


def sidebar():

    with st.sidebar:

        st.markdown("## Knowledge Base")

        st.divider()

        docs = [

            "Employee Handbook",

            "Leave Policy",

            "HR Policy",

            "Training Policy",

            "IT Security",

            "Code of Conduct",

            "Performance Policy",

            "Travel Policy",

            "WFH Policy",

        ]

        for doc in docs:

            st.write(doc)

        st.divider()

        st.markdown("## System")

        st.write("Documents : 10")

        st.write("Chunks : 10")

        st.write("Embedding : MiniLM")

        st.write("LLM : Gemini")