# AI Agent with Calculator Tool

A command-line AI agent that decides when a question requires calculation, extracts the expression, and sends it to a controlled Python tool.

## Why it matters

Modern AI agents are useful because they can combine language understanding with reliable software functions. This project demonstrates that pattern in a small, understandable form.

## What it does

- Accepts natural-language questions
- Uses Gemini to decide whether calculation is needed
- Extracts a mathematical expression
- Evaluates supported operations through Python's AST
- Avoids unsafe `eval()` execution

## Technology

Python, Google Gemini, AST parsing, and a command-line interface.

## Run

```bash
pip install google-generativeai
python main.py
```

Set `GEMINI_API_KEY` in the environment. The prototype supports a limited set of operators and does not retain conversation memory.
