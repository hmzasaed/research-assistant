from agents import search_chain, reader_chain, writer_chain, critic_chain
from tools import web_search, scrape_url

def run_research_pipeline(topic: str) -> dict:
    """
    Complete research pipeline with 4 steps:
    1. Search for information
    2. Read and analyze content
    3. Write comprehensive report
    4. Get critic feedback
    """
    state = {}

    # STEP 1: SEARCH
    print("\n" + "="*70)
    print("STEP 1: Searching for information...")
    print("="*70)
    
    try:
        search_result = web_search.invoke(topic)
        print(f"✓ Search completed")
        state["search_data"] = search_result
        
        search_summary = search_chain.invoke({
            "topic": topic,
            "search_data": search_result
        })
        state["search_summary"] = search_summary
        print(f"Search Summary:\n{search_summary[:300]}...\n")
    except Exception as e:
        print(f"✗ Search Error: {e}")
        state["search_data"] = f"Information about {topic}"
        state["search_summary"] = f"Research on {topic}"

    # STEP 2: READ & ANALYZE
    print("\n" + "="*70)
    print("STEP 2: Analyzing content...")
    print("="*70)
    
    try:
        scrape_result = scrape_url.invoke("https://www.bbc.com/news")
        print(f"✓ Content scraped")
        
        content_summary = reader_chain.invoke({
            "topic": topic,
            "content": scrape_result
        })
        state["content_summary"] = content_summary
        print(f"Content Summary:\n{content_summary[:300]}...\n")
    except Exception as e:
        print(f"✗ Content Analysis Error: {e}")
        state["content_summary"] = f"Analysis of {topic}"

    # STEP 3: WRITE REPORT
    print("\n" + "="*70)
    print("STEP 3: Writing research report...")
    print("="*70)
    
    try:
        report = writer_chain.invoke({
            "topic": topic,
            "search_summary": state.get("search_summary", ""),
            "content_summary": state.get("content_summary", "")
        })
        state["report"] = report
        print(f"✓ Report generated\n")
        print(f"Report:\n{report}\n")
    except Exception as e:
        print(f"✗ Report Writing Error: {e}")
        state["report"] = f"Research Report on {topic}"

    # STEP 4: GET CRITIC FEEDBACK
    print("\n" + "="*70)
    print("STEP 4: Getting expert feedback...")
    print("="*70)
    
    try:
        feedback = critic_chain.invoke({
            "report": state["report"]
        })
        state["feedback"] = feedback
        print(f"✓ Feedback received\n")
        print(f"Feedback:\n{feedback}\n")
    except Exception as e:
        print(f"✗ Critic Error: {e}")
        state["feedback"] = "Feedback on report"

    # SUMMARY
    print("\n" + "="*70)
    print("RESEARCH PIPELINE COMPLETE!")
    print("="*70)
    print(f"\nTopic: {topic}")
    print(f"Report Length: {len(state.get('report', ''))} characters")
    print(f"Feedback: {state.get('feedback', 'N/A')[:100]}...")
    
    return state


if __name__ == "__main__":
    print("\n" + "="*70)
    print("MULTIPLE RESEARCH AGENT - Research Pipeline")
    print("="*70)
    
    topic = input("\nEnter the topic you want to research: ").strip()
    if not topic:
        topic = "Artificial Intelligence"
        print(f"Using default topic: {topic}")
    
    results = run_research_pipeline(topic)
    
    print("\n" + "="*70)
    print("Pipeline execution finished!")
    print("="*70)