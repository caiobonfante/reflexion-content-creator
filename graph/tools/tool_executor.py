import json
from typing import List
from dotenv import load_dotenv
from collections import defaultdict
from langgraph.prebuilt import ToolInvocation, ToolExecutor
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import AIMessage, BaseMessage, ToolMessage
from langchain_core.output_parsers.openai_tools import JsonOutputToolsParser
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper

load_dotenv()

parser = JsonOutputToolsParser(return_id=True)
search = TavilySearchAPIWrapper()
tavily_tool = TavilySearchResults(api_wrapper=search, max_results=5)
tool_executor = ToolExecutor([tavily_tool])

def execute_tools(state: List[BaseMessage]) -> List[BaseMessage]:
    tool_invocation: AIMessage = state[-1]
    parsed_tool_calls = parser.invoke(tool_invocation)
    ids = []
    tool_invocations = []
    for parsed_call in parsed_tool_calls:
        for query in parsed_call["args"]["search_queries"]:
            tool_invocations.append(
                ToolInvocation(
                    tool="tavily_search_results_json",
                    tool_input=query,
                )
            )
            ids.append(parsed_call["id"])

    outputs = tool_executor.batch(tool_invocations)

    outputs_map = defaultdict(dict)
    for id_, output, invocation in zip(ids, outputs, tool_invocations):
        outputs_map[id_][invocation.tool_input] = output

    tool_messages = []
    for id_, query_outputs in outputs_map.items():
        tool_messages.append(
            ToolMessage(content=json.dumps(query_outputs), tool_call_id=id_)
        )

    return tool_messages
