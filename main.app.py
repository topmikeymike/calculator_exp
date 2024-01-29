import streamlit as st
from calculator_app import header, main_content, footer, select_language, get_language_dict

def main():
    
    with st.sidebar:
        # Call select_language to get the selected language
        selected_language = select_language()

        # Call get_language_dict with the selected language
        language_dict = get_language_dict(selected_language)

    header(selected_language)
    
    # Add a line break
    st.markdown("<br>", unsafe_allow_html=True)
    
    main_content(language_dict)
    
    # Add a line break
    st.markdown("<br>", unsafe_allow_html=True)
    
    footer(language_dict)

if __name__ == "__main__":
    main()
