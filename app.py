import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Judul Aplikasi
st.title("Descriptive Statistics")

# Ambil file dari URL jika ada
query_params = st.query_params
file_name = query_params.get("file")

if file_name:
    file_path = os.path.join("uploads", file_name)

    if os.path.exists(file_path):
        # Membaca file CSV
        df = pd.read_csv(file_path)

        # Menampilkan Data
        st.subheader("Uploaded file:")
        st.write(df)

        # Statistik Deskriptif
        st.subheader("Descriptive Statistics:")
        st.write(df.describe())


        # Pilihan Kolom Numerik untuk Visualisasi
        st.subheader("Data Visualization")
        numeric_columns = df.select_dtypes(include=['number']).columns

        if len(numeric_columns) > 0:
            column = st.selectbox("Choose numeric columns:", numeric_columns)

            # Line Plot
            st.subheader("1. Line Plot")
            fig, ax = plt.subplots()
            ax.plot(df[column], linestyle="-", marker="o", color="b")
            st.pyplot(fig)

            # Scatter Plot (jika ada lebih dari 1 kolom numerik)
            if len(numeric_columns) > 1:
                second_column = st.selectbox("Choose second numeric columns for Scatter Plot:", numeric_columns)
                st.subheader("2. Scatter Plot")
                fig, ax = plt.subplots()
                ax.scatter(df[column], df[second_column], alpha=0.5)
                st.pyplot(fig)

            # Boxplot
            st.subheader("3️. Boxplot")
            fig, ax = plt.subplots()
            sns.boxplot(y=df[column], ax=ax)
            st.pyplot(fig)

            # KDE Plot (Estimasi Distribusi)
            st.subheader("4. KDE Plot")
            fig, ax = plt.subplots()
            sns.kdeplot(df[column], fill=True)
            st.pyplot(fig)

            # Histogram
            st.subheader("5. Histogram")
            fig, ax = plt.subplots()
            ax.hist(df[column], bins=20, edgecolor="b")
            st.pyplot(fig)

            # 🔹 **Histogram Populasi vs Sampel**
            st.write("### 6. Population vs Sample Histogram")
            sample_size = st.slider("Select sample size", min_value=1, max_value=len(df), value=int(len(df) * 0.1))
            sample_df = df.sample(sample_size, random_state=42)
        
            selected_col_pop_sample = st.selectbox("Select column for Population vs Sample Histogram", numeric_columns, key="pop_sample")
            fig, ax = plt.subplots()
            sns.histplot(df[selected_col_pop_sample], kde=True, color='blue', label='Population', ax=ax)
            sns.histplot(sample_df[selected_col_pop_sample], kde=True, color='red', label='Sample', ax=ax)
            ax.legend()
            st.pyplot(fig)


        else:
            st.warning("No numeric column found from the dataset.")
    else:
        st.error("File not found.")
else:
    st.warning("File not found.a")
