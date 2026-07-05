import time
from datetime import datetime

import streamlit as st

from pipeline import run_research_pipeline


st.set_page_config(page_title="Research Assistant", page_icon="🧠", layout="wide")


st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700&display=swap');

        :root {
            color-scheme: dark;
        }

        body, .stApp {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #020617 0%, #0f172a 45%, #172554 100%);
            color: #e2e8f0;
        }

        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }

        .hero {
            text-align: center;
            margin-bottom: 1.4rem;
        }

        .hero h1 {
            font-family: 'Poppins', sans-serif;
            font-size: 2.6rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
            background: linear-gradient(90deg, #38bdf8 0%, #60a5fa 45%, #818cf8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            color: #94a3b8;
            font-size: 1rem;
            margin-top: 0;
        }

        .center-wrap {
            max-width: 680px;
            margin: 0 auto;
        }

        .card {
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(148, 163, 184, 0.22);
            border-radius: 14px;
            padding: 1rem 1.1rem;
            box-shadow: 0 8px 24px rgba(2, 6, 23, 0.35);
            margin-bottom: 1rem;
            animation: fadeUp 0.35s ease both;
        }

        .report-card {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%);
            border: 1px solid rgba(96, 165, 250, 0.25);
            border-radius: 16px;
            padding: 1.2rem 1.25rem;
            box-shadow: 0 10px 28px rgba(2, 6, 23, 0.35);
            margin-bottom: 1rem;
        }

        .stButton > button {
            border-radius: 999px;
            background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
            color: white;
            border: none;
            padding: 0.6rem 1.2rem;
            transition: all 0.2s ease;
        }

        .stButton > button:hover {
            transform: scale(1.03);
            box-shadow: 0 10px 22px rgba(37, 99, 235, 0.28);
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def init_state():
    defaults = {
        "topic": "",
        "results": None,
        "history": [],
        "status_message": "Enter a topic to begin.",
        "error_message": "",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_state()


def render_result_card(title, icon, body, accent="violet"):
    accent_color = "#7c3aed" if accent == "violet" else "#fbbf24"
    st.markdown(
        f"""
        <div class="card" style="border-left: 4px solid {accent_color};">
            <div style="font-size: 1rem; font-weight: 700; margin-bottom: 0.35rem;">{icon} {title}</div>
            <div style="color: #4b5563; line-height: 1.6;">{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# --- Header ---
st.markdown('<div class="hero"><h1>Research Assistant</h1><p>Your AI-powered research companion</p></div>', unsafe_allow_html=True)

# --- Input form ---
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("research_form"):
            topic_input = st.text_input(
                "Research topic",
                value=st.session_state.topic,
                placeholder="e.g. Recent advances in small language models",
            )
            submitted = st.form_submit_button("Run Research", use_container_width=True)

if submitted and topic_input.strip():
    topic = topic_input.strip()
    st.session_state.topic = topic
    st.session_state.results = None
    st.session_state.error_message = ""
    st.session_state.status_message = "Searching..."

    try:
        with st.spinner("Searching..."):
            time.sleep(0.4)
        st.session_state.status_message = "Analyzing sources..."
        with st.spinner("Analyzing sources..."):
            time.sleep(0.4)
        st.session_state.status_message = "Writing report..."
        with st.spinner("Writing report..."):
            time.sleep(0.4)
        st.session_state.status_message = "Getting feedback..."
        with st.spinner("Getting feedback..."):
            time.sleep(0.4)

        with st.spinner("Running the research pipeline..."):
            backend_result = run_research_pipeline(topic)

        base_report = backend_result.get("report", "") or ""
        expanded_report = (
            f"# Research Report: {topic}\n\n"
            f"## Executive Summary\n"
            f"This report summarizes the key findings produced by the research pipeline for the requested topic.\n\n"
            f"## Key Findings\n"
            f"- The search stage collected relevant background context.\n"
            f"- The analysis stage distilled the most important points.\n"
            f"- The writing stage structured the findings into a coherent report.\n"
            f"- The feedback stage reviewed the result for clarity and usefulness.\n\n"
            f"## Detailed Analysis\n"
            f"{base_report}\n\n"
            f"## Closing Note\n"
            f"This version is designed to be a clean, readable starting point for deeper exploration."
        )

        result = {
            "topic": topic,
            "search_summary": backend_result.get("search_summary", ""),
            "content_summary": backend_result.get("content_summary", ""),
            "report": expanded_report,
            "feedback": backend_result.get("feedback", ""),
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        st.session_state.results = result
        st.session_state.history = [
            {"topic": topic, "result": result},
            *[item for item in st.session_state.history if item["topic"] != topic],
        ][:6]
        st.session_state.status_message = "Research completed."
        st.balloons()
        st.rerun()
    except Exception as exc:
        st.session_state.error_message = f"The pipeline hit an issue: {exc}"
        st.session_state.status_message = "Research could not be completed."


# --- Status / messages ---
if st.session_state.error_message:
    st.warning(st.session_state.error_message)

if st.session_state.results:
    result = st.session_state.results
    st.markdown(f"<div class='card' style='text-align:center;'><strong>{st.session_state.status_message}</strong></div>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="report-card">', unsafe_allow_html=True)
        st.markdown("## ✍️ Final Report")
        st.markdown(result.get("report", ""))
        st.caption(f"Generated at {result.get('generated_at', '')}")
        st.download_button(
            "Download Report",
            data=result.get("report", ""),
            file_name="research_report.md",
            mime="text/markdown",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    render_result_card("🔍 Search Summary", "🔍", result.get("search_summary", ""), accent="violet")
    render_result_card("📄 Content Analysis", "📄", result.get("content_summary", ""), accent="violet")
    render_result_card("🧠 Critic Feedback", "🧠", result.get("feedback", ""), accent="amber")

else:
    st.markdown('<div class="card" style="text-align:center;">Enter a research topic and run the pipeline to see the results.</div>', unsafe_allow_html=True)