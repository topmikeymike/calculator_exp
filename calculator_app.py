import streamlit as st
import pandas as pd
import numpy as np
import math


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def header(selected_language):
    if selected_language == "English":
        logo_image2 = "images/logo2.png" # Replace with the actual path to your logo image
        logo_image = "images/logo.png" # Replace with the actual path to your logo image
        logo_image1 = "images/logo1.png" # Replace with the actual path to your logo image
        
        # Create three columns for each image
        col1, col2, col3 = st.columns(3)

        # Display the logo images in horizontal order
        col1.image(logo_image2, width=100)
        col2.image(logo_image, width=150)
        col3.image(logo_image1, width=150)
    
        # Display the logo image
        # st.image(logo_image2, width=100)
        # st.image(logo_image, width=100)
        # st.image(logo_image1, width=100)
        st.header("Expenditure Calculator 🌟")
        st.markdown(
            """
            <div style="text-align: justify; font-size: 20px; line-height: 1.6; color: #444;">
                <p>Wondering how your monthly expenses should look?</p>
                <p>Now, you can find out the value of your expenses with <b>4 steps.</b></p>
                <p style="font-weight: bold;">Let our Artificial Intelligence (AI) model calculate your expenses based on your inputs.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        logo_image2 = "images/logo2.png" # Replace with the actual path to your logo image
        logo_image = "images/logo.png" # Replace with the actual path to your logo image
        logo_image1 = "images/logo1.png" # Replace with the actual path to your logo image
        
        # Create three columns for each image
        col1, col2, col3 = st.columns(3)

        # Display the logo images in horizontal order
        col1.image(logo_image2, width=100)
        col2.image(logo_image, width=150)
        col3.image(logo_image1, width=150)
    
        st.header("Kalkulator Perbelanjaan 🌟")
        st.markdown(
            """
            <div style="text-align: justify; font-size: 20px; line-height: 1.6; color: #444;">
                <p>Tertanya-tanya berapakah sepatutnya perbelanjaan bulanan anda?</p>
                <p>Kini, anda boleh mengetahui nilai perbelanjaan anda dengan <b>4 Langkah</b> sahaja.</p>
                <p style="font-weight: bold;">Kalkulator ini akan mengira perbelanjaan anda berdasarkan maklumat yang anda berikan dengan penggunaan model <i>Artificial Intelligence (AI)</i> kami.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

def select_language():
    selected_language = st.radio("Select Language", ["English", "Malay"], format_func=str)

    # Apply custom CSS to move the radio button to the right
    st.markdown(
        """
        <style>
        .css-2trqyj {
            justify-content: flex-end;
            display: flex-end;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    return selected_language


def get_language_dict(selected_language):
    if selected_language == "English":
        language = {
            "select_negeri": "State",
            "select_daerah": "District",
            "select_strata": "Strata",
            "select_jantina": "Sex",
            "select_etnik": "Ethnic",
            "input_bil_air": "Members of Households:",
            "input_bil_oku": "Number of Persons With Disabilities (PWD):",
            "input_bil_wargaEmas": "Number of Senior Citizens (Age = 60 above):",
            "input_bil_kanak2": "Number of Children (Age = 17 below):",
            "input_hh_income": "Household Gross Income:",
            "predicted_expenditure": "Predicted Expenditure for Household (RM):",
            "percentage": "Percentage of Predicted Expenditure over Income:", 
            "step_1": "Step 1: Your Location",
            "detail_step1": "Select the state you are currently residing in and whether it is in an urban or rural area",
            "step_2": "Step 2: Head of Household Information",
            "detail_step2": "Select your Gender and Ethnicity",
            "step_3": "Step 3: Your Household Gross Income",
            "detail_step3": "Enter your total gross monthly income of all your household members. This includes income from rent, investments or other transfers.",
            "step_4": "Step 4: Your Household Information",
            "detail_step4": "Enter your number of household as well as the number of elderly people, the number of children, and the number of disabled people.",
            "footer": "Copyright © 2024 Team Usecase. All rights reserved",
            "footer2": "Copyright © 2024 Michael/Khairul. All rights reserved",
            "sumber": "Source:",
            "source": "Department of Statistics Malaysia, Household Income and Expenditure Survey (HIES) 2022",
            "Bandar": "Urban",
            "Luar bandar": "Rural",
            "Lelaki": "Male",
            "Perempuan": "Female",
            "Melayu": "Malay",
            "Cina": "Chinese",
            "India": "Indian",
            "Lain-lain": "Others"
        }
    else:
        # Default to Malay if language is not English
        language = {
            "select_negeri": "Negeri",
            "select_daerah": "Daerah",
            "select_strata": "Strata",
            "select_jantina": "Jantina",
            "select_etnik": "Etnik",
            "input_bil_air": "Bilangan Ahli Isi Rumah:",
            "input_bil_oku": "Bilangan Orang Kurang Upaya (OKU):",
            "input_bil_wargaEmas": "Bilangan Warga Emas (Umur = 60 Ke atas):",
            "input_bil_kanak2": "Bilangan Kanak-Kanak (Umur = 17 Ke bawah):",
            "input_hh_income": "Pendapatan Kasar Isi Rumah:",
            "predicted_expenditure": "Perbelanjaan Yang Dijangkakan untuk Isi Rumah Anda ialah:",
            "percentage": "Peratusan Perbelanjaan Jangkaan terhadap Pendapatan:", 
            "step_1": "Langkah 1: Lokasi Anda",
            "detail_step1": "Sila pilih Daerah tempat tinggal anda dan sama ada Bandar atau Luar Bandar.",
            "step_2": "Langkah 2: Maklumat Ketua Isi Rumah",
            "detail_step2": "Sila pilih Jantina dan Etnik Anda.", 
            "step_3": "Langkah 3: Pendapatan Kasar Isi Rumah Anda",
            "detail_step3": "Sila masukkan jumlah pendapatan kasar bulanan semua ahli isi rumah anda. Ini termasuk pendapatan daripada sewa, pelaburan atau pindahan lain.", 
            "step_4": "Langkah 4: Maklumat Isi Rumah Anda",
            "detail_step4": "Sila masukkan bilangan isi rumah Anda serta bilangan warga emas, bilangan kanak-kanak, dan bilangan OKU.",
            "footer": "Hakcipta © 2024 Team Usecase. Hakcipta terpelihara",
            "footer2": "Hakcipta © 2024 Michael/Khairul. Hakcipta terpelihara",
            "sumber": "Sumber:",
            "source": "Jabatan Perangkaan Malaysia, Survei Pendapatan dan Perbelanjaan Isi Rumah (HIES) 2022",
            "Bandar": "Bandar",
            "Luar bandar": "Luar bandar",
            "Lelaki": "Lelaki",
            "Perempuan": "Perempuan",
            "Melayu": "Melayu",
            "Cina": "Cina",
            "India": "India",
            "Lain-lain": "Lain-lain"
         }
    
    return language



def main_content(language_dict):
    

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
    st.header(language_dict["step_1"])
    st.write(language_dict["detail_step1"])
    selected_negeri = st.selectbox(language_dict["select_negeri"], ["Selangor"] + list(data_negeri_daerah['NEGERI'].unique()))

    # Filter Daerah options based on selected Negeri
    daerah_options = list(data_negeri_daerah[data_negeri_daerah['NEGERI'] == selected_negeri]['DAERAH'].unique())
    selected_daerah = st.selectbox(language_dict["select_daerah"], [""] + daerah_options)

    # daerah_coeff_dict = dict(zip(daerah_list, coefficients))
    item_coeff_dict = dict(zip(data_model['Item'], data_model['Coefficient']))
    data_model['Coefficient'] = round(data_model['Coefficient'], 12)

    # Set default selected coefficient
    selected_coefficient = default_feature

    # Check if selected Negeri and Daerah are W.P. KUALA LUMPUR or W.P. PUTRAJAYA
    if selected_negeri in ["W.P. KUALA LUMPUR", "W.P. PUTRAJAYA"] and selected_daerah in ["W.P. KUALA LUMPUR", "W.P. PUTRAJAYA"]:
        # Display the options in a single-select dropdown for Strata restricted to "Bandar"
        #selected_strata = st.selectbox(language_dict["select_strata"],[language_dict["Bandar"] if selected_language == "Malay" else "Urban"], index=0, key="strata_dropdown", disabled=True)    
        #selected_strata = st.selectbox(language_dict["select_strata"], [language_dict["Bandar"] if language_dict["select_strata"] == "Pilih Strata" else "Urban"], index=0, key="strata_dropdown", disabled=True)
        selected_strata = st.selectbox(language_dict["select_strata"], [language_dict["Bandar"]])
        # Use the selected Daerah to get its coefficient if it's "Bandar"
        #if selected_strata == "Bandar":
        if selected_strata == language_dict["Bandar"]:
            selected_coefficient = default_feature

    else:
        # Display the options in a single-select dropdown for Strata with all available options
        selected_strata = st.selectbox(language_dict["select_strata"], [language_dict["Bandar"], language_dict["Luar bandar"]] )
        
        # Use the selected Daerah to get its coefficient
        selected_coefficient = item_coeff_dict.get(selected_strata, default_feature)

    # Display the coefficient for the selected Daerah
    # st.write(f"Coefficient for {selected_strata}: {round(selected_coefficient, 12)}") 
    
    ############################################################################################################
    
    # # Check if selected Negeri and Daerah are W.P. KUALA LUMPUR or W.P. PUTRAJAYA
    # if selected_negeri in ["W.P. KUALA LUMPUR", "W.P. PUTRAJAYA"] and selected_daerah in ["W.P. KUALA LUMPUR", "W.P. PUTRAJAYA"]:
    #     # Display the options in a single-select dropdown for Strata restricted to "Bandar"
    #     selected_strata = st.selectbox(language_dict["select_strata"], ["Bandar"])
        

    #     # Use the selected Daerah to get its coefficient if it's "Bandar"
    #     if selected_strata == "Bandar":
    #         selected_coefficient = item_coeff_dict.get(selected_strata, default_feature)

    # else:
    #     # Display the options in a single-select dropdown for Strata with all available options
    #     selected_strata = st.selectbox(language_dict["select_strata"], ["Bandar"] + list(data_negeri_daerah['STRATA'].dropna().unique()))
        
    #     # Use the selected Daerah to get its coefficient
    #     selected_coefficient = item_coeff_dict.get(selected_strata, default_feature)

    # # Display the coefficient for the selected Daerah
    # st.write(f"Coefficient for {selected_strata}: {round(selected_coefficient, 12)}") 

        
    st.markdown("<br>", unsafe_allow_html=True)
        
    st.header(language_dict["step_2"])
    st.write(language_dict["detail_step2"])
    
    # Display the options in a single-select dropdown for Jantina
    selected_jantina = st.selectbox(language_dict["select_jantina"], [language_dict["Lelaki"], language_dict["Perempuan"]] )

    # Handle Lelaki and Perempuan as special cases
    if selected_jantina == language_dict["Lelaki"]:
        # Set all feature values to 0 for Lelaki and Perempuan
        selected_coefficient = default_feature
    else:
        # Use the selected Jantina to get its coefficient
        selected_coefficient = item_coeff_dict.get(selected_jantina, default_feature)

    # Display the coefficient for the selected Jantina
    # st.write(f"Coefficient for {selected_jantina}: {round(selected_coefficient, 12)}")

    ###################################################################################
    
    # # Display the options in a single-select dropdown for Jantina
    # selected_jantina = st.selectbox(language_dict["select_jantina"], ["Lelaki"] + list(data_negeri_daerah['JANTINA'].dropna().unique()))
    
    # # Handle Bandar as a special case
    # if selected_jantina == "Lelaki":
    #     # Set all feature values to 0 for Bandar
    #     selected_coefficient = default_feature
    # else:
    #     # Use the selected Daerah to get its coefficient
    #     selected_coefficient = item_coeff_dict.get(selected_jantina, default_feature)

    # # Display the coefficient for the selected Daerah
    # # st.write(f"Coefficient for {selected_jantina}: {round(selected_coefficient, 12)}") 
    
    # Display the options in a single-select dropdown for Etnik
    selected_etnik = st.selectbox(language_dict["select_etnik"], [language_dict["Melayu"], language_dict["Cina"], language_dict["India"], language_dict["Lain-lain"]] )

    # Handle special case for Melayu
    if selected_etnik == language_dict["Melayu"]:
        # Set selected_coefficient to default_feature for Melayu
        selected_coefficient = default_feature
    else:
        # Use the selected Etnik to get its coefficient
        selected_coefficient = item_coeff_dict.get(selected_etnik, default_feature)

    # Display the coefficient for the selected Etnik
    # st.write(f"Coefficient for {selected_etnik}: {round(selected_coefficient, 12)}")

    
    #####################################################################################
    
    # # Display the options in a single-select dropdown for Etnik
    # selected_etnik = st.selectbox(language_dict["select_etnik"], ["Melayu"] + list(data_negeri_daerah['KUMP_ETNIK'].dropna().unique()))
    
    # # Handle Bandar as a special case
    # if selected_etnik == "Melayu":
    #     # Set all feature values to 0 for Bandar
    #     selected_coefficient = default_feature
    # else:
    #     # Use the selected Daerah to get its coefficient
    #     selected_coefficient = item_coeff_dict.get(selected_etnik, default_feature)

    # # Display the coefficient for the selected Daerah
    # # st.write(f"Coefficient for {selected_etnik}: {round(selected_coefficient, 12)}") 
    
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    #declare coefficient hhincome
    coefficient_hh_income = round(item_coeff_dict.get('HH_Income', default_feature), 12)
    
    st.header(language_dict["step_3"])
    st.write(language_dict["detail_step3"])
    user_input_hh_income = st.number_input(language_dict["input_hh_income"], value=0.0, step=0.01, format="%.2f", min_value=0.0, max_value=999999.0)
    ln_user_input_hh_income = np.log(user_input_hh_income) if user_input_hh_income > 0 else 0.0
    ln_coefficient_hh_income = coefficient_hh_income * ln_user_input_hh_income
    # coefficient_hh_income= coefficient_hh_income * user_input_hh_income
    # st.write("User Input for LN Household Income:", round(ln_user_input_hh_income, 12))
    # st.write("Coefficient for LN Household Income:", round(ln_coefficient_hh_income, 12))
    st.markdown("<br>", unsafe_allow_html=True)
    
    
    st.header(language_dict["step_4"])
    st.write(language_dict["detail_step4"])
    # Declare coefficient with 12 decimal points
    coefficient_bil_ir = round(item_coeff_dict.get('Bil IR', default_feature), 12)
    coefficient_kanak2 = round(item_coeff_dict.get('Bil Kanak-kanak', default_feature), 12)
    coefficient_warga_emas = round(item_coeff_dict.get('Bil Warga Emas', default_feature), 12)
    coefficient_oku = round(item_coeff_dict.get('Bil OKU', default_feature), 12)
    constant_term = round(item_coeff_dict.get('Constant', default_feature), 12)
    
   # Get user input for an integer
    user_input_bil_air = st.number_input(language_dict["input_bil_air"], value=0, step=1, min_value=0)
    coefficient_bil_ir= coefficient_bil_ir * user_input_bil_air
    # st.write("Coefficient for Bil IR:", round(coefficient_bil_ir, 12))
    
    user_input_bil_wargaEmas = st.number_input(language_dict["input_bil_wargaEmas"], value=0, step=1, min_value=0, max_value=user_input_bil_air )
    coefficient_warga_emas= coefficient_warga_emas * user_input_bil_wargaEmas
    # st.write("Coefficient for Bil Warga Emas:", round(coefficient_warga_emas, 12))

    user_input_bil_kanak2 = st.number_input(language_dict["input_bil_kanak2"], value=0, step=1, min_value=0, max_value=user_input_bil_air - user_input_bil_wargaEmas)
    coefficient_kanak2= coefficient_kanak2 * user_input_bil_kanak2
    # st.write("Coefficient for Bil Kanak-kanak:", round(coefficient_kanak2, 12))
    
    user_input_bil_oku = st.number_input(language_dict["input_bil_oku"], value=0, step=1, min_value=0, max_value=user_input_bil_air)
    coefficient_oku= coefficient_oku * user_input_bil_oku
    # st.write("Coefficient for Bil OKU:", round(coefficient_oku, 12))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
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

    # Calculate the percentage of predicted expenditure over income
    percentage_predicted_over_income = (exp_selected_coefficient / user_input_hh_income) * 100

    # Display the exponentiated coefficient for the selected_daerah
    if ln_coefficient_hh_income == 0:
        st.write(
            f"""
            <p style='font-size: 20px; font-weight: bold;'>{language_dict['predicted_expenditure']}</p>
            <p style='font-size: 24px; font-weight: bold; color: darkblue;'>NA</p>
            <p style='font-size: 20px; font-weight: bold;'>{language_dict['percentage']}</p>
            <p style='font-size: 24px; font-weight: bold; color: darkblue;'>NA</p>
            """,
            unsafe_allow_html=True
        )
    else:
        st.write(
            f"""
            <p style='font-size: 20px; font-weight: bold;'>{language_dict['predicted_expenditure']}</p>
            <p style='font-size: 24px; font-weight: bold; color: darkblue;'>RM {round(exp_selected_coefficient, 2)}</p>
            <p style='font-size: 20px; font-weight: bold;'>{language_dict['percentage']}</p>
            <p style='font-size: 24px; font-weight: bold; color: darkblue;'> {round(percentage_predicted_over_income, 2)}%</p>
            """,
            unsafe_allow_html=True
        )

    
    st.markdown(
        f"""
        <div style="text-align:left;">
            <p style="font-size: 12px; color: grey;">{language_dict['sumber']} {language_dict['source']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Calculate e raised to the power of sum_coefficient
    result = math.exp(sum_coefficient)

    # Display the result with 12 decimal points
    formatted_result = round(result, 12)
    # st.write(f"e^{sum_coefficient} = {formatted_result}")

    
def footer(language_dict):
    st.markdown(
        f"""
        <div style="text-align:center; padding: 10px;">
        <p style="font-size: 12px; color: grey;">{language_dict['footer']}</p>
        <style>
            .footer-text {{
                font-size: 12px;
                color: transparent;
            }}
            .footer-text:hover {{
                color: grey;
            }}
        </style>
        <p class="footer-text">{language_dict['footer2']}</p>
            <p style="font-size: 12px; color: grey;">Ver.1.0</p>
        </div>
        """,
        unsafe_allow_html=True
    )
