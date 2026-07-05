from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
from rich import print
import os
from dotenv import load_dotenv

load_dotenv()

tavily_key = os.getenv("TAVILY_API_KEY")
if not tavily_key:
    raise ValueError("TAVILY_API_KEY is not set in .env file")

tavily = TavilyClient(api_key=tavily_key)


@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information on a topic. Returns Titles, URLS, and Snippets of the top results. If no results are found, returns a message indicating that no results were found.
    """
    try:
        results = tavily.search(query=query, max_results=5)
        
        if not results or not results.get('results'):
            return f"No search results found for query: {query}"
        
        out = []
        for r in results['results']:
            out.append(f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n")
        
        final_result = "\n-----\n".join(out)
        return final_result if final_result.strip() else f"No search results found for query: {query}"
    except Exception as e:
        return f"Error during search: {str(e)}"


@tool
def scrape_url(url: str) -> str:
    """
    Scrape the content of a webpage of the given URL. Returns the text content of the page after reading deeper.
    """
    try:
        resp = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        content = soup.get_text(separator='\n', strip=True)[:3000]
        return content if content.strip() else "No content found in the webpage"
    except Exception as e:
        return f"An error occurred while trying to scrape the webpage: {str(e)}"