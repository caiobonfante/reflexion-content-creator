from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from graph.tools.models import ReviseAnswer
from graph.prompts import actor_template

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

revise_instructions = """Revise your previous post using the new information.
    - You should use the previous critique to add important information to your post.
        - You MUST include numerical citations in your revised post to ensure it can be verified.
        - Add a "References" section to the bottom of your post (which does not count towards the word limit), never skip this instruction. In form of:
            - [1] https://example.com/article1
            - [2] https://example.com/article2
            - [3] https://example.com/article3
            ...
            - [N] https://example.com/articleN
    - You should use the previous critique to remove superfluous information from your post and make SURE it is not more than 400 words.
    - You should evaluate the quality of your post and make sure it is well-structured and easy to read.
    - Provide detailed recommendations, including requests for length, depth, style, etc.
"""

revisor = actor_template.partial(
    first_instruction=revise_instructions
) | llm.bind_tools(tools=[ReviseAnswer], tool_choice="ReviseAnswer")
