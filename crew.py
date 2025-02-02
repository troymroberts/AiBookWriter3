import os
from pathlib import Path
import yaml
from crewai import Agent, Crew, Process, Task
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# Agent imports
from agents.story_planner import StoryPlanner, StoryPlannerConfig
from agents.outline_creator import OutlineCreator, OutlineCreatorConfig
from agents.setting_builder import SettingBuilder, SettingBuilderConfig
from agents.character_creator import CharacterCreator, CharacterCreatorConfig
from agents.relationship_architect import RelationshipArchitect, RelationshipArchitectConfig
from agents.plot_agent import PlotAgent, PlotAgentConfig
from agents.writer import Writer, WriterConfig
from agents.editor import Editor, EditorConfig
from agents.critic import Critic, CriticConfig
from agents.reviser import Reviser, ReviserConfig
from agents.memory_keeper import MemoryKeeper, MemoryKeeperConfig
from agents.item_developer import ItemDeveloper, ItemDeveloperConfig
from agents.researcher import Researcher, ResearcherConfig

# Tool imports
from tools.ywriter_tools import (
    ReadProjectNotesTool,
    WriteProjectNoteTool,
    CreateChapterTool,
    ReadOutlineTool,
    ReadCharactersTool,
    ReadLocationsTool,
    ReadSceneTool,
    WriteSceneContentTool,
)

# Progress monitoring and writing state imports
from tools.writing_progress import WritingProgressMonitor
from tools.writing_state import WritingState

# Load environment variables
load_dotenv()

class BookWritingCrew:
    """Main crew class for the book writing project."""

    def __init__(self, ywriter_project: str):
        """Initialize the BookWritingCrew.
        
        Args:
            ywriter_project (str): Path to the yWriter project file
        """
        self.ywriter_project = ywriter_project

        # Set up the Ollama LLM
        self.ollama = Ollama(
            base_url="http://10.1.1.47:11434",
            model="qwen2.5:1.5b",
            temperature=0.7
        )

        # Load the genre configuration
        genre_file = os.environ.get("BOOK_GENRE", "literary_fiction") + ".yaml"
        genre_config_path = Path(__file__).parent / "config" / "genres" / genre_file

        try:
            with open(genre_config_path, "r") as f:
                self.genre_config = yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Genre config file not found: {genre_config_path}")
            self.genre_config = {}

        # Load tasks configuration
        tasks_config_path = Path(__file__).parent / "config" / "tasks.yaml"
        try:
            with open(tasks_config_path, "r") as f:
                self.tasks_config = yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Tasks config file not found: {tasks_config_path}")
            self.tasks_config = {}

        # Initialize the WritingProgressMonitor
        num_chapters = self.genre_config.get("num_chapters", 10)
        self.monitor = WritingProgressMonitor(num_chapters)
        self.monitor.start_session()

        # Initialize WritingState
        checkpoint_file = f"{ywriter_project}_checkpoint.json"
        if os.path.exists(checkpoint_file):
            self.state = WritingState(ywriter_project)
            self.state.load_checkpoint(checkpoint_file)
        else:
            self.state = WritingState(ywriter_project)

        # Create the crew with the configured LLM
        self.crew = Crew(
            agents=[],  # Agents will be added as needed
            process=Process.sequential,
            verbose=True,
            llm=self.ollama
        )

    def character_creator(self) -> Agent:
        """Return a configured CharacterCreator agent."""
        config = CharacterCreatorConfig()
        return CharacterCreator(config=config)

    def story_planner(self) -> Agent:
        """Return a configured StoryPlanner agent."""
        config = StoryPlannerConfig()
        return StoryPlanner(config=config)

    def outline_creator(self) -> Agent:
        """Return a configured OutlineCreator agent."""
        config = OutlineCreatorConfig()
        return OutlineCreator(
            config=config,
            tools=[
                ReadProjectNotesTool(yw7_path=self.ywriter_project),
                WriteProjectNoteTool(yw7_path=self.ywriter_project),
                CreateChapterTool(yw7_path=self.ywriter_project),
                ReadOutlineTool(yw7_path=self.ywriter_project),
                ReadCharactersTool(yw7_path=self.ywriter_project),
                ReadLocationsTool(yw7_path=self.ywriter_project),
            ],
        )

    def setting_builder(self) -> Agent:
        """Return a configured SettingBuilder agent."""
        config = SettingBuilderConfig()
        return SettingBuilder(config=config)

    def relationship_architect(self) -> Agent:
        """Return a configured RelationshipArchitect agent."""
        config = RelationshipArchitectConfig()
        return RelationshipArchitect(config=config)

    def plot_agent(self) -> Agent:
        """Return a configured PlotAgent."""
        config = PlotAgentConfig()
        return PlotAgent(config=config)

    def writer(self) -> Agent:
        """Return a configured Writer agent."""
        config = WriterConfig()
        return Writer(config=config)

    def editor(self) -> Agent:
        """Return a configured Editor agent."""
        config = EditorConfig()
        return Editor(config=config)

    def critic(self) -> Agent:
        """Return a configured Critic agent."""
        config = CriticConfig()
        return Critic(config=config)

    def reviser(self) -> Agent:
        """Return a configured Reviser agent."""
        config = ReviserConfig()
        return Reviser(config=config)

    def memory_keeper(self) -> Agent:
        """Return a configured MemoryKeeper agent."""
        config = MemoryKeeperConfig()
        return MemoryKeeper(config=config)

    def item_developer(self) -> Agent:
        """Return a configured ItemDeveloper agent."""
        config = ItemDeveloperConfig()
        return ItemDeveloper(config=config)

    def researcher(self) -> Agent:
        """Return a configured Researcher agent."""
        config = ResearcherConfig()
        return Researcher(config=config)

    def kickoff(self):
        """Initialize and start the crew's work."""
        # Add your kickoff logic here
        pass