import datetime
from dotenv import load_dotenv
from graph.prompts import actor_template
from langchain_openai import ChatOpenAI
from graph.tools.models import AnswerQuestion
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

first_responder = actor_template.partial(
    first_instruction="Provide a detailed ~400 word post."
) | llm.bind_tools(tools=[AnswerQuestion], tool_choice="AnswerQuestion")
