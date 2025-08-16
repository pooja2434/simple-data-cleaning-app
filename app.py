import streamlit as st
import pandas as pd

st.set_page_config(page_title="Simple Data Cleaning Demo", page_icon="🧹", layout="wide")

st.title("🧹 Simple Data Cleaning Demo")

# Load data
raw_df = pd.read_csv("data/raw_sales.csv")
cleaned_df = pd.read_csv("data/cleaned_sales.csv")

st.subheader("📊 Raw Data (Before Cleaning)")
st.dataframe(raw_df)

st.subheader("✅ Cleaned Data (After Cleaning)")
st.dataframe(cleaned_df)

st.markdown("### 🔍 Cleaning Steps Performed")
st.write("""
1. Removed duplicate rows  
2. Filled missing values in `Sales` column with mean  
3. Converted `Date` column to proper datetime format  
4. Renamed columns for clarity  
""")

# Option to download cleaned file
st.download_button(
    label="📥 Download Cleaned Dataset",
    data=cleaned_df.to_csv(index=False).encode("utf-8"),
    file_name="cleaned_sales.csv",
    mime="text/csv"
)
