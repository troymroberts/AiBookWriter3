from crewai import Agent
from pydantic import BaseModel, Field
from typing import Optional

class CharacterCreatorConfig(BaseModel):
    """Configuration for the CharacterCreator agent's LLM."""
    llm_endpoint: str = Field(
        default="http://10.1.1.47:11434",
        description="Endpoint for the Ollama server."
    )
    llm_model: str = Field(
        default="qwen2.5:1.5b",
        description="Model identifier for Ollama."
    )
    temperature: float = Field(
        default=0.7,
        description="Temperature setting for the language model.",
        ge=0.0,
        le=1.0
    )
    top_p: float = Field(
        default=0.95,
        description="Top-p sampling parameter for the language model.",
        ge=0.0,
        le=1.0
    )

    class Config:
        """Pydantic configuration class."""
        arbitrary_types_allowed = True

class CharacterCreator(Agent):
    """Agent responsible for creating and managing characters in the story."""

    def __init__(self, config: CharacterCreatorConfig):
        """Initialize the CharacterCreator agent.
        
        Args:
            config: Configuration instance containing LLM settings.
        """
        super().__init__(
            role='Character Creator',
            goal="""
                Develop and maintain consistent, engaging, and evolving characters throughout the story.
                Provide full names, ages, detailed backstories, motivations, personalities, strengths, 
                weaknesses, and relationships for each character. Assign character stats 
                (e.g., Intelligence, Charisma, etc.) on a scale of 1-10 and define their speech 
                patterns (e.g., accent, tone, verbosity). Ensure characters are diverse and well-rounded.
                """,
            backstory="""
                You are the character development expert, responsible for creating and maintaining 
                consistent, engaging, and evolving characters throughout the book. You define and 
                track all key characters, ensuring depth, consistency, and compelling arcs. 
                
                Your expertise includes:
                - Creating detailed character profiles with physical and psychological traits
                - Developing unique voices and speech patterns for each character
                - Building realistic character relationships and dynamics
                - Ensuring character motivations drive the story forward
                - Maintaining character consistency across all chapters
                
                You provide full names, ages, detailed backstories, and rich descriptions.
                You also assign character stats and define speech patterns to guide the writer 
                in creating realistic dialogue and interactions.
                """,
            verbose=True,
            allow_delegation=False,
            tools=[],  # Add specific character development tools as needed
            llm_config={
                "config_type": "ollama",
                "base_url": config.llm_endpoint,
                "model": config.llm_model,
                "temperature": config.temperature,
                "top_p": config.top_p
            }
        )