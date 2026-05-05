# 📈 AI Financial Advisor

An intelligent financial advisor powered by **LangChain**, **Groq (Llama 3.3)**, **RAG**, and **real-time stock data** via yFinance. Ask any finance question and get data-driven answers backed by Zerodha Varsity knowledge base.

---

## 🚀 Live Demo

> [Add your HuggingFace Spaces or Render link here]

---

## 🧠 How It Works

```
User Query
    ↓
LangChain Agent (Llama 3.3 70B via Groq)
    ↓                        ↓
get_stock_data tool    search_financial_knowledge tool
(yFinance API)         (RAG — Zerodha Varsity PDFs)
    ↓                        ↓
Real-time stock data   Retrieved context from FAISS
    ↓                        ↓
          LLM synthesizes final answer
                    ↓
          Streamlit chat UI displays response
```

---

## ✨ Features

- 💬 **Conversational chat interface** with full message history
- 📊 **Real-time Indian stock data** — price, PE ratio, 52-week high/low, market cap
- 📚 **RAG-powered knowledge base** built on Zerodha Varsity (Module 1 + Module 3)
- 🤖 **LangChain Agent** that decides which tools to call automatically
- 🧠 **Memory** — remembers context across the full conversation
- 🇮🇳 **Indian market focused** — NSE/BSE tickers supported

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| LLM | Llama 3.3 70B via Groq API |
| Agent Framework | LangChain |
| Stock Data | yFinance |
| Vector Store | FAISS |
| Embeddings | HuggingFace all-MiniLM-L6-v2 |
| PDF Loader | PyPDFLoader |
| Memory | RunnableWithMessageHistory |
| UI | Streamlit |
| Knowledge Base | Zerodha Varsity Module 1 + Module 3 |

---

## 📁 Project Structure

```
ai_financial_advisor/
│
├── app.py          ← Streamlit UI (entry point)
├── agent.py        ← LangChain agent + message history
├── tools.py        ← @tool functions (stock data + RAG search)
├── rag.py          ← RAG chain (PDF loading, FAISS, retrieval)
├── pdf's/
│   ├── Module 1_Introduction to Stock Markets.pdf
│   └── Module 3_Fundamental Analysis.pdf
├── .env            ← API keys (never commit this)
└── requirements.txt
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-financial-advisor.git
cd ai-financial-advisor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.env` file
```env
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here
```

Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 4. Add Zerodha Varsity PDFs
Download from [varsity.zerodha.com](https://varsity.zerodha.com) and place in `pdf's/` folder:
- Module 1 — Introduction to Stock Markets
- Module 3 — Fundamental Analysis

### 5. Run the app
```bash
streamlit run app.py
```

---

## 📦 Requirements

```txt
langchain
langchain-groq
langchain-community
langchain-huggingface
langchain-core
faiss-cpu
yfinance
streamlit
sentence-transformers
pypdf
python-dotenv
```

---

## 💬 Example Queries

| Query | Tools Used |
|---|---|
| `What is the current price of Reliance?` | get_stock_data |
| `What is PE ratio and how is it calculated?` | search_financial_knowledge |
| `Is TCS overvalued based on its PE ratio?` | get_stock_data + search_financial_knowledge |
| `I have ₹50,000 to invest, which stock should I buy?` | Both tools |
| `Compare Infosys and Wipro` | get_stock_data (twice) + search_financial_knowledge |

---

## 🔧 Supported Indian Stock Tickers

Add `.NS` for NSE or `.BO` for BSE:

```
RELIANCE.NS    TCS.NS    INFY.NS
HDFCBANK.NS    WIPRO.NS  TATAMOTORS.NS
```

---

## 📊 Architecture

```
┌─────────────────────────────────────────┐
│              Streamlit UI               │
│         (app.py — chat interface)       │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│           LangChain Agent               │
│   Llama 3.3 70B + Message History       │
│         (agent.py)                      │
└────────┬──────────────────┬─────────────┘
         │                  │
┌────────▼──────┐  ┌────────▼──────────────┐
│  get_stock_   │  │ search_financial_      │
│  data tool    │  │ knowledge tool         │
│  (yFinance)   │  │ (RAG + FAISS)          │
└───────────────┘  └────────────────────────┘
```

---

## ⚠️ Disclaimer

This tool is for **educational purposes only** and does not constitute professional financial advice. Always consult a SEBI-registered financial advisor before making investment decisions.

---

## 🙋 Author

**Amardeep**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [your linkedin](https://linkedin.com/in/yourprofile)

---

## ⭐ If you found this useful, give it a star!
