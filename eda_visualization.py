{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f7d44d12-74eb-414e-9d08-bc48c7eaafe9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-17 14:21:10.032 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-17 14:21:10.033 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-17 14:21:10.035 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-17 14:21:10.035 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-17 14:21:10.036 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-17 14:21:10.038 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-17 14:21:10.039 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "# eda_visualization.py\n",
    "\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Title\n",
    "st.title(\"📊 Exploratory Data Analysis (EDA) Dashboard\")\n",
    "\n",
    "# File Upload\n",
    "uploaded_file = st.file_uploader(\"📁 Upload your CSV file\", type=[\"csv\"])\n",
    "\n",
    "if uploaded_file is not None:\n",
    "    df = pd.read_csv(uploaded_file)\n",
    "    \n",
    "    st.subheader(\"📝 Dataset Preview\")\n",
    "    st.dataframe(df.head())\n",
    "\n",
    "    st.subheader(\"🔍 Basic Info\")\n",
    "    st.write(\"Shape of dataset:\", df.shape)\n",
    "    st.write(\"Data types:\", df.dtypes)\n",
    "    st.write(\"Missing values:\", df.isnull().sum())\n",
    "\n",
    "    st.subheader(\"📈 Numerical Summary\")\n",
    "    st.write(df.describe())\n",
    "\n",
    "    st.subheader(\"📊 Correlation Heatmap\")\n",
    "    corr = df.corr(numeric_only=True)\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.heatmap(corr, annot=True, cmap=\"coolwarm\", ax=ax)\n",
    "    st.pyplot(fig)\n",
    "\n",
    "    st.subheader(\"📉 Value Counts for Categorical Columns\")\n",
    "    cat_cols = df.select_dtypes(include='object').columns\n",
    "    for col in cat_cols:\n",
    "        st.write(f\"📌 {col} value counts:\")\n",
    "        st.bar_chart(df[col].value_counts())\n",
    "\n",
    "    st.subheader(\"📌 Box Plot\")\n",
    "    num_col = st.selectbox(\"Select numeric column for boxplot\", df.select_dtypes(include='number').columns)\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.boxplot(x=df[num_col], ax=ax)\n",
    "    st.pyplot(fig)\n",
    "    st.subheader(\"📊 Histogram (Distribution Plot)\")\n",
    "    hist_col = st.selectbox(\"Select numeric column for histogram\", df.select_dtypes(include='number').columns)\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.histplot(df[hist_col], kde=True, ax=ax, bins=30, color='skyblue')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "    st.subheader(\"🟢 Pie Chart for Categorical Data\")\n",
    "\n",
    "    if len(cat_cols) > 0:\n",
    "        pie_col = st.selectbox(\"Select categorical column for pie chart\", cat_cols)\n",
    "        if pie_col:\n",
    "            pie_data = df[pie_col].value_counts()\n",
    "            fig, ax = plt.subplots()\n",
    "            ax.pie(pie_data.values, labels=pie_data.index, autopct='%1.1f%%', startangle=90)\n",
    "            ax.axis('equal')\n",
    "            st.pyplot(fig)\n",
    "    else:\n",
    "        st.warning(\"No categorical columns found in the dataset.\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "706baa48-8550-4ee4-80a1-78384ae623cf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
