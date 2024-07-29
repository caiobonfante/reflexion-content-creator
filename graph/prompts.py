from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

actor_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are expert social media content post writer.
            Current time: {time}

            1. {first_instruction}
            2. Reflect and critique your post. Be severe to maximize improvement.
            3. Provide 3 search queries to research information and improve the post. Never skip this step, always provide the queries.
            """,
        ),
        MessagesPlaceholder(variable_name="messages"),
        ("system", "Answer the user's question above using the required format."),
    ]
).partial(
    time=lambda: datetime.now().isoformat(),
)