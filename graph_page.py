# pages/graph_page.py
# ---
# NetworkX Graph Visualization

import streamlit as st
import networkx as nx
from pyvis.network import Network
import tempfile

# st.set_page_config(page_title="NetworkX Visualization")

st.title("NetworkX Visualization")
# Set up LightRAG
WORKING_DIR = "./data/Affiliations/"


st.logo("./static/duke_match2.png", size = "large")
# Create a sample NetworkX graph
G = nx.read_graphml(WORKING_DIR + "graph_chunk_entity_relation.graphml")

# Convert NetworkX graph to Pyvis graph
net = Network(notebook=True)
net.from_nx(G)

# Save and display the interactive graph in Streamlit
with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
    path = WORKING_DIR + "temp.html"
    net.save_graph(path)

    # Display the graph in an iframe
    st.components.v1.html(open(path).read(), height=500)
        
        
        
        