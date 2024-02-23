

from pathlib import Path

import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | JOJO VARGHESE"
PAGE_ICON = ":wave:"
NAME = "JOJO VARGHESE"
DESCRIPTION = """
Junior Data Scientist, looking forward to apply analytical skills to real-world problems and learn through
the experience.
"""
EMAIL = "jojo3416jo@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jojo-varghese-datastronaut/",
    "GitHub": "https://github.com/JOCRZ",
    "Medium": "https://medium.com/@jojo3416jo",
    "Hackerrank": "https://www.hackerrank.com/profile/jojo3416jo",
}
PROJECTS = {
    "🏆 Employee Turn Over Prediction - Logistic Regression": "https://employechurnprediction.streamlit.app/",
    "🏆 Recruit Salary Prediction - Linear Regression": "https://recruitsalarypredictor.streamlit.app/",
    "🏆 Iris Flower Classification - Decision Tree": "https://irisclassifications.streamlit.app/",
    "🏆 HR Attrition Analysis Dashboard - Powerbi": "https://mavenanalytics.io/project/12578",
    "🏆 Sales Data Analysis Dashboard - Powerbi": "https://mavenanalytics.io/project/12577",
    "🏆 Walmart Sales Dashboard - LookerStudio": "https://lookerstudio.google.com/reporting/8bd21894-3814-44ac-83b5-ff2d7a454b2e",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS & PDF ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- HERO SECTION ---
st.title(NAME)
st.write(DESCRIPTION)
st.download_button(
    label=" 📄 Download Resume",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
)
st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
-  Programming: Python, SQL
-  Data Science : Pandas, Numpy, Scikit-learn, Keras, Seaborn, Matplotlib
-  Databases: Postgres, MySQL
-  Frame work : Streamlit, Flask
-  WebScrapping : BeautifulSoup
-  Dashboarding : PowerBi, MS Excel, LookerStudio
-  Algorithms : Linear regression, Logistic regression, Decision trees, Random Forest, SVM, KNN
-  Clustering : K-Means
-  Neural Networks : ANN, CNN, RNN
-  Version Control : Git, Git-Hub
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---
st.write("**Data Scientist Intern | The Sparks Foundation**")
st.write("December 2023 - January 2024")
st.write(
    """
- ► The Internship involved completing multiple tasks, including improving my LinkedIn profile,
peer evaluation, and creating a credible resume on mycredible. The project primarily
centered around using a Decision Tree to classify the iris flower. By focusing solely on this
algorithm, I gained in-depth knowledge about its workings.
"""
)

# --- JOB 2 ---
st.write('\n')
st.write("**Data Analyst Intern | Meriskill**")
st.write("October 2023 - Novermber 2023")
st.write(
    """
- ► During the Internship, I completed three projects:
- ► Sales Data Analysis: Explored a large sales dataset, identifying trends, top-selling products,
and revenue metrics. Applied feature engineering to enhance the dataset and created clear
visualizations to convey fndings.
- ► Gestational Diabetes Prediction: Cleaned and prepared data, addressed data imbalance,
and built a predictive model with 77% accuracy. Deployed the model on Streamlit for
accessibility.
- ► HR Attrition Analysis: Conducted EDA, cleaned data, and utilized statistical techniques to
uncover insights into HR dynamics. Developed a dashboard to efectively communicate
fndings to stakeholders.
"""
)

# --- JOB 3 ---
st.write('\n')
st.write("**Data Scientist | British Airways**")
st.write("8 October 2023")
st.write(
    """
- ► Web Scraping and EDA: Task 1 web scraping on British Airways customer reviews using Pandas and BeautifulSoup.
Performed Exploratory Data Analysis (EDA) on the scraped data to extract insights and identify trends.
- ► Data Cleaning and Wrangling: Cleaned and wrangled the scraped data to prepare it for analysis and modeling.
- ► Predictive Modeling: Task 2 Built a predictive model using statistical methods for feature selection and engineering.
- ► Experimented with various Machine Learning (ML) algorithms to find the best-performing one.
- ► Model Evaluation: Evaluated the predictive model's performance, achieving a high accuracy of 0.99.
Assessed the model's precision, indicating a low False Positive Rate of 0.074%.
"""
)
# --- JOB 4 ---
st.write('\n')
st.write("**Data Analyst | Accenture**")
st.write("7 April 2023")
st.write(
    """
- ►Understanding Project Requirements: Collaborate with project teams to comprehend scope, objectives, and deliverables of data analysis projects.
Gain a thorough understanding of client requirements, business processes, and data sources. 
- ►  Data Cleaning and Modeling: Apply data cleaning techniques to ensure data accuracy, consistency, and completeness.
- ► Data Analysis and Insights: Perform in-depth data analysis to identify trends, patterns, and correlations.
- ►  Visualization and Storytelling: Create visually appealing and informative data visualizations using Matplotlib.
Develop compelling narratives to communicate insights effectively using tools like PowerPoint.
- ► Client Presentation: Prepare and deliver presentations to clients, effectively conveying insights derived from data analysis.

"""
)

# --- PROJECTS & ACCOMPLISHMENTS ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
