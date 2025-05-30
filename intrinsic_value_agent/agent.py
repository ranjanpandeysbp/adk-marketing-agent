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

from intrinsic_value_agent.instructions import (
    INTRINSIC_VALUE_INSTRUCTION
)

intrinsic_research_agent = LlmAgent(
    name="IntrinsicAgent",
    model=MODEL_NAME,
    instruction=INTRINSIC_VALUE_INSTRUCTION,
    tools=[google_search],
    output_key="intrinsic_summary"
)

root_agent = intrinsic_research_agent