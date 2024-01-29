import streamlit as st
from calculator_app import header, main_content, footer, select_language, get_language_dict

def main():
    
    header()
    # Add a line break
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Call select_language to get the selected language
    selected_language = select_language()
    
    # Call get_language_dict with the selected language
    language_dict = get_language_dict(selected_language)
    
    
    main_content(language_dict)
    
    # Add a line break
    st.markdown("<br>", unsafe_allow_html=True)
    
    footer()

if __name__ == "__main__":
    main()
