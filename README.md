# 🔬 Multi-Agent Research Assistant

[![Streamlit App](https://static.streamlit.io/badge_svg.svg)](https://share.streamlit.io/)
[![GitHub License](https://img.shields.io/github/license/hmzasaed/research-assistant?color=blue)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

An enterprise-grade, autonomous multi-agent research platform designed to search, scrape, synthesize, and evaluate comprehensive technical data in seconds. Built with a premium SaaS-style interface inspired by Perplexity AI, ChatGPT, and LangSmith.

---

## 🚀 Live Demo

Experience the live application hosted completely free on Streamlit Community Cloud:
🔗 **[Live App Link]([https://share.streamlit.io/](https://research-assistant-5baxfflizugcnpcs3lqhx8.streamlit.app/))** *(Replace with your actual Streamlit link once deployed!)*

---

## 🧠 System Architecture

The platform operates using four distinct, specialized AI agents working sequentially via structured chain handoffs:

1. **🔍 Search Agent:** Interacts with the web via high-precision toolchains (Tavily Search) to gather relevant data nodes.
2. **📖 Reader Agent:** Parses raw HTML targets, strips semantic boilerplate noise, and structures clean context.
3. **✍️ Writer Agent:** Synthesizes multi-source findings into a comprehensive, highly formatted Markdown report.
4. **🧠 Critic Agent:** Acts as an autonomous quality auditor, scoring readability and identifying logical anomalies or missing metrics.

---

## ✨ Key Features

- **Premium SaaS UI/UX:** Dark slate glassmorphism design with responsive grids, interactive components, and soft shadows.
- **Dynamic Live Activity Stream:** Real-time logging panel showing step-by-step agent telemetry and execution states.
- **Granular Controls:** Adjustable sliders for search depth configurations, result limits, and model temperatures.
- **Advanced Document Export Center:** One-click downloads for **Professional PDF (with custom cover page)**, Markdown (`.md`), MS Word (`.docx`), and Plain Text (`.txt`).
- **Flexible Provider Backend:** Dropdown switching support for Gemini, Groq, and OpenAI instances.

---

## 🛠️ Local Installation & Setup

Follow these simple steps to run the platform locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/hmzasaed/research-assistant.git](https://github.com/hmzasaed/research-assistant.git)
cd research-assistant
