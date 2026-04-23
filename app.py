import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from groq import Groq

st.set_page_config(page_title="Generative AI Data Analysis with Natural Language Processing", layout="wide")

#  Add your Groq API Key here
client = Groq(api_key="your_api_key")

st.title("Generative AI Data Analysis with Natural Language Processing")
st.write("Upload your dataset and analyze it using charts and AI queries.")

uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:

    # Read file
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    st.subheader("🔍 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📌 Dataset Summary")

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    with st.expander("View Missing Values by Column"):
        st.write(df.isnull().sum())

    st.subheader("📊 Create Visualization")

    columns = df.columns.tolist()
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found.")
        st.stop()

    x_col = st.selectbox("Select X-axis", columns)
    y_col = st.selectbox("Select Y-axis", numeric_cols)
    chart_type = st.selectbox("Chart Type", ["Bar", "Line", "Histogram"])

    st.subheader("📈 Chart Output")

    try:
        if chart_type == "Bar":
            chart_data = df.groupby(x_col)[y_col].sum().reset_index()
            st.bar_chart(chart_data.set_index(x_col))

        elif chart_type == "Line":
            chart_data = df.groupby(x_col)[y_col].sum().reset_index()
            st.line_chart(chart_data.set_index(x_col))

        elif chart_type == "Histogram":
            fig, ax = plt.subplots()
            ax.hist(df[y_col].dropna(), bins=20)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Chart Error: {e}")

    st.subheader("Ask Questions About Your Data")

    user_query = st.text_input("Example: Top 5 products by profit")

    def generate_pandas_code(query, columns):
        prompt = f"""
        You are a data analyst.

        Dataset columns: {columns}

        Convert the user question into pandas code.
        Store final output in a variable named 'result'.

        Only return python code. No explanation.

        DataFrame name is df.

        Example:
        result = df.groupby('Category')['Sales'].sum().sort_values(ascending=False).head(5)

        Question: {query}
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    if user_query:
        try:
            code = generate_pandas_code(user_query, df.columns.tolist())

            st.subheader("🧠 Generated Code")
            st.code(code, language="python")

            local_vars = {"df": df}

            exec(code, {}, local_vars)

            result = local_vars.get("result", None)

            if result is not None:
                st.subheader("📊 Result")
                st.write(result)
            else:
                st.warning("No result returned. Make sure 'result' variable is used.")

        except Exception as e:
            st.error(f"AI Error: {e}")

else:
    st.info(" Upload a dataset to begin.")