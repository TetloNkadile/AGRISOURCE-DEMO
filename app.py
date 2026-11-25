"""AgriSource stakeholder demonstration, preserving the original HTML interface.

Deployment: streamlit run app.py
Security: optional shared password gate; prefer private Streamlit app invites too.
This is a wrapper, NOT a production multi-user/backend implementation.
"""

from __future__ import annotations

import hmac
import os
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parent
HTML_FILE = APP_DIR / "agrisource_demo.html"

st.set_page_config(
    page_title="AgriSource | Agricultural Commerce & Fulfilment",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# These overrides affect only Streamlit's outer shell, not the approved
# AgriSource HTML styles, cards, menus, workflows or page structure.
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] { background: #f5f7f2; }
    [data-testid="stMain"] { padding: 0 !important; }
    [data-testid="stMainBlockContainer"] {
        max-width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    [data-testid="stHeader"] { height: 0 !important; min-height: 0 !important; }
    [data-testid="stDecoration"] { display: none !important; }
    div[data-testid="stIFrame"] { margin: 0 !important; }
    div[data-testid="stIFrame"] iframe { border: none !important; display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)


def get_gate_password() -> str:
    """Read the secret on the server; no password is shipped in the demo."""
    try:
        secret = st.secrets.get("AGRISOURCE_ACCESS_PASSWORD", "")
    except (FileNotFoundError, KeyError, OSError):
        secret = ""
    return str(secret or os.environ.get("AGRISOURCE_ACCESS_PASSWORD", "")).strip()


def require_optional_access_password() -> None:
    expected = get_gate_password()
    if not expected or st.session_state.get("agrisource_access_ok"):
        return

    # The gate appears only when a deployment password is configured.
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### AgriSource — Stakeholder Demo")
        st.caption("Private preview by Agroproducts and Technologies")
        st.write("Enter the access password supplied with your invitation.")
        with st.form("agrisource_access_form", clear_on_submit=True):
            supplied = st.text_input("Access password", type="password")
            entered = st.form_submit_button("Open demo", use_container_width=True)
        if entered:
            if hmac.compare_digest(supplied, expected):
                st.session_state["agrisource_access_ok"] = True
                st.rerun()
            else:
                st.error("That access password was not recognised.")
    st.stop()


require_optional_access_password()

if not HTML_FILE.is_file():
    st.error("AgriSource interface not found: agrisource_demo.html")
    st.stop()

# Supported by Streamlit 1.57+: the full HTML document is isolated inside
# an iframe, preserving existing JavaScript, navigation, styling and images.
# The iframe resizes with content, avoiding a separate internal scrollbar.
st.iframe(
    HTML_FILE,
    width="stretch",
    height="content",
    alt="AgriSource agricultural marketplace and fulfilment demo",
)
