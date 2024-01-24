import streamlit as st
import pandas as pd


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def header():
    st.title("Expenditure Calculator")


def main_content():

    # Load data from CSV files
    file_path_negeri_daerah = r"C:\Users\michael.igo\Documents\Coding\calculator_exp\data\Negeri_Daerah.csv"
    # file_path_strata = r"C:\Users\michael.igo\Documents\Coding\calculator_exp\data\LU_STRATA.csv"
    # data_strata = load_data(file_path_strata)
    data_negeri_daerah = load_data(file_path_negeri_daerah)

    # Display the options in a single-select dropdown for Negeri
    selected_negeri = st.selectbox("Select Negeri", [""] + list(data_negeri_daerah['NEGERI'].unique()))
    st.write("Selected Negeri:", selected_negeri)

    # Filter Daerah options based on selected Negeri
    daerah_options = list(data_negeri_daerah[data_negeri_daerah['NEGERI'] == selected_negeri]['DAERAH'].unique())
    selected_daerah = st.selectbox("Select Daerah", [""] + daerah_options)
    st.write("Selected Daerah:", selected_daerah)

    
    # Display the options in a single-select dropdown for Strata
    selected_strata = st.selectbox("Select Strata", [""] + list(data_negeri_daerah['STRATA'].dropna().unique()))
    st.write("Selected Strata:", selected_strata)

    # Display the options in a single-select dropdown for Jantina
    selected_jantina = st.selectbox("Select Jantina", [""] + list(data_negeri_daerah['JANTINA'].dropna().unique()))
    st.write("Selected Jantina:", selected_jantina)

    # Display the options in a single-select dropdown for Etnik
    selected_etnik = st.selectbox("Select Etnik", [""] + list(data_negeri_daerah['KUMP_ETNIK'].dropna().unique()))
    st.write("Selected Etnik:", selected_etnik)

    # Get user input for an integer
    user_input_bil_air = st.number_input("Bilangan Isi Rumah:", value=0, step=1)

    # Display the entered integer
    st.write("Bilangan Isi Rumah:", user_input_bil_air)
    
    # Get user input for an integer
    user_input_bil_oku = st.number_input("Bilangan OKU:", value=0, step=1)

    # Display the entered integer
    st.write("Bilangan OKU:", user_input_bil_oku)


    # Get user input for an integer
    user_input_bil_wargaEmas = st.number_input("Bilangan Warga Emas:", value=0, step=1)

    # Display the entered integer
    st.write("Bilangan Warga Emas:", user_input_bil_wargaEmas)


    # Get user input for an integer
    user_input_bil_kanak2 = st.number_input("Bilangan Kanak-Kanak:", value=0, step=1)

    # Display the entered integer
    st.write("Bilangan Kanak-Kanak:", user_input_bil_air)

    # Get user input for income (double)
    user_input_hh_income = st.number_input("Pendapatan Isi Rumah:", value=0.0, step=0.01, format="%.2f")

    # Display the entered income with a default value
    st.write("Pendapatan Isi Rumah: RM {:.2f}".format(user_input_hh_income))


 
 
def footer():
    # Footer with logo
    st.markdown(
        """
        <div style="text-align:center; padding: 10px;">
            <img src="https://example.com/your_logo.png" alt="Your Logo" width="100">
        </div>
        """,
        unsafe_allow_html=True
    )