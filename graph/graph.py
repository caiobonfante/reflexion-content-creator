from typing import List
from graph.chains.revisor import revisor
from langgraph.graph import END, MessageGraph
from graph.tools.tool_executor import execute_tools
from graph.chains.first_responder import first_responder
from langchain_core.messages import BaseMessage, ToolMessage

MAX_ITERATIONS = 2

def event_loop(state: List[BaseMessage]) -> str:
    count_tool_visits = sum(isinstance(item, ToolMessage) for item in state)
    num_iterations = count_tool_visits
    if num_iterations > MAX_ITERATIONS:
        return END
    return "execute_tools"

builder = MessageGraph()

builder.add_node("draft", first_responder)
builder.add_node("execute_tools", execute_tools)
builder.add_node("revise", revisor)

builder.add_edge("draft", "execute_tools")
builder.add_edge("execute_tools", "revise")

builder.add_conditional_edges("revise", event_loop)

builder.set_entry_point("draft")

graph = builder.compile()