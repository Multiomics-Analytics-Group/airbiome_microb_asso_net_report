import os
import time

import psutil
import streamlit as st

st.set_page_config(layout="wide",
                   page_title="Airbiome Microbial Association Networks Summary")

st.markdown(
    '''
    <h1 style='text-align: center;
    color: #023858;'>
    Airbiome Microbial Association Networks Summary
    </h1>
    ''',
    unsafe_allow_html=True)


sections_pages = {}
homepage = st.Page('Home/Homepage.py', title='Homepage')
sections_pages['Home'] = [homepage]

Nopge_Genus_Adj = st.Page('Adjacency_Networks/Nopge_Genus_Adj.py', title='Nopge Genus Adj')
Nopge_Species_Adj = st.Page('Adjacency_Networks/Nopge_Species_Adj.py', title='Nopge Species Adj')
Pge_Genus_Adj = st.Page('Adjacency_Networks/Pge_Genus_Adj.py', title='Pge Genus Adj')
Pge_Species_Adj = st.Page('Adjacency_Networks/Pge_Species_Adj.py', title='Pge Species Adj')
sections_pages['Adjacency Networks'] = [Nopge_Genus_Adj, Nopge_Species_Adj, Pge_Genus_Adj, Pge_Species_Adj]

Nopge_Genus_Asso = st.Page('Association_Networks/Nopge_Genus_Asso.py', title='Nopge Genus Asso')
Nopge_Species_Asso = st.Page('Association_Networks/Nopge_Species_Asso.py', title='Nopge Species Asso')
Pge_Genus_Asso = st.Page('Association_Networks/Pge_Genus_Asso.py', title='Pge Genus Asso')
Pge_Species_Asso = st.Page('Association_Networks/Pge_Species_Asso.py', title='Pge Species Asso')
sections_pages['Association Networks'] = [Nopge_Genus_Asso, Nopge_Species_Asso, Pge_Genus_Asso, Pge_Species_Asso]

report_nav = st.navigation(sections_pages)

# Following https://discuss.streamlit.io/t/close-streamlit-app-with-button-click/35132/5
exit_app = st.sidebar.button("Shut Down App",
                             icon=":material/power_off:",
                             use_container_width=True)
if exit_app:
    st.toast("Shutting down the app...")
    time.sleep(1)
    # Terminate streamlit python process
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()


report_nav.run()
