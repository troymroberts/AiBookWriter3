import os
from pathlib import Path

import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff

# Import your agent definitions using absolute imports:
from agents.story_planner import StoryPlanner, StoryPlannerConfig
from agents.outline_creator import OutlineCreator, OutlineCreatorConfig
from agents.setting_builder import SettingBuilder, SettingBuilderConfig
from agents.character_creator import CharacterCreator, CharacterCreatorConfig
from agents.relationship_architect import (
    RelationshipArchitect,
    RelationshipArchitectConfig,
)
from agents.plot_agent import PlotAgent, PlotAgentConfig
from agents.writer import Writer, WriterConfig
from agents.editor import Editor, EditorConfig
from agents.critic import Critic, CriticConfig
from agents.reviser import Reviser, ReviserConfig
from agents.memory_keeper import MemoryKeeper, MemoryKeeperConfig
from agents.item_developer import ItemDeveloper, ItemDeveloperConfig
from agents.researcher import Researcher, ResearcherConfig

# Import your custom tools using absolute imports:
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

# Import your progress monitoring and writing state tools using absolute imports:
from tools.writing_progress import WritingProgressMonitor
from tools.writing_state import WritingState

# from .tools.rag_tools import RAGTool  # Uncomment when you implement RAG

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class BookWritingCrew:
    """
    This is the main crew class for your book writing project.
    It defines the agents, tasks, and overall crew configuration.
    """

    # Set the path to your yWriter 7 project file
    ywriter_project: str = "your_ywriter_project.yw7"  # Replace with your actual file

    # Load the config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # Load the genre configuration based on the environment variable
    genre_file = os.environ.get("BOOK_GENRE", "literary_fiction") + ".yaml"
    genre_config_path = Path(__file__).parent / "config" / "genres" / genre_file

    try:
        with open(genre_config_path, "r") as f:
            genre_config = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Genre config file not found: {genre_config_path}")
        genre_config = {}  # Default to empty config if file not found

    def __init__(self, ywriter_project: str):
        super().__init__()  # Initialize the superclass
        self.ywriter_project = ywriter_project

        # Load the genre configuration
        genre_file = os.environ.get("BOOK_GENRE", "literary_fiction") + ".yaml"
        genre_config_path = Path(__file__).parent / "config" / "genres" / genre_file

        try:
            with open(genre_config_path, "r") as f:
                self.genre_config = yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Genre config file not found: {genre_config_path}")
            self.genre_config = {}  # Default to empty config if file not found

        # Initialize the WritingProgressMonitor with the number of chapters from genre_config
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

    # Define your agents using the @agent decorator.
    @agent
    def story_planner(self) -> Agent:
        config = StoryPlannerConfig(
            llm_model=self.genre_config.get("llm_model"),
            llm_endpoint=self.genre_config.get("llm_endpoint"),
            temperature=self.genre_config.get("temperature"),
            max_tokens=self.genre_config.get("max_tokens"),
            top_p=self.genre_config.get("top_p"),
        )
        return StoryPlanner(config=config)

    @agent
    def outline_creator(self) -> Agent:
        config = OutlineCreatorConfig(
            llm_model=self.genre_config.get("llm_model"),
            llm_endpoint=self.genre_config.get("llm_endpoint"),
            temperature=self.genre_config.get("temperature"),
            max_tokens=self.genre_config.get("max_tokens"),
            top_p=self.genre_config.get("top_p"),
        )
        return OutlineCreator(
            config=config,
            tools=[
                # ChapterBreakdownTool(),  # Assuming you will implement these custom tools later
                # OutlineTemplateTool(),
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
        config = SettingBuilderConfig(
            llm_model=self.genre_config.get("llm_model"),
            llm_endpoint=self.genre_config.get("llm_endpoint"),
            temperature=self.genre_config.get("temperature"),
            max_tokens=self.genre_config.get("max_tokens"),
            top_p=self.genre_config.get("top_p"),
        )
        return SettingBuilder(config=config)

    @agent
    def character_creator(self) -> Agent:
        config = CharacterCreatorConfig(
            llm_model=self.genre_config.get("llm_model"),
            llm_endpoint=self.genre_config.get("llm_endpoint"),
            temperature=self.genre_config.get("temperature"),
            max_tokens=self.genre_config.get("max_tokens"),
            top_p=self.genre_config.get("top_p"),
        )
        return CharacterCreator(config=config)

    @agent
    def relationship_architect(self) -> Agent:
        config = RelationshipArchitectConfig(
            llm_model=self.genre_config.get("llm_model"),
            llm_endpoint=self.genre_config.get("llm_endpoint"),
            temperature=self.genre_config.get("temperature"),
            max_tokens=self.genre_config.get("max_tokens"),
            top_p=self.genre_config.get("top_p"),
        )
        return RelationshipArchitect(config=config)

    @agent
    def plot_agent(self) -> Agent:
        config = PlotAgentConfig(
            llm_model=self.genre_config.get("llm_model"),
            llm_endpoint=self.genre_config.get("llm_endpoint"),
            temperature=self.genre_config.get("temperature"),
            max_tokens=self.genre_config.get("max_tokens"),
            top_p=self.genre_config.get("top_p"),
        )
        return PlotAgent(config=config)

    @agent
    def writer(self) -> Agent:
        config = WriterConfig(
            llm_model=self.genre_config.get("llm_model"),
            llm_endpoint=self.genre_config.get("llm_endpoint"),
            temperature=self.genre_config.get("temperature"),
            max_tokens=self.genre_config.get("max_tokens"),
            top_p=self.genre_config.get("top_p"),
        )
        return Writer(config=config)

    @agent
    def editor(self) -> Agent:
        config = EditorConfig(
            llm_model=self.genre_config.get("llm_model"),
            llm_endpoint=self.genre_config.get("llm_endpoint"),
            temperature=self.genre_config.get("temperature"),
            max_tokens=self.genre_config.get("max_tokens"),
            top_p=self.genre_config.get("top_p"),
        )
        return Editor(config=config)

    @agent
    def critic(self) -> Agent:
        config = CriticConfig(
            llm_model=self.genre_config.get("llm_model"),
            llm_endpoint=self.genre_config.get("llm_endpoint"),
            temperature=self.genre_config.get("temperature"),
            max_tokens=self.genre_config.get("max_tokens"),
            top_p=self.genre_config.get("top_p"),
        )
        return Critic(config=config)

    @agent
    def reviser(self) -> Agent:
        config = ReviserConfig(
            llm_model=self.genre_config.get("llm_model"),
            llm_endpoint=self.genre_config.get("llm_endpoint"),
            temperature=self.genre_config.get("temperature"),
            max_tokens=self.genre_config.get("max_tokens"),
            top_p=self.genre_config.get("top_p"),
        )
        return Reviser(config=config)

    @agent
    def memory_keeper(self) -> Agent:
        config = MemoryKeeperConfig(
            llm_model=self.genre_config.get("llm_model"),
            llm_endpoint=self.genre_config.get("llm_endpoint"),
            temperature=self.genre_config.get("temperature"),
            max_tokens=self.genre_config.get("max_tokens"),
            top_p=self.genre_config.get("top_p"),
        )
        return MemoryKeeper(config=config)

    @agent
    def item_developer(self) -> Agent:
        config = ItemDeveloperConfig(
            llm_model=self.genre_config.get("llm_model"),
            llm_endpoint=self.genre_config.get("llm_endpoint"),
            temperature=self.genre_config.get("temperature"),
            max_tokens=self.genre_config.get("max_tokens"),
            top_p=self.genre_config.get("top_p"),
        )
        return ItemDeveloper(config=config)

    @agent
    def researcher(self) -> Agent:
        config = ResearcherConfig(
            llm_model=self.genre_config.get("llm_model"),
            llm_endpoint=self.genre_config.get("llm_endpoint"),
            temperature=self.genre_config.get("temperature"),
            max_tokens=self.genre_config.get("max_tokens"),
            top_p=self.genre_config.get("top_p"),
        )
        return Researcher(config=config)

    # Define your tasks using the @task decorator.
    @task
    def plan_story_arc(self) -> Task:
        return Task(
            config=self.tasks_config["plan_story_arc"],
            agent=self.story_planner,
        )

    @task
    def create_chapter_outlines(self) -> Task:
        return Task(
            config=self.tasks_config["create_chapter_outlines"],
            agent=self.outline_creator,
            context=[self.plan_story_arc],
        )

    # Add other task definitions here using @task decorator

    @before_kickoff
    def before_kickoff_function(self, inputs):
        print("Before kickoff function with inputs:", inputs)
        return inputs

    @after_kickoff
    def after_kickoff_function(self, result):
        print("After kickoff function with result:", result)
        return result

    @crew
    def crew(self) -> Crew:
        """
        Creates the Book Writing crew.

        To learn how to add knowledge sources to your crew, check out the documentation:
        https://docs.crewai.com/concepts/knowledge/#what-is-knowledge
        """
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )