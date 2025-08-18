from pathlib import Path
from st_aggrid import AgGrid, GridOptionsBuilder
from vuegen import table_utils
import json
import pandas as pd
import requests
import streamlit as st
df_index = 1
section_dir = Path(__file__).resolve().parent.parent

st.markdown(
    '''
    <h3 style='text-align: center;
    color: #023558;'>
    Pge Species Asso
    </h3>
    ''',
    unsafe_allow_html=True)

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Network Metrics All Thresholds
    </h4>
    ''',
    unsafe_allow_html=True)

selected_sheet = 0
file_path = (section_dir / '../../AirBiome_microbial_association_networks_summary/Association_networks/PGE_species_asso/1_Network_metrics_all_thresholds.xlsx').resolve()
df = pd.read_excel(file_path, sheet_name=selected_sheet)


# Displays a DataFrame using AgGrid with configurable options.
grid_builder = GridOptionsBuilder.from_dataframe(df)
grid_builder.configure_default_column(editable=True,
                                      groupable=True,
                                      filter=True,
)
grid_builder.configure_side_bar(filters_panel=True,
                                columns_panel=True)
grid_builder.configure_selection(selection_mode="multiple")
grid_builder.configure_pagination(enabled=True,
                                paginationAutoPageSize=False,
                                paginationPageSize=20,
)
grid_options = grid_builder.build()

AgGrid(df, gridOptions=grid_options, enable_enterprise_modules=True)

# Button to download the df
df_csv = df.to_csv(sep=',', header=True, index=False
                  ).encode('utf-8')
st.download_button(
    label="Download dataframe as CSV",
    data=df_csv,
    file_name=f"dataframe_{df_index}.csv",
    mime='text/csv',
    key=f"download_button_{df_index}")
df_index += 1
st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Cclasso No Singletons Threshold 55 Edgelist
    </h4>
    ''',
    unsafe_allow_html=True)


file_path = (section_dir / '../static/Cclasso_No_Singletons_Threshold_55_Edgelist.html').resolve().as_posix()
with open(file_path, 'r') as html_file:
    html_content = html_file.read()


st.markdown(("<p style='text-align: center; color: black;'> "
            "<b>Number of nodes:</b> 18 </p>"),
            unsafe_allow_html=True)
st.markdown(("<p style='text-align: center; color: black;'>"
             " <b>Number of relationships:</b> 20"
             " </p>"),
            unsafe_allow_html=True)

# Streamlit checkbox for controlling the layout
control_layout = st.checkbox('Add panel to control layout', value=True)
net_html_height = 1200 if control_layout else 630
# Load HTML into HTML component for display on Streamlit
st.components.v1.html(html_content, height=net_html_height)

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Centrality Metrics All Nodes
    </h4>
    ''',
    unsafe_allow_html=True)

file_path = (section_dir / '../../AirBiome_microbial_association_networks_summary/Association_networks/PGE_species_asso/3_centrality_metrics_all_nodes.csv').resolve().as_posix()
df = pd.read_csv(file_path)


# Displays a DataFrame using AgGrid with configurable options.
grid_builder = GridOptionsBuilder.from_dataframe(df)
grid_builder.configure_default_column(editable=True,
                                      groupable=True,
                                      filter=True,
)
grid_builder.configure_side_bar(filters_panel=True,
                                columns_panel=True)
grid_builder.configure_selection(selection_mode="multiple")
grid_builder.configure_pagination(enabled=True,
                                paginationAutoPageSize=False,
                                paginationPageSize=20,
)
grid_options = grid_builder.build()

AgGrid(df, gridOptions=grid_options, enable_enterprise_modules=True)

# Button to download the df
df_csv = df.to_csv(sep=',', header=True, index=False
                  ).encode('utf-8')
st.download_button(
    label="Download dataframe as CSV",
    data=df_csv,
    file_name=f"dataframe_{df_index}.csv",
    mime='text/csv',
    key=f"download_button_{df_index}")
df_index += 1
st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Module Taxa Membership
    </h4>
    ''',
    unsafe_allow_html=True)

file_path = (section_dir / '../../AirBiome_microbial_association_networks_summary/Association_networks/PGE_species_asso/4_module_taxa_membership.csv').resolve().as_posix()
df = pd.read_csv(file_path)


# Displays a DataFrame using AgGrid with configurable options.
grid_builder = GridOptionsBuilder.from_dataframe(df)
grid_builder.configure_default_column(editable=True,
                                      groupable=True,
                                      filter=True,
)
grid_builder.configure_side_bar(filters_panel=True,
                                columns_panel=True)
grid_builder.configure_selection(selection_mode="multiple")
grid_builder.configure_pagination(enabled=True,
                                paginationAutoPageSize=False,
                                paginationPageSize=20,
)
grid_options = grid_builder.build()

AgGrid(df, gridOptions=grid_options, enable_enterprise_modules=True)

# Button to download the df
df_csv = df.to_csv(sep=',', header=True, index=False
                  ).encode('utf-8')
st.download_button(
    label="Download dataframe as CSV",
    data=df_csv,
    file_name=f"dataframe_{df_index}.csv",
    mime='text/csv',
    key=f"download_button_{df_index}")
df_index += 1
st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Module Means
    </h4>
    ''',
    unsafe_allow_html=True)

file_path = (section_dir / '../../AirBiome_microbial_association_networks_summary/Association_networks/PGE_species_asso/5_module_means.csv').resolve().as_posix()
df = pd.read_csv(file_path)


# Displays a DataFrame using AgGrid with configurable options.
grid_builder = GridOptionsBuilder.from_dataframe(df)
grid_builder.configure_default_column(editable=True,
                                      groupable=True,
                                      filter=True,
)
grid_builder.configure_side_bar(filters_panel=True,
                                columns_panel=True)
grid_builder.configure_selection(selection_mode="multiple")
grid_builder.configure_pagination(enabled=True,
                                paginationAutoPageSize=False,
                                paginationPageSize=20,
)
grid_options = grid_builder.build()

AgGrid(df, gridOptions=grid_options, enable_enterprise_modules=True)

# Button to download the df
df_csv = df.to_csv(sep=',', header=True, index=False
                  ).encode('utf-8')
st.download_button(
    label="Download dataframe as CSV",
    data=df_csv,
    file_name=f"dataframe_{df_index}.csv",
    mime='text/csv',
    key=f"download_button_{df_index}")
df_index += 1
st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Module Means Heatmap
    </h4>
    ''',
    unsafe_allow_html=True)


file_path = (section_dir / '../../AirBiome_microbial_association_networks_summary/Association_networks/PGE_species_asso/6_module_means_heatmap.json').resolve().as_posix()
with open(file_path, 'r') as plot_file:
    plot_json = json.load(plot_file)

# Keep only 'data' and 'layout' sections
plot_json = {key: plot_json[key] for key in plot_json
                                 if key in ['data', 'layout']}

# Remove 'frame' section in 'data'
plot_json['data'] = [{k: v for k, v in entry.items() if k != 'frame'}
                                for entry in plot_json.get('data', [])]
st.plotly_chart(plot_json, use_container_width=True)

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Module Variability
    </h4>
    ''',
    unsafe_allow_html=True)


file_path = (section_dir / '../../AirBiome_microbial_association_networks_summary/Association_networks/PGE_species_asso/7_module_variability.json').resolve().as_posix()
with open(file_path, 'r') as plot_file:
    plot_json = json.load(plot_file)

# Keep only 'data' and 'layout' sections
plot_json = {key: plot_json[key] for key in plot_json
                                 if key in ['data', 'layout']}

# Remove 'frame' section in 'data'
plot_json['data'] = [{k: v for k, v in entry.items() if k != 'frame'}
                                for entry in plot_json.get('data', [])]
st.plotly_chart(plot_json, use_container_width=True)

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Module Metadata Correlations
    </h4>
    ''',
    unsafe_allow_html=True)

file_path = (section_dir / '../../AirBiome_microbial_association_networks_summary/Association_networks/PGE_species_asso/8_module_metadata_correlations.csv').resolve().as_posix()
df = pd.read_csv(file_path)


# Displays a DataFrame using AgGrid with configurable options.
grid_builder = GridOptionsBuilder.from_dataframe(df)
grid_builder.configure_default_column(editable=True,
                                      groupable=True,
                                      filter=True,
)
grid_builder.configure_side_bar(filters_panel=True,
                                columns_panel=True)
