import streamlit as st

create_page = st.Page("graph_page.py", title="Relationship Visualization")
delete_page = st.Page("app.py", title="Main Chat")

pg = st.navigation([delete_page, create_page])
pg.run()