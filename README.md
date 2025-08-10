# AirBiome Project: Microbial Association Networks Summary

This repository contains a summary of the main results for the microbial association networks from the AirBiome project. The reports 
were generated using [VueGen](https://github.com/Multiomics-Analytics-Group/vuegen), a tool to automate the creation of scientific reports.

## Project Structure

The repository is organized as follows:

| Folder | Description |
|---|---|
| `AirBiome_microbial_association_networks_summary/` | Contains all the data and raw outputs from the analysis. |
| `streamlit_report/` | Contains the scripts for a Streamlit report. This interactive report allows for dynamic exploration of the output. |
| `quarto_report/` | Includes HTML and Reveal.js reports. |
| `airbiome_microbial_association_networks_summary_config.yaml` | Configuration file for the VueGen report generation, which can be extended with additional information. |
| `Network_visualizations_cytoscape/` | Holds Cytoscape session files for detailed network visualizations of adjacency and association networks. |

## How to Run the Reports

### Streamlit Report

To run the interactive Streamlit report, ensure you have the required dependencies installed, then navigate to the `streamlit_report` directory and run the main script.

```bash
cd streamlit_report
pip install -r requirements.txt
streamlit run sections/report_manager.py
```

### Quarto Reports

The HTML and Reveal.js reports in the `quarto_report` directory can be viewed directly in a web browser.

## Scripts, Data and Raw Outputs

The scripts, data, and raw outputs used to generate these reports are available in this [repository](https://github.com/Multiomics-Analytics-Group/airbiome).


