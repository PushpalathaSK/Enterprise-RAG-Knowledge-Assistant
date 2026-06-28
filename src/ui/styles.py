import streamlit as st


def load_css():
    st.markdown(
        """
        <style>

        /* -----------------------------
           Global
        ------------------------------ */

        .main {
            background-color: #F8FAFC;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1300px;
        }

        /* -----------------------------
           Header
        ------------------------------ */

        .main-title {
            font-size: 38px;
            font-weight: 700;
            color: #111827;
            margin-bottom: 0;
        }

        .sub-title {
            font-size: 16px;
            color: #6B7280;
            margin-bottom: 30px;
        }

        /* -----------------------------
           Cards
        ------------------------------ */

        .card {

            background: white;

            padding:20px;

            border-radius:12px;

            border:1px solid #E5E7EB;

            margin-bottom:20px;

            box-shadow:
            0 1px 3px rgba(0,0,0,0.05);

        }

        /* -----------------------------
           Section Title
        ------------------------------ */

        .section-title{

            font-size:20px;

            font-weight:600;

            color:#111827;

            margin-bottom:15px;

        }

        /* -----------------------------
           Sidebar
        ------------------------------ */

        section[data-testid="stSidebar"]{

            background:#FFFFFF;

            border-right:
            1px solid #E5E7EB;

        }

        /* -----------------------------
           Buttons
        ------------------------------ */

        .stButton>button{

            background:#2563EB;

            color:white;

            border-radius:8px;

            border:none;

            height:48px;

            width:100%;

            font-weight:600;

        }

        .stButton>button:hover{

            background:#1D4ED8;

            color:white;

        }

        /* -----------------------------
           Text Area
        ------------------------------ */

        textarea{

            border-radius:10px !important;

        }
        /* ===========================
   Hero Section
=========================== */

.hero-card{

display:flex;

justify-content:space-between;

align-items:center;

background:white;

padding:30px;

border-radius:14px;

border:1px solid #E5E7EB;

margin-bottom:30px;

box-shadow:
0 4px 12px rgba(0,0,0,0.04);

}

.hero-title{

font-size:40px;

font-weight:700;

color:#111827;

margin-bottom:8px;

}

.hero-subtitle{

font-size:17px;

color:#6B7280;

}

.status-badge{

background:#DCFCE7;

color:#15803D;

padding:10px 18px;

border-radius:25px;

font-weight:600;

border:1px solid #BBF7D0;

}

/* ===========================
   Search Panel
=========================== */

.search-card{

background:white;

padding:25px;

border-radius:14px;

border:1px solid #E5E7EB;

margin-bottom:15px;

box-shadow:
0 4px 10px rgba(0,0,0,0.04);

}

.search-title{

font-size:26px;

font-weight:600;

color:#111827;

margin-bottom:10px;

}

.search-subtitle{

font-size:15px;

color:#6B7280;

margin-bottom:5px;

}

/* Text Area */

textarea{

font-size:16px !important;

padding:15px !important;

}

/* Search Button */

.stButton>button{

height:48px;

font-size:16px;

font-weight:600;

border-radius:10px;

}

/* ===========================
   Answer Card
=========================== */

.answer-card{

background:white;

padding:28px;

border-radius:14px;

border:1px solid #E5E7EB;

margin-top:20px;

box-shadow:
0 4px 12px rgba(0,0,0,0.04);

}

.answer-title{

font-size:22px;

font-weight:600;

color:#111827;

margin-bottom:18px;

}

.answer-body{

font-size:16px;

line-height:1.8;

color:#374151;

white-space:pre-wrap;

}

        </style>
        """,
        unsafe_allow_html=True,
    )