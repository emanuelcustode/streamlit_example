import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

pg = st.navigation([st.Page("welcome.py"),
                    st.Page("players.py"),
                    st.Page("coaches.py"),
                    st.Page("teams.py"), ])
pg.run()