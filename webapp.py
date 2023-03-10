import streamlit as st
import pandas as pd
st.set_page_config(page_title = "Student Class test Score", page_icon=":tada:", layout="wide")

st.subheader("Enter the marks of students")
df = pd.DataFrame(
    [
       {"Name": "Rita", "Test Score": 10}
    ]  
)
edited_df = st.experimental_data_editor(df, num_rows = "dynamic")

student_name = edited_df.loc[edited_df["Test Score"].idxmax()]["Name"]
st.markdown(f"Most number are attained by **{student_name}** 🎈")
