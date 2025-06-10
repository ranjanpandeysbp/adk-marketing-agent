# File agent.py
import asyncio
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams
# No need for google.adk.runners.Runner in this file when using adk web/run

# Define the remote SSE MCP server's URI
# Note: For adk web to access a remote server, ensure the server (178.16.137.35:8121)
# is publicly accessible or accessible from where adk web is running.
remote_sse_uri = "http://178.16.137.35:8121/sse"

# Create the MCPToolset instance directly, passing SseServerParams.
# This will be used by the LlmAgent.
mcp_toolset = MCPToolset(
    connection_params=SseServerParams(url=remote_sse_uri)
)

# CRITICAL CHANGE FOR ADK WEB/RUN:
# Define the root_agent directly as an instance of LlmAgent.
# The ADK CLI (adk web or adk run) will automatically discover and use this variable.
root_agent = LlmAgent(
    model='gemini-2.0-flash', # Or your preferred model
    name='my_remote_tool_agent', # This name should ideally match your project/package name
    instruction="You are an agent that can use remote tools, including an article extractor from external services.",
    tools=[mcp_toolset], # Pass the created MCPToolset instance
)

# The 'main' function and direct 'asyncio.run(main())' block are removed.
# These are for standalone script execution, not for integration with adk web/run.
# When you run `adk web <your_agent_directory_or_module>`, ADK handles the lifecycle
# of `root_agent` and exposes it via a web interface.