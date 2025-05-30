import os

try:
    from dotenv import load_dotenv
    load_dotenv()

    MODEL_NAME = os.environ.get("GOOGLE_GENAI_MODEL", "gemini-2.0-flash")
except ImportError:
    print("Warning: python-dotenv not installed. Ensure API key is set")
    MODEL_NAME = "gemini-2.0-flash"

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search

from stock_market_ta_fa_researcher.instructions import (
    STOCK_RESEARCH_INSTRUCTION
)

stock_research_agent = LlmAgent(
    name="StockResearcher",
    model=MODEL_NAME,
    instruction=STOCK_RESEARCH_INSTRUCTION,
    tools=[google_search],
    output_key="stock_research_summary"
)

root_agent = stock_research_agent