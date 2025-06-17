# eda_visualization.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit_authenticator as stauth

# --- Authentication Setup ---
names = ['Admin', 'Guest']
usernames = ['admin', 'guest']
hashed_passwords = [
    '$pbkdf2-sha256$29000$PbPkNfz9By0xXR1hKmlcZw$W7hDL7MJvScRBGn1J6j7ovCZKAhzYOvGCrQdlmxztpA',  # example hash for 'admin123'
    '$pbkdf2-sha256$29000$PtYDyNTk5BvCibos9wT5Jw$MBlY9kLemNMbQ1Rhcv5AKQaHOGr7VgyLNYzC/N7nD/I'   # example hash for 'guest123'
]

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    'eda_app_cookie',      # Cookie name
    'eda_signature_key',   # Signature key
    cookie_expiry_days=1
)

# --- Login UI ---
name, auth_status, username = authenticator.login('Login', 'main')

if auth_status == False:
    st.error('❌ Incorrect username or password')
elif auth_status is None:
    st.warning('🔐 Please enter your credentials')
elif auth_status:
    # --- Logout & Welcome ---
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.success(f'✅ Logged in as {name}')

    # --- EDA Dashboard ---
    st.title("📊 Exploratory Data Analysis (EDA) Dashboard")

    uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("📝 Dataset Preview")
        st.dataframe(df.head())

        st.subheader("🔍 Basic Info")
        st.write("Shape of dataset:", df.shape)
        st.write("Data types:", df.dtypes)
        st.write("Missing values:", df.isnull().sum())

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
