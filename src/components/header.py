import base64
from pathlib import Path

import streamlit as st


def _logo_src():
    """Return an embeddable logo so Streamlit can display it reliably."""
    logo_path = Path(__file__).resolve().parent.parent / "logo.jpeg"

    if not logo_path.exists():
        return ""

    encoded = base64.b64encode(logo_path.read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"


def header_home():
    logo_src = _logo_src()
    logo = f"<img src='{logo_src}' alt='SynClass logo' style='height:100px; object-fit:contain; border-radius:19px;' />" if logo_src else ""

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center;
                    width:100%; min-height:150px; margin:30px 0 30px 0;
                    color:#5865F2; visibility:visible;">
            {logo}
            <h1 style="display:block; width:100%; text-align:center; margin:10px 0 0 0;
                       color:#5865F2; opacity:1; font-weight:700; line-height:1.2;
                       text-shadow:0 1px 2px rgba(0,0,0,0.25);">SynClass</h1>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_src = _logo_src()
    logo = f"<img src='{logo_src}' alt='SynClass logo' style='height:85px; object-fit:contain; border-radius:8px;' />" if logo_src else ""

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px;
                    width:100%; min-height:85px; margin:10px 0;
                    color:#5865F2; visibility:visible;">
            {logo}
            <h2 style="display:block; margin:0; text-align:left; color:#5865F2;
                       opacity:1; font-weight:700; line-height:1.2;
                       text-shadow:0 1px 2px rgba(0,0,0,0.25);">SynClass</h2>
        </div>
    """, unsafe_allow_html=True)