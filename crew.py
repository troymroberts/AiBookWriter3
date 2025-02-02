import os
from pathlib import Path

import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
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

@CrewBase
class BookWritingCrew:
    """
    Main crew class for the book writing project.
    Defines the agents, tasks, and overall crew configuration.
    """

    def __init__(self, ywriter_project: str):
        """Initialize the BookWritingCrew.
        
        Args:
            ywriter_project (str): Path to the yWriter project file
        """
        super().__init__()
        self.ywriter_project = ywriter_project

        # Load the genre configuration
        genre_file = os.environ.get("BOOK_GENRE", "literary_fiction") + ".yaml"
        genre_config_path = Path(__file__).parent / "config" / "genres" / genre_file

        try:
            with open(genre_config_path, "r") as f:
                self.genre_config = yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Genre config file not found: {genre_config_path}")
            self.genre_config = {}

        # Initialize progress monitoring
        num_chapters = self.genre_config.get("num_chapters", 10)
        self.monitor = WritingProgressMonitor(num_chapters)
        self.monitor.start_session()

        # Initialize writing state
        checkpoint_file = f"{ywriter_project}_checkpoint.json"
        if os.path.exists(checkpoint_file):
            self.state = WritingState(ywriter_project)
            self.state.load_checkpoint(checkpoint_file)
        else:
            self.state = WritingState(ywriter_project)

    # Agent definitions
    @agent
    def story_planner(self) -> Agent:
        """Return a configured StoryPlanner agent."""
        config = StoryPlannerConfig()
        return StoryPlanner(config=config)

    @agent
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

    @agent
    def setting_builder(self) -> Agent:
        """Return a configured SettingBuilder agent."""
        config = SettingBuilderConfig()
        return SettingBuilder(config=config)

    @agent
    def character_creator(self) -> Agent:
        """Return a configured CharacterCreator agent."""
        config = CharacterCreatorConfig()
        return CharacterCreator(config=config)

    @agent
    def relationship_architect(self) -> Agent:
        """Return a configured RelationshipArchitect agent."""
        config = RelationshipArchitectConfig()
        return RelationshipArchitect(config=config)

    @agent
    def plot_agent(self) -> Agent:
        """Return a configured PlotAgent."""
        config = PlotAgentConfig()
        return PlotAgent(config=config)

    @agent
    def writer(self) -> Agent:
        """Return a configured Writer agent."""
        config = WriterConfig()
        return Writer(config=config)

    @agent
    def editor(self) -> Agent:
        """Return a configured Editor agent."""
        config = EditorConfig()
        return Editor(config=config)

    @agent
    def critic(self) -> Agent:
        """Return a configured Critic agent."""
        config = CriticConfig()
        return Critic(config=config)

    @agent
    def reviser(self) -> Agent:
        """Return a configured Reviser agent."""
        config = ReviserConfig()
        return Reviser(config=config)

    @agent
    def memory_keeper(self) -> Agent:
        """Return a configured MemoryKeeper agent."""
        config = MemoryKeeperConfig()
        return MemoryKeeper(config=config)

    @agent
    def item_developer(self) -> Agent:
        """Return a configured ItemDeveloper agent."""
        config = ItemDeveloperConfig()
        return ItemDeveloper(config=config)

    @agent
    def researcher(self) -> Agent:
        """Return a configured Researcher agent."""
        config = ResearcherConfig()
        return Researcher(config=config)

    # Task definitions
    @task
    def plan_story_arc(self) -> Task:
        """Define the story arc planning task."""
        return Task(
            description="Create a high-level story arc for the entire book",
            agent=self.story_planner,
        )

    @task
    def create_chapter_outlines(self) -> Task:
        """Define the chapter outline creation task."""
        return Task(
            description="Create detailed outlines for each chapter",
            agent=self.outline_creator,
            context=[self.plan_story_arc],
        )

    # Crew lifecycle hooks
    @before_kickoff
    def before_kickoff_function(self, inputs):
        """Execute before the crew starts working.
        
        Args:
            inputs: The inputs to be processed
            
        Returns:
            The processed inputs
        """
        print("Before kickoff function with inputs:", inputs)
        return inputs

    @after_kickoff
    def after_kickoff_function(self, result):
        """Execute after the crew finishes working.
        
        Args:
            result: The results to be processed
            
        Returns:
            The processed results
        """
        print("After kickoff function with result:", result)
        return result

    @crew
    def crew(self) -> Crew:
        """Create and configure the BookWriting crew.
        
        Returns:
            A configured Crew instance
        """
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )