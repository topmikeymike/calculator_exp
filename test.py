import streamlit as st
import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def main():
    st.title("Expenditure Calculator")

    # Load data from CSV file
    file_path_negeri_daerah = r"C:\Users\michael.igo\Documents\Coding\calculator_exp\data\Negeri_Daerah.csv"
    data_negeri_daerah = load_data(file_path_negeri_daerah)

    # Display the options in a single-select dropdown for Negeri
    selected_negeri = st.selectbox("Select Negeri", [""] + list(data_negeri_daerah['NEGERI'].unique()))

    # Filter Daerah options based on selected Negeri
    daerah_options = list(data_negeri_daerah[data_negeri_daerah['NEGERI'] == selected_negeri]['DAERAH'].unique())
    selected_daerah = st.selectbox("Select Daerah", [""] + daerah_options)

    # ... Rest of your main content ...

    st.write("Selected Negeri:", selected_negeri)
    st.write("Selected Daerah:", selected_daerah)

if __name__ == "__main__":
    main()
