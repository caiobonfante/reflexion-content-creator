from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field

class Reflection(BaseModel):
    missing: str = Field(description="Critique of what is missing.")
    superfluous: str = Field(description="Critique of what is superfluous")
    write_style: str = Field(description="Critique of how improve the writing style to be more human like.")

class AnswerQuestion(BaseModel):
    """Answer the question."""

    answer: str = Field(description="~400 word detailed post about to the theme.")
    reflection: Reflection = Field(description="Your reflection on the initial post.")
    search_queries: List[str] = Field(
        description="3 search queries for researching improvements to address the critique of your current post."
    )
    
class ReviseAnswer(AnswerQuestion):
    """Revise your original answer to your question."""

    references: List[str] = Field(
        description="Citations motivating your updated answer."
    )
