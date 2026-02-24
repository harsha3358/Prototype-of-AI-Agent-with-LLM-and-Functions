# 🤖 AI Agent Prototype with LLM + Function Calling (Calculator Tool)

## 📌 Overview

This project demonstrates a prototype AI Agent built using Google's Gemini LLM that intelligently decides when to invoke a mathematical calculation tool.

The agent:
- Accepts natural language user queries
- Uses an LLM to determine whether a tool is required
- Extracts mathematical expressions
- Executes them securely using a safe Python AST-based calculator
- Returns the computed result

This project showcases foundational AI Agent architecture combining reasoning + tool execution.

---

## 🧠 Architecture

User Input  
   ↓  
LLM Decision Layer (Tool Selection)  
   ↓  
Expression Extraction  
   ↓  
Tool Execution (Safe Calculator)  
   ↓  
Final Response  

The LLM acts as the reasoning engine, while Python functions act as controlled tools.

---

## 🚀 Features

- ✅ LLM-powered decision making
- ✅ Tool invocation based on reasoning
- ✅ Secure mathematical evaluation using `ast` (No `eval()` used)
- ✅ Supports:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
- ✅ Interactive CLI-based agent loop
- ✅ Basic error handling for invalid expressions

---

## 🛠 Tech Stack

- Python 3.10+
- Google Gemini API (`google-generativeai`)
- AST Module (Secure Expression Parsing)
- Operator Module

---

## 📂 Project Structure

ai-agent-calculator/
│
├── main.py
├── requirements.txt
└── README.md

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ai-agent-calculator.git
cd ai-agent-calculator
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install google-generativeai
```

---

## 🔐 Environment Setup

⚠️ Never hardcode your API key.

Set your Gemini API key as an environment variable:

### Windows (PowerShell)
```bash
setx GEMINI_API_KEY "your_api_key_here"
```

### Mac/Linux
```bash
export GEMINI_API_KEY="your_api_key_here"
```

Then configure in code:

```python
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
```

---

## ▶️ Running the Agent

```bash
python main.py
```

Example:

Enter query (or exit): What is 10 + 5 * 2?

✅ Agent Decision: Calculation tool can solve this.  
🧠 LLM Extracted Expression: 10+5*2  
✅ Final Answer: 20  

---

## 🔎 How It Works

### Step 1 – Tool Decision
The LLM determines whether the query requires mathematical computation.

### Step 2 – Expression Extraction
If required, the LLM extracts the raw mathematical expression.

### Step 3 – Safe Tool Execution
The expression is parsed using Python's `ast` module to prevent arbitrary code execution.

This ensures security and controlled execution.

---

## 🏗 Why This Project Matters

This project demonstrates:
- AI Agent reasoning
- LLM + Tool integration
- Controlled execution pipelines
- Prompt engineering
- Secure system design

It reflects foundational concepts used in modern AI agent systems.

---

## ⚠️ Limitations (Prototype Scope)

- Prompt-based tool decision (not structured function calling)
- Limited operator support
- No memory/context retention
- CLI-only interface

---
