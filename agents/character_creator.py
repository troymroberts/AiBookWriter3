from crewai import Agent
from pydantic import BaseModel, Field
from typing import Optional

class CharacterCreatorConfig(BaseModel):
    llm_endpoint: str = Field(default="http://localhost:11434", description="Endpoint for the language model server.")
    llm_model: str = Field(default="ollama/llama3.2:3b", description="Model identifier for the character creator.")
    temperature: float = Field(default=0.7, description="Temperature setting for the language model.")
    max_tokens: int = Field(default=2000, description="Maximum number of tokens for the language model.")
    top_p: float = Field(default=0.95, description="Top-p sampling parameter for the language model.")
    system_template: Optional[str] = Field(
        default=None,
        description="System template for the character creator agent."
    )
    prompt_template: Optional[str] = Field(
        default=None,
        description="Prompt template for the character creator agent."
    )
    response_template: Optional[str] = Field(
        default=None,
        description="Response template for the character creator agent."
    )

    class Config:
        arbitrary_types_allowed = True

class CharacterCreator(Agent):
    def __init__(self, config: CharacterCreatorConfig):
        super().__init__(
            role='Character Creator',
            goal=f"""
                Develop and maintain consistent, engaging, and evolving characters throughout the story.
                Provide full names, ages, detailed backstories, motivations, personalities, strengths, weaknesses, and relationships for each character.
                Assign character stats (e.g., Intelligence, Charisma, etc.) on a scale of 1-10 and define their speech patterns (e.g., accent, tone, verbosity).
                Ensure characters are diverse and well-rounded.
                """,
            backstory=f"""
                You are the character development expert, responsible for creating and maintaining consistent, engaging, and evolving characters throughout the book.
                You define and track all key characters, ensuring depth, consistency, and compelling arcs. You provide full names, ages, detailed backstories, and rich descriptions.
                You also assign character stats and define speech patterns to guide the writer in creating realistic dialogue and interactions.
                """,
            verbose=True,
            allow_delegation=False,
            llm=self.create_llm(config),
            # TODO: Add tools here
            tools=[],
        )

    def create_llm(self, config: CharacterCreatorConfig):
        from crewai.llm import LLM
        return LLM(
            base_url=config.llm_endpoint,
            model=config.llm_model,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            top_p=config.top_p,
            system_template=config.system_template,
            prompt_template=config.prompt_template,
            response_template=config.response_template,
        )