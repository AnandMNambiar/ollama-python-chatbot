# Local Python Chatbot (Python + Ollama)

A simple beginner-friendly **terminal chatbot** written in **Python** that chats with a **local LLM** through **Ollama** (default model: `phi3`). Designed as a first chatbot project: small, readable, and easy to extend.

## What it does
- Chat in the terminal with a local AI model
- Keeps conversation context during the session (basic memory)
- Supports commands:
  - `/reset` — clears the current conversation
  - `/quit` — exits the program

## Tech stack
- Python
- Ollama (local LLM runtime)
- Model: `phi3` (configurable)

## Configuration
The model is set in `chatbot.py`:
- `MODEL = "phi3"`

You can switch to any model available in your local Ollama library.

## Project structure
- `chatbot.py` — main chatbot script
- `.gitignore` — ignores virtual environment/cache files (recommended)

## Roadmap (ideas)
- Stream tokens (print responses as they generate)
- Save/load chat history between runs
- Add a system prompt editor
- Add tools (web search, file Q&A) with guardrails
- Simple GUI (Tkinter / web UI)

## License
MIT
