import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from graph.tools.models import AnswerQuestion
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are expert researcher.
            Current time: {time}

            1. {first_instruction}
            2. Reflect and critique your answer. Be severe to maximize improvement.
            3. Recommend search queries to research information and improve your post.
            """,
        ),
        MessagesPlaceholder(variable_name="messages"),
        ("system", "Create the post required by the user using the required format."),
    ]
).partial(
    time=lambda: datetime.datetime.now().isoformat(),
)

first_responder = actor_prompt_template.partial(
    first_instruction="Provide a detailed ~400 word post."
) | llm.bind_tools(tools=[AnswerQuestion], tool_choice="AnswerQuestion")
