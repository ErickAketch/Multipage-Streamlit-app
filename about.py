import streamlit as st 
from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("assets/passport.png", width=250)
with col2:
    st.title("Erick Aketch", anchor="False")
    st.write("Data Analyst | Python Developer | Streamlit Enthusiast")

    if st.button("📩 Contact Me"):
        show_contact_form()

# ----- Qualifications -----
st.write("\n")
st.subheader("Qualifications", anchor ="False")
st.write(
    """
    - Degree in Computer Science, Statistics, Mathematics, or related field.
    - Skilled in Python, R, SQL, and data visualization tools (Tableau/Power BI).
    - Strong foundation in statistics, machine learning, and data analysis.
    - Knowledge of big data tools (Spark, Hadoop) and cloud platforms (AWS, Azure, GCP).
    """
)

#------ Experiences -----
st.write("\n")
st.subheader("Experiences", anchor ="False")
st.write(
    """
    - Hands-on experience in data cleaning, analysis, and building predictive models.
    - Worked with large datasets to generate business insights.
    - Experience deploying models into production environments.
    - Communicated findings through reports and visual dashboards.
    - Collaborated with teams on real-world projects across different domains.
    """
)

#------ Skills -----
st.write("\n")
st.subheader("Skills", anchor ="False")
st.write(
    """
    - Programming: Python, R, SQL
    - Data Handling: Data cleaning, preprocessing, wrangling
    - Statistics & Math: Probability, regression, hypothesis testing
    - Machine Learning: Classification, clustering, deep learning, NLP
    - Data Visualization: Tableau, Power BI, Matplotlib, Seaborn
    """
)
