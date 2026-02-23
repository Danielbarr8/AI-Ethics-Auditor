import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="AI Ethics Auditor", page_icon="📜")

st.title("📜 AI Ethics & Compliance Auditor")
st.write("Complete the audit below to generate your 2026 Compliance PDF.")

# User Inputs for the Report
project_name = st.text_input("Project Name", placeholder="e.g., Alpha-Llama Internal Bot")
auditor_name = st.text_input("Auditor Name", placeholder="Daniel Barr")
risk_level = st.selectbox("Assessed Risk Level", ["Minimal", "Limited", "High", "Unacceptable"])
findings = st.text_area("Audit Findings", placeholder="Detail the ethics and security checks performed...")

if st.button("Prepare Report"):
    if project_name and auditor_name:
        # Create PDF in memory
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="AI COMPLIANCE AUDIT REPORT", ln=True, align='C')
        
        pdf.set_font("Arial", size=12)
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Project: {project_name}", ln=True)
        pdf.cell(200, 10, txt=f"Auditor: {auditor_name}", ln=True)
        pdf.cell(200, 10, txt=f"Risk Level: {risk_level}", ln=True)
        pdf.ln(5)
        pdf.multi_cell(0, 10, txt=f"Findings: {findings}")
        
        # Output PDF as a string (binary)
        pdf_output = pdf.output(dest='S').encode('latin-1')
        
        st.success("✅ Report Prepared! Click below to download.")
        st.download_button(
            label="Download PDF Report",
            data=pdf_output,
            file_name=f"{project_name}_Audit.pdf",
            mime="application/pdf"
        )
    else:
        st.error("Please fill in the Project and Auditor names.")

st.divider()
st.caption("AI Ethics Framework v2026 | Portfolio by Daniel Barr")