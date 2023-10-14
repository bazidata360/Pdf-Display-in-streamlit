import streamlit as st
import base64

if st.checkbox("Show Instructions"):
    
        def show_pdf(file_path):
            with open(file_path,"rb") as f:
                  base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
            st.markdown(pdf_display, unsafe_allow_html=True)
        (show_pdf("C:\Users\marba\OneDrive\Desktop\New folder (2)\streamlit_login_auth_ui\NYSE_RBS_2020.pdf"))
