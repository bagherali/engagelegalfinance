
import streamlit as st

# Set up the webpage
st.set_page_config(page_title="Legal Funding Application", layout="wide")

# Header Section
st.image("https://www.highriselegalfunding.com/wp-content/uploads/2021/07/High-Rise-Legal-Funding-Logo.svg", width=250)
st.title("Apply for Legal Funding Today")
st.write("Get pre-settlement funding quickly and easily.")

# Form
with st.form(key="funding_form"):
    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    case_type = st.selectbox("Type of Case", ["Personal Injury", "Car Accident", "Medical Malpractice", "Other"])
    loan_amount = st.text_input("Requested Loan Amount ($)")
    
    submit_button = st.form_submit_button("Apply Now")

# Form submission handling
if submit_button:
    if full_name and email and phone and loan_amount:
        st.success(f"Thank you {full_name}, your application has been submitted!")
    else:
        st.error("Please fill out all required fields.")

# Contact Info
st.markdown("### Need help? Call us at **(888) 888-8888** or email **support@legalfunding.com**")
