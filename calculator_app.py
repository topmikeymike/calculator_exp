import streamlit as st
import pandas as pd
import numpy as np
import math


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def header():
    st.title("Expenditure Calculator 🌟")
    st.markdown(
        """
        <div style="text-align: justify; font-size: 20px; line-height: 1.6; color: #444;">
            <p>Feeling the pinch in the middle of the month?</p>
            <p>Wondering how your monthly expenses should look?</p>
            <p>Introducing the Expenditure Prediction Calculator.</p>
            <p style="font-weight: bold;">Let our AI model calculate your expenses based on your inputs.</p>
        </div>
        """,
        unsafe_allow_html=True
    ) 


def main_content():

    # Load data from CSV files
    file_path_negeri_daerah = "data/Negeri_Daerah.csv"
    file_model = "data/modelv1.csv"
    # file_path_strata = r"C:\Users\michael.igo\Documents\Coding\calculator_exp\data\LU_STRATA.csv"
    # data_strata = load_data(file_path_strata)
    data_negeri_daerah = load_data(file_path_negeri_daerah)
    data_model = load_data(file_model)
    
    # Create a dictionary to map items to coefficients
    default_feature = 0.0
    
    # # # Display data_model
    # st.write("Data Model:")
    # st.dataframe(data_model)
    
    # Display the options in a single-select dropdown for Negeri
    selected_negeri = st.selectbox("Negeri", ["Selangor"] + list(data_negeri_daerah['NEGERI'].unique()))


    # Filter Daerah options based on selected Negeri
    daerah_options = list(data_negeri_daerah[data_negeri_daerah['NEGERI'] == selected_negeri]['DAERAH'].unique())
    selected_daerah = st.selectbox("Daerah", [""] + daerah_options)

    # daerah_coeff_dict = dict(zip(daerah_list, coefficients))
    item_coeff_dict = dict(zip(data_model['Item'], data_model['Coefficient']))
    data_model['Coefficient'] = round(data_model['Coefficient'], 12)
    # Handle Petaling as a special case
    if selected_daerah == "Petaling":
        # Set all feature values to 0 for Petaling
        selected_coefficient = default_feature

    else:
        # Use the selected Daerah to get its coefficient
        selected_coefficient = item_coeff_dict.get(selected_daerah, default_feature)

    # Display the coefficient for the selected Daerah
    # st.write(f"Coefficient for {selected_daerah}: {round(selected_coefficient, 12)}") 

    
    # Display the options in a single-select dropdown for Strata
    selected_strata = st.selectbox("Strata", ["Bandar"] + list(data_negeri_daerah['STRATA'].dropna().unique()))
    
     # Handle Bandar as a special case
    if selected_strata == "Bandar":
        # Set all feature values to 0 for Bandar
        selected_coefficient = default_feature
    else:
        # Use the selected Daerah to get its coefficient
        selected_coefficient = item_coeff_dict.get(selected_strata, default_feature)

    # Display the coefficient for the selected Daerah
    # st.write(f"Coefficient for {selected_strata}: {round(selected_coefficient, 12)}") 
    
    # Display the options in a single-select dropdown for Jantina
    selected_jantina = st.selectbox("Jantina KIR(Ketua Isi Rumah)", ["Lelaki"] + list(data_negeri_daerah['JANTINA'].dropna().unique()))
    
     # Handle Bandar as a special case
    if selected_jantina == "Lelaki":
        # Set all feature values to 0 for Bandar
        selected_coefficient = default_feature
    else:
        # Use the selected Daerah to get its coefficient
        selected_coefficient = item_coeff_dict.get(selected_jantina, default_feature)

    # Display the coefficient for the selected Daerah
    # st.write(f"Coefficient for {selected_jantina}: {round(selected_coefficient, 12)}") 
    
    # Display the options in a single-select dropdown for Etnik
    selected_etnik = st.selectbox("Etnik KIR(Ketua Isi Rumah)", ["Melayu"] + list(data_negeri_daerah['KUMP_ETNIK'].dropna().unique()))
    
    # Handle Bandar as a special case
    if selected_etnik == "Melayu":
        # Set all feature values to 0 for Bandar
        selected_coefficient = default_feature
    else:
        # Use the selected Daerah to get its coefficient
        selected_coefficient = item_coeff_dict.get(selected_etnik, default_feature)

    # Display the coefficient for the selected Daerah
    # st.write(f"Coefficient for {selected_etnik}: {round(selected_coefficient, 12)}") 

    # # Get user input for an integer
    # user_input_bil_air = st.number_input("Bilangan Isi Rumah:", key="bil_air", value=0, step=1)

    # # Display the entered integer
    # st.write("Bilangan Isi Rumah:", user_input_bil_air)

    # # Get user input for an integer
    # user_input_bil_oku = st.number_input("Bilangan OKU:", key="bil_oku", value=0, step=1)

    # # Display the entered integer
    # st.write("Bilangan OKU:", user_input_bil_oku)

    # # Get user input for an integer
    # user_input_bil_wargaEmas = st.number_input("Bilangan Warga Emas:", key="bil_wargaEmas", value=0, step=1)

    # # Display the entered integer
    # st.write("Bilangan Warga Emas:", user_input_bil_wargaEmas)

    # # Get user input for an integer
    # user_input_bil_kanak2 = st.number_input("Bilangan Kanak-Kanak:", key="bil_kanak2", value=0, step=1)

    # # Display the entered integer
    # st.write("Bilangan Kanak-Kanak:", user_input_bil_kanak2)

    # # Get user input for income (double)
    # user_input_hh_income = st.number_input("Pendapatan Isi Rumah:", key="hh_income", value=0.0, step=0.01, format="%.2f")

    # # Display the entered income with a default value
    # st.write("Pendapatan Isi Rumah: RM {:.2f}".format(user_input_hh_income))

 
     # Numeric coefficients
    # coefficient_bil_air = 0.100
    # coefficient_bil_kanak2 = -0.0051
    # coefficient_bil_wargaEmas = -0.033
    # coefficient_bil_oku = -0.090 
    # coefficient_hh_income = 0.0000370972249842198
    
    # # Declare coefficient
    # coefficient_bil_ir = item_coeff_dict.get('Bil IR', default_feature)
    # coefficient_kanak2 = item_coeff_dict.get('Bil Kanak-kanak', default_feature)
    # coefficient_warga_emas = item_coeff_dict.get('Bil Warga Emas', default_feature)
    # coefficient_oku = item_coeff_dict.get('Bil OKU', default_feature)
    # coefficient_hh_income = item_coeff_dict.get('HH_Income', default_feature)
    # constant_term = item_coeff_dict.get('Constant', default_feature)
    
    # # Declare coefficient with 12 decimal points
    coefficient_bil_ir = round(item_coeff_dict.get('Bil IR', default_feature), 12)
    coefficient_kanak2 = round(item_coeff_dict.get('Bil Kanak-kanak', default_feature), 12)
    coefficient_warga_emas = round(item_coeff_dict.get('Bil Warga Emas', default_feature), 12)
    coefficient_oku = round(item_coeff_dict.get('Bil OKU', default_feature), 12)
    coefficient_hh_income = round(item_coeff_dict.get('HH_Income', default_feature), 12)
    constant_term = round(item_coeff_dict.get('Constant', default_feature), 12)
    

    
   # Get user input for an integer
    user_input_bil_air = st.number_input("Bilangan Isi Rumah:", value=0, step=1, min_value=0)
    coefficient_bil_ir= coefficient_bil_ir * user_input_bil_air
    # st.write("Coefficient for Bil IR:", round(coefficient_bil_ir, 12))
    
    user_input_bil_oku = st.number_input("Bilangan OKU:", value=0, step=1, min_value=0, max_value=user_input_bil_air)
    coefficient_oku= coefficient_oku * user_input_bil_oku
    # st.write("Coefficient for Bil OKU:", round(coefficient_oku, 12))

    user_input_bil_wargaEmas = st.number_input("Bilangan Warga Emas:", value=0, step=1, min_value=0, max_value=user_input_bil_air - user_input_bil_oku)
    coefficient_warga_emas= coefficient_warga_emas * user_input_bil_wargaEmas
    # st.write("Coefficient for Bil Warga Emas:", round(coefficient_warga_emas, 12))

    user_input_bil_kanak2 = st.number_input("Bilangan Kanak-Kanak:", value=0, step=1, min_value=0, max_value=user_input_bil_air - user_input_bil_oku - user_input_bil_wargaEmas)
    coefficient_kanak2= coefficient_kanak2 * user_input_bil_kanak2
    # st.write("Coefficient for Bil Kanak-kanak:", round(coefficient_kanak2, 12))

    user_input_hh_income = st.number_input("Pendapatan Isi Rumah:", value=0.0, step=0.01, format="%.2f", min_value=0.0)
    # Calculate the natural logarithm (ln) of the user input
    ln_user_input_hh_income = np.log(user_input_hh_income) if user_input_hh_income > 0 else 0.0
    ln_coefficient_hh_income = coefficient_hh_income * ln_user_input_hh_income
    # coefficient_hh_income= coefficient_hh_income * user_input_hh_income
    # st.write("User Input for LN Household Income:", round(ln_user_input_hh_income, 12))
    # st.write("Coefficient for LN Household Income:", round(ln_coefficient_hh_income, 12))

    # Coefficients for the selected features
    coefficient_daerah = item_coeff_dict.get(selected_daerah, default_feature)
    coefficient_strata = item_coeff_dict.get(selected_strata, default_feature)
    coefficient_jantina = item_coeff_dict.get(selected_jantina, default_feature)
    coefficient_etnik = item_coeff_dict.get(selected_etnik, default_feature)
    

    # Calculate the regression formula
    sum_coefficient = (
        round(constant_term ,12)+
        round(coefficient_daerah,12) + round(coefficient_strata,12) + round(coefficient_jantina, 12) + round(coefficient_etnik, 12) + 
        round(coefficient_bil_ir, 12)+ round(coefficient_oku, 12) + round(coefficient_warga_emas, 12) + round(coefficient_kanak2, 12) +
        round(ln_coefficient_hh_income, 12)
    )
    
    # Display the Coefficient CONSTANT
    # st.write("Coefficient Constant", round(constant_term, 12))
    
    # Display the calculated regression formula
    # st.write("Sum of Coefficient:", round(sum_coefficient, 12))
    
    # Exponentiate the coefficient
    exp_selected_coefficient = np.exp(round(sum_coefficient, 12))
    # st.write("Sum :", round(exp_selected_coefficient, 12))
    
    # Display the exponentiated coefficient for the selected_daerah
    st.write(f"Predicted Expenditure for Household (RM): {round(exp_selected_coefficient, 2)}")
    
    # Calculate e raised to the power of sum_coefficient
    result = math.exp(sum_coefficient)

    # Display the result with 12 decimal points
    formatted_result = round(result, 12)
    # st.write(f"e^{sum_coefficient} = {formatted_result}")

    
def footer():
    # Footer with copyright
    st.markdown(
        """
        <div style="text-align:center; padding: 10px;">
            <p style="font-size: 12px; color: grey;">Copyright © 2024 Michael/Khairul. All rights reserved.</p>
            <p style="font-size: 12px; color: grey;">bank in dulu</p>
        </div>
        """,
        unsafe_allow_html=True
    )
