import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
        'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
        'hours-per-week', 'native-country', 'income'
    ]
    data = pd.read_csv(url, names=column_names, na_values=' ?', skipinitialspace=True)
    data.dropna(inplace=True)
    data['income'] = data['income'].str.strip()
    return data

st.set_page_config(page_title="Sheeshable Guys - Data Exploration Report", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #f4f7fc;
    }
    h1, h2, h3, h4, h5, h6 {
        color: white;
        text-align: center;
    }
    p, li {
        color: white;
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

data = load_data()

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
    st.write("### 📈 Histograms and Boxplots")

    st.subheader("1. Age Distribution")
    st.write("The majority of individuals are between 20 and 50 years old, peaking around 30-40. The red dashed line indicates a mean age of 38.58.")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))  # Side-by-side plots
    sns.histplot(data['age'], kde=False, color='skyblue', ax=ax1)
    ax1.axvline(data['age'].mean(), color='red', linestyle='--', label=f'Mean Age: {data["age"].mean():.2f}')
    ax1.legend()
    sns.boxplot(x=data['age'], color='skyblue', ax=ax2)
    ax2.axvline(data['age'].mean(), color='red', linestyle='--', label=f'Mean: {data["age"].mean():.2f}')
    ax2.legend()
    st.pyplot(fig)

    st.subheader("2. Education-Num Distribution")
    st.write("Represents the years of education completed. Most people have around 10 years of education, with secondary spikes at 13-14 years, indicating high school and college-level education. The mean education number is 10.08.")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    sns.histplot(data['education-num'], kde=False, color='lightgreen', ax=ax1)
    ax1.axvline(data['education-num'].mean(), color='red', linestyle='--', label=f'Mean: {data["education-num"].mean():.2f}')
    ax1.legend()
    sns.boxplot(x=data['education-num'], color='lightgreen', ax=ax2)
    ax2.axvline(data['education-num'].mean(), color='red', linestyle='--', label=f'Mean: {data["education-num"].mean():.2f}')
    ax2.legend()
    st.pyplot(fig)

    st.subheader("3. Capital-Gain Distribution")
    st.write("Most values are zero, indicating that a large proportion of individuals do not have additional capital gains. The mean value is skewed to 1077.65 due to a few high outliers.")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    sns.histplot(data['capital-gain'], kde=False, color='lightcoral', ax=ax1)
    ax1.axvline(data['capital-gain'].mean(), color='red', linestyle='--', label=f'Mean: {data["capital-gain"].mean():.2f}')
    ax1.legend()
    sns.boxplot(x=data['capital-gain'], color='lightcoral', ax=ax2)
    ax2.axvline(data['capital-gain'].mean(), color='red', linestyle='--', label=f'Mean: {data["capital-gain"].mean():.2f}')
    ax2.legend()
    st.pyplot(fig)

    st.subheader("4. Capital-Loss Distribution")
    st.write("Similar to capital gain, the majority of individuals have zero capital loss, with a small number having significant losses. The mean value is 87.30.")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    sns.histplot(data['capital-loss'], kde=False, color='gold', ax=ax1)
    ax1.axvline(data['capital-loss'].mean(), color='red', linestyle='--', label=f'Mean: {data["capital-loss"].mean():.2f}')
    ax1.legend()
    sns.boxplot(x=data['capital-loss'], color='gold', ax=ax2)
    ax2.axvline(data['capital-loss'].mean(), color='red', linestyle='--', label=f'Mean: {data["capital-loss"].mean():.2f}')
    ax2.legend()
    st.pyplot(fig)

    st.subheader("5. Hours-per-Week Distribution")
    st.write("Most individuals work a standard 40-hour week, with the distribution centered around this value. The mean value is 40.44, matching the typical full-time schedule.")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    sns.histplot(data['hours-per-week'], kde=False, color='orange', ax=ax1)
    ax1.axvline(data['hours-per-week'].mean(), color='red', linestyle='--', label=f'Mean: {data["hours-per-week"].mean():.2f}')
    ax1.legend()
    sns.boxplot(x=data['hours-per-week'], color='orange', ax=ax2)
    ax2.axvline(data['hours-per-week'].mean(), color='red', linestyle='--', label=f'Mean: {data["hours-per-week"].mean():.2f}')
    ax2.legend()
    st.pyplot(fig)
    
    st.subheader("6. Income Distribution")
    st.write("Binary distribution indicating 76% of individuals earn <=50K and 24% earn >50K. Text annotations show these proportions clearly, without using a mean line since the variable is categorical.")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.countplot(x='income', data=data, palette='muted', ax=ax)
    ax.set_xticklabels(['<=50K', '>50K'])
    st.pyplot(fig)

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
