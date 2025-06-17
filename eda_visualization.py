import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA Dashboard", layout="wide")
st.title("📊 Exploratory Data Analysis (EDA) Dashboard")

uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📝 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("🔍 Basic Info")
    st.write("Shape of dataset:", df.shape)
    st.write("Data types:")
    st.write(df.dtypes)
    st.write("Missing values:")
    st.write(df.isnull().sum())

    st.subheader("📈 Numerical Summary")
    st.write(df.describe())

    st.subheader("📊 Correlation Heatmap")
    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    st.subheader("📉 Value Counts for Categorical Columns")
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        st.write(f"📌 {col} value counts:")
        st.bar_chart(df[col].value_counts())

    st.subheader("📌 Box Plot")
    num_col = st.selectbox("Select numeric column for boxplot", df.select_dtypes(include='number').columns)
    fig, ax = plt.subplots()
    sns.boxplot(x=df[num_col], ax=ax)
    st.pyplot(fig)

    st.subheader("📊 Histogram (Distribution Plot)")
    hist_col = st.selectbox("Select numeric column for histogram", df.select_dtypes(include='number').columns)
    fig, ax = plt.subplots()
    sns.histplot(df[hist_col], kde=True, ax=ax, bins=30, color='skyblue')
    st.pyplot(fig)

    st.subheader("🟢 Pie Chart for Categorical Data")
    if len(cat_cols) > 0:
        pie_col = st.selectbox("Select categorical column for pie chart", cat_cols)
        if pie_col:
            pie_data = df[pie_col].value_counts()
            fig, ax = plt.subplots()
            ax.pie(pie_data.values, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)
    else:
        st.warning("No categorical columns found in the dataset.")
