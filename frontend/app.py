import streamlit as st
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

st.title("Extracteur de CV")




st.header("Télécharger et analyser un CV")

uploaded_file = st.file_uploader(
    "Choisissez un fichier CV (PDF ou DOCX)",
    type=["pdf", "docx"]
)

if st.button("Analyze CV"):
    if uploaded_file is None:
        st.error("Veuillez d'abord télécharger un fichier.")
    else:
        with st.spinner("Analyse du CV en cours..."):
            files = {
                "file": (uploaded_file.name, uploaded_file, uploaded_file.type)
            }
            response = requests.post(
                f"{BASE_URL}/api/v1/upload-cv",
                files=files
            )

        if response.status_code == 200:
            st.success("CV analysé avec succès !")
            st.session_state.cv_result = response.json()
        else:
            st.error(response.json().get("detail", "Une erreur s'est produite."))





if "cv_result" in st.session_state:
    st.header("Extracted Information")

    cv = st.session_state.cv_result

    first_name = st.text_input("First name", cv["first_name"])
    last_name = st.text_input("Last name", cv["last_name"])
    email = st.text_input("Email", cv["email"])
    phone = st.text_input("Phone", cv["phone"])
    degree = st.text_input("Degree", cv["degree"])

    updated_cv = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "degree": degree,
    }

    st.download_button(
        label="Download JSON",
        data=json.dumps(updated_cv, indent=2),
        file_name="cv_result.json",
        mime="application/json"
    )
