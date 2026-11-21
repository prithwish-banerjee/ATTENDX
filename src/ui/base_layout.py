import streamlit as st



def style_background_home():

    st.markdown("""
        <style>
            .stApp {
                background:
                    radial-gradient(circle at 8% 8%, rgba(255,255,255,.26), transparent 28%),
                    radial-gradient(circle at 90% 85%, rgba(88,101,242,.3), transparent 32%),
                    #8273B8 !important;
            }

            .stApp div[data-testid="stColumn"] {
                background: rgba(255, 255, 255, .86) !important;
                padding: 2rem !important;
                border: 1px solid rgba(255,255,255,.65) !important;
                border-radius: 2rem !important;
                box-shadow: 0 18px 45px rgba(23,36,59,.13) !important;
                backdrop-filter: blur(12px);
            }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

            .stApp {
                background:
                    radial-gradient(circle at 5% 0%, rgba(130,115,184,.22), transparent 30%),
                    linear-gradient(135deg, #f8f9ff 0%, #e0e3ff 100%) !important;
            }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@300;400;500;600;700&display=swap');

            :root { --ink:#17243B; --purple:#8273B8; --blue:#5865F2; --pink:#EB459E; }
            #MainMenu { visibility: visible; }
            footer { visibility: hidden; }
            header, [data-testid="stHeader"] {
                background: rgba(23, 36, 59, .12) !important;
            }
            .block-container {
                max-width: 1200px;
                padding: 2.5rem 2rem 4rem !important;
            }
            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                letter-spacing: -.04em !important;
                margin-bottom: .5rem !important;
                color: var(--ink) !important;
            }
            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: .95 !important;
                margin-bottom: .5rem !important;
                color: var(--purple) !important;
            }

            h3, h4, p, label, .stCaption {
                font-family: 'Outfit', sans-serif !important;
            }
            h3, h4 { color: var(--ink) !important; }
            p { color: #526078 !important; line-height: 1.6 !important; }
            .stMarkdown { color: var(--ink) !important; }

            /* Cards and form controls */
            div[data-testid="stMetric"], div[data-testid="stExpander"],
            div[data-testid="stFileUploader"] {
                background: rgba(255,255,255,.72) !important;
                border: 1px solid rgba(130,115,184,.16) !important;
                border-radius: 1.25rem !important;
                box-shadow: 0 8px 26px rgba(23,36,59,.07) !important;
                padding: .8rem !important;
            }
            input, textarea, [data-baseweb="select"] > div {
                border-radius: .8rem !important;
                border-color: #d7d9ed !important;
                background: rgba(255,255,255,.9) !important;
                color: var(--ink) !important;
            }
            input::placeholder, textarea::placeholder {
                color: #526078 !important;
                opacity: 1 !important;
            }
            input:focus, textarea:focus { border-color: var(--blue) !important; box-shadow: 0 0 0 3px rgba(88,101,242,.14) !important; }

            button {
                border-radius: .85rem !important;
                color: white !important;
                padding: .65rem 1.25rem !important;
                border: 0 !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                background: linear-gradient(135deg, var(--blue), #747cff) !important;
                box-shadow: 0 8px 18px rgba(88,101,242,.22) !important;
                transition: transform .2s ease, box-shadow .2s ease !important;
            }
            button[kind="secondary"] { background: linear-gradient(135deg, var(--pink), #f574ba) !important; box-shadow: 0 8px 18px rgba(235,69,158,.2) !important; }
            button[kind="tertiary"] { background: var(--ink) !important; box-shadow: none !important; }
            button:hover { transform: translateY(-2px); box-shadow: 0 12px 24px rgba(23,36,59,.18) !important; }
            [data-testid="stSidebar"] { background: rgba(255,255,255,.8) !important; border-right: 1px solid rgba(130,115,184,.15); }

            @media (max-width: 700px) {
                .block-container { padding: 1.5rem 1rem 3rem !important; }
                h1 { font-size: 2.5rem !important; }
            }
        </style>  

                """
            ,unsafe_allow_html=True)