grid_builder.configure_selection(selection_mode="multiple")
grid_builder.configure_pagination(enabled=True,
                                paginationAutoPageSize=False,
                                paginationPageSize=20,
)
grid_options = grid_builder.build()

AgGrid(df, gridOptions=grid_options, enable_enterprise_modules=True)

# Button to download the df
df_csv = df.to_csv(sep=',', header=True, index=False
                  ).encode('utf-8')
st.download_button(
    label="Download dataframe as CSV",
    data=df_csv,
    file_name=f"dataframe_{df_index}.csv",
    mime='text/csv',
    key=f"download_button_{df_index}")
df_index += 1
st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Module Metadata Correlations Volcano Plot
    </h4>
    ''',
    unsafe_allow_html=True)


file_path = (section_dir / '../../AirBiome_microbial_association_networks_summary/Association_networks/PGE_species_asso/9_module_metadata_correlations_volcano_plot.json').resolve().as_posix()
with open(file_path, 'r') as plot_file:
    plot_json = json.load(plot_file)

# Keep only 'data' and 'layout' sections
plot_json = {key: plot_json[key] for key in plot_json
                                 if key in ['data', 'layout']}

# Remove 'frame' section in 'data'
plot_json['data'] = [{k: v for k, v in entry.items() if k != 'frame'}
                                for entry in plot_json.get('data', [])]
st.plotly_chart(plot_json, use_container_width=True)

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Significant Module Metadata Correlations
    </h4>
    ''',
    unsafe_allow_html=True)

file_path = (section_dir / '../../AirBiome_microbial_association_networks_summary/Association_networks/PGE_species_asso/10_significant_module_metadata_correlations.csv').resolve().as_posix()
df = pd.read_csv(file_path)


# Displays a DataFrame using AgGrid with configurable options.
grid_builder = GridOptionsBuilder.from_dataframe(df)
grid_builder.configure_default_column(editable=True,
                                      groupable=True,
                                      filter=True,
)
grid_builder.configure_side_bar(filters_panel=True,
                                columns_panel=True)
grid_builder.configure_selection(selection_mode="multiple")
grid_builder.configure_pagination(enabled=True,
                                paginationAutoPageSize=False,
                                paginationPageSize=20,
)
grid_options = grid_builder.build()

AgGrid(df, gridOptions=grid_options, enable_enterprise_modules=True)

# Button to download the df
df_csv = df.to_csv(sep=',', header=True, index=False
                  ).encode('utf-8')
st.download_button(
    label="Download dataframe as CSV",
    data=df_csv,
    file_name=f"dataframe_{df_index}.csv",
    mime='text/csv',
    key=f"download_button_{df_index}")
df_index += 1
st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Top Correlations Heatmap
    </h4>
    ''',
    unsafe_allow_html=True)


file_path = (section_dir / '../../AirBiome_microbial_association_networks_summary/Association_networks/PGE_species_asso/11_top_correlations_heatmap.json').resolve().as_posix()
with open(file_path, 'r') as plot_file:
    plot_json = json.load(plot_file)

# Keep only 'data' and 'layout' sections
plot_json = {key: plot_json[key] for key in plot_json
                                 if key in ['data', 'layout']}

# Remove 'frame' section in 'data'
plot_json['data'] = [{k: v for k, v in entry.items() if k != 'frame'}
                                for entry in plot_json.get('data', [])]
st.plotly_chart(plot_json, use_container_width=True)

footer = '''
<style type="text/css">
.footer {
    position: relative;
    left: 0;
    width: 100%;
    text-align: center;
}
</style>
<footer class="footer">
    This report was generated with
    <a href="https://github.com/Multiomics-Analytics-Group/vuegen" target="_blank">
        <img src="https://raw.githubusercontent.com/Multiomics-Analytics-Group/vuegen/HEAD/docs/images/logo/vuegen_logo.svg" alt="VueGen" width="65px">
    </a>
    | Copyright 2025 <a href="https://github.com/Multiomics-Analytics-Group" target="_blank">
        Multiomics Network Analytics Group (MoNA)
    </a>
</footer>
'''

st.markdown(footer, unsafe_allow_html=True)
