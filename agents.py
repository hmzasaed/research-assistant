from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
import os
from dotenv import load_dotenv

load_dotenv()

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY environment variable is not set")

print(f"OpenRouter API Key loaded: {openrouter_api_key[:10]}...")

# Single unified LLM instance using OpenRouter
llm = ChatOpenAI(
    api_key=openrouter_api_key,
    model="openai/gpt-4o-mini",
    base_url="https://openrouter.ai/api/v1",
    temperature=0.7
)

# Search Chain
search_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research assistant. Analyze the search results and provide key information."),
    ("human", "Search results for '{topic}':\n{search_data}\n\nProvide a summary of the most important findings.")
])
search_chain = search_prompt | llm | StrOutputParser()

# Reader Chain  
reader_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a content analyzer. Extract key insights from the webpage content."),
    ("human", "Webpage content for '{topic}':\n{content}\n\nExtract the 3 most important points.")
])
reader_chain = reader_prompt | llm | StrOutputParser()

# Writer Chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Create comprehensive, well-structured reports."),
    ("human", """Based on the following research data, write a professional research report about '{topic}'.

Search Summary:
{search_summary}

Content Summary:
{content_summary}

Write a report with:
- Executive Summary
- Key Findings (3-4 points)
- Conclusion
- Sources""")
])
writer_chain = writer_prompt | llm | StrOutputParser()

# Critic Chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research critic and quality evaluator."),
    ("human", """Evaluate this research report:

{report}

Provide:
- Quality Score (1-10)
- Strengths (2-3 points)
- Areas to Improve (2-3 points)""")
])
critic_chain = critic_prompt | llm | StrOutputParser()
