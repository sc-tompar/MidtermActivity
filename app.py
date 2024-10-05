import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sheeshable Guys - Data Exploration Report", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #f4f7fc;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #333333;
        text-align: center;
    }
    p, li {
        color: #444444;
        font-size: 18px;
        line-height: 1.6;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #3498db, #8e44ad);
        color: white;
    }
    .stButton>button {
        background-color: #3E5C76;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        padding: 10px 20px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #6C8BB5;
    }
    .stImage>img {
        border: 2px solid #3498db;
        border-radius: 10px;
    }
    .metric-box {
        background: linear-gradient(120deg, #3498db, #8e44ad);
        border-radius: 10px;
        padding: 20px;
        margin: 20px;
        color: white;
        font-size: 24px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("🚀 Sheeshable Guys - Data Exploration Report")
page = st.sidebar.radio("Navigate to:", ["Introduction", "Visualizations", "Conclusion"])

if page == "Introduction":
    st.title("💼 Data Exploration Report: Adult Income Dataset")
    st.header("📊 Introduction")
    st.write("""
    The **Adult Income Dataset** is sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/adult).
    This dataset compiles census data aimed at predicting whether an individual earns over $50,000 a year based on various demographic and employment variables.
    
    The dataset consists of 32,561 entries with 15 attributes (features), ranging from age and education to working hours and occupation, along with one target variable (income).
    
    This report is prepared by the **Sheeshable Guys** team and aims to explore key factors that influence income levels among adults.
    """)

    st.subheader("🎓 Prepared By:")
    st.markdown("""
    - **Steve Laurenz Villas**
    - **Trisan Jae Españo**
    - **Simoun Cloyd Tompar**
    - **Kade Sanico**
    - **Chris Marklen Fernandez**
    """)

    st.write("""
    ### 🎯 Purpose of Exploration:
    - Understand the demographic characteristics of individuals based on income.
    - Analyze the relationships between age, education, work hours, and income.
    - Identify key factors influencing higher income.
    """)

    with st.expander("See Why This Dataset is Important 🔍"):
        st.write("""
        This dataset is crucial for understanding the socio-economic patterns in the workforce. It helps identify key factors that affect income inequality and can serve as a foundation for making policy recommendations to bridge the income gap.
        """)

elif page == "Visualizations":
    st.title("📊 Visualizations of Key Insights")
    st.write("### 📈 Distribution Analysis")

    st.write("#### Key Statistics at a Glance")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Average Age", "38.5 years")
    col2.metric("Hours per Week", "40.44 hours")
    col3.metric("Education Level", "10 years")
    col4.metric("Income Proportion", "24% > $50K")

    st.subheader("1. Histograms of Numeric Features with Mean Annotations")
    st.image("histograms_image.png", caption="Histograms of Numeric Features with Mean Annotations", use_column_width=True)

    st.subheader("2. Boxplot of Numeric Features (Excluding Capital-Gain and Capital-Loss)")
    st.image("boxplot_numeric.png", caption="Boxplot of Numeric Features (Excluding Capital-Gain and Capital-Loss)", use_column_width=True)

    st.subheader("3. Boxplot of Capital-Gain and Capital-Loss")
    st.image("boxplot_capital.png", caption="Boxplot of Capital-Gain and Capital-Loss", use_column_width=True)

elif page == "Conclusion":
    st.title("🔍 Conclusion and Takeaways")
    st.write("""
    ### 🏁 Key Insights from the Data Exploration:
    
    - **Age**: The average age of individuals is around 38.5 years, with a majority falling within the range of 28 to 48 years.
    
    - **Income**: Only about 24% of the individuals earn more than $50,000 annually, indicating income disparity.
    
    - **Education**: The average education level is around 10 years, which aligns closely with a high school education.
    
    - **Work Hours**: Most individuals work a standard 40-hour work week, indicating typical full-time job schedules.
    
    - **Capital Gains/Losses**: The majority of individuals have zero capital gains or losses, with a small number of significant outliers.
    
    ### 🔍 Future Recommendations:
    
    1. Focus on analyzing the relationship between occupation and income.
    2. Explore the impact of marital status and education on income levels.
    3. Consider creating predictive models to understand income mobility.

    Thank you for exploring the Adult Income Dataset!
    """)

    st.balloons()
    st.markdown("""
    ### 🎉 Thank you for reviewing our report!
    """)