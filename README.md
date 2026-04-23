# Generative AI Data Analysis with Natural Language Processing

> Upload any dataset. Ask questions in plain English. Get instant insights through charts and tables — powered by Groq, Pandas, and NLP.

---

## 🚀 Overview

**DataTalk** is an end-to-end data analytics tool that lets you explore datasets without writing a single line of code. Simply upload your CSV, choose the visualizations you want, and ask questions like *"Top 5 products by revenue"* — the app translates your query into a Pandas operation and returns a clean, formatted result.

Built as a portfolio project demonstrating practical integration of **Generative AI**, **NLP**, and **data analysis workflows**.

---

## ✨ Features

- 📁 **CSV Upload** — Load any tabular dataset instantly
- 📈 **Auto Visualizations** — Select from bar, line, pie, scatter, and histogram charts generated via Matplotlib
- 💬 **Natural Language Querying** — Type questions in plain English; the app converts them to Pandas queries using the Groq API (LLaMA 3)
- 📋 **Tabular Results** — Query output rendered as a clean, formatted table
- ⚡ **Fast Inference** — Groq's LPU hardware delivers sub-second NLP response times
- 🔍 **EDA Insights** — Automatic summary statistics, null value detection, and data type profiling

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| AI / LLM | Groq API (LLaMA 3 70B) |
| NLP | Custom prompt engineering + output parsing |
| Data Processing | Pandas, NumPy |
| Visualizations | Matplotlib |
| Frontend | Streamlit |

🗂️ Project Structure
datatalk/
│
├── app.py                  # Main application — UI, NLP querying, and chart logic
├── requirements.txt        # Python dependencies
└── README.md

## ⚙️ Setup & Installation

Follow these steps to run the project locally.

1. Clone the Repository and move it to your repo name

2. Create and Activate Virtual Environment
`python -m venv venv`

Activate the environment:

Windows:
`venv\Scripts\activate`

Mac/Linux:
`source venv/bin/activate`

3. Install Dependencies
`pip install -r requirements.txt`

4. Set Up API Key

This project uses the Groq API for AI-powered query processing.

Windows:
`set GROQ_API_KEY=your_api_key_here`

Mac/Linux:
`export GROQ_API_KEY=your_api_key_here`

5. Run the Application
`streamlit run app.py`

6. Open in Browser

After running, the app will open automatically

Notes:
- Make sure Python 3.8+ is installed
- Do not share your API key publicly
- Ensure your dataset is in CSV or Excel format

Quick Start:
`git clone <repo-link>
cd <repo-name>
pip install -r requirements.txt
set GROQ_API_KEY=your_key
streamlit run app.py`

## 💡 How It Works

```
User uploads CSV
       ↓
Dataset loaded into Pandas DataFrame
       ↓
User selects chart type → Matplotlib renders visualization
       ↓
User types natural language query
       ↓
Query + DataFrame schema sent to Groq API (LLaMA 3)
       ↓
LLM returns a Pandas code string
       ↓
Code executed safely → result rendered as table
```

---

## 📸 Sample Queries

| Natural Language Query | Equivalent Pandas Operation |
|---|---|
| "Top 5 products by sales" | `df.groupby('Product')['Sales'].sum().nlargest(5)` |
| "Monthly revenue trend" | `df.groupby('Month')['Revenue'].sum()` |
| "Show null values in each column" | `df.isnull().sum()` |
| "Average order value by region" | `df.groupby('Region')['Order_Value'].mean()` |

---

## 📦 Requirements

```
streamlit
pandas
numpy
matplotlib
groq
python-dotenv
```

---

## 🔮 Roadmap

- [ ] Support for Excel (.xlsx) uploads
- [ ] Export charts as PNG/PDF
- [ ] Multi-turn conversational memory for follow-up queries
- [ ] Support for additional LLM providers (OpenAI, Gemini)
- [ ] Automated insight narration using GenAI

---

## 👤 Author

**Shubham Jindal**
Dual Degree — MCA (IT) + PGDM | Data Analytics Enthusiast

[![LinkedIn](https://img.shields.io/badge/LinkedIn-shubham--jindal123-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/shubham-jindal123)
[![GitHub](https://img.shields.io/badge/GitHub-shubhamjindal250-black?style=flat&logo=github)](https://github.com/shubhamjindal250)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

> ⭐ If you found this useful, consider starring the repo!
