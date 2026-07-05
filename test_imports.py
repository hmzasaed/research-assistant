"""
Quick test to verify all imports and basic functionality
"""
print("Testing imports...")

try:
    from tools import web_search, scrape_url
    print("✓ Tools imported successfully")
except Exception as e:
    print(f"✗ Tools import error: {e}")
    exit(1)

try:
    from agents import search_chain, reader_chain, writer_chain, critic_chain
    print("✓ Agents imported successfully")
except Exception as e:
    print(f"✗ Agents import error: {e}")
    exit(1)

try:
    from pipeline import run_research_pipeline
    print("✓ Pipeline imported successfully")
except Exception as e:
    print(f"✗ Pipeline import error: {e}")
    exit(1)

print("\n✓✓✓ All imports successful! ✓✓✓")
print("\nYou can now run: python pipeline.py")
