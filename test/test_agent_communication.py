# test_agent_communication.py
import unittest
from crewai import Agent, Task

# Import your agent definitions and configurations from crew.py 
from crew import BookWritingCrew

class AgentCommunicationTest(unittest.TestCase):

    def setUp(self):
        # We don't need to load a real yWriter project for this test
        self.crew = BookWritingCrew(ywriter_project="dummy_project.yw7")  
        self.crew.kickoff()  # Initialize the agents

    def test_story_planner_communication(self):
        task = Task(description="Introduce yourself.", agent=self.crew.story_planner)
        result = task.execute()
        self.assertNotEqual(result, "", "StoryPlanner failed to communicate with the model.")
        self.assertNotIn("Error", result, "StoryPlanner encountered an error.")

    def test_outline_creator_communication(self):
        task = Task(description="Introduce yourself.", agent=self.crew.outline_creator)
        result = task.execute()
        self.assertNotEqual(result, "", "OutlineCreator failed to communicate with the model.")
        self.assertNotIn("Error", result, "OutlineCreator encountered an error.")

    def test_setting_builder_communication(self):
        task = Task(description="Introduce yourself.", agent=self.crew.setting_builder)
        result = task.execute()
        self.assertNotEqual(result, "", "SettingBuilder failed to communicate with the model.")
        self.assertNotIn("Error", result, "SettingBuilder encountered an error.")

    def test_character_creator_communication(self):
        task = Task(description="Introduce yourself.", agent=self.crew.character_creator)
        result = task.execute()
        self.assertNotEqual(result, "", "CharacterCreator failed to communicate with the model.")
        self.assertNotIn("Error", result, "CharacterCreator encountered an error.")

    def test_relationship_architect_communication(self):
        task = Task(description="Introduce yourself.", agent=self.crew.relationship_architect)
        result = task.execute()
        self.assertNotEqual(result, "", "RelationshipArchitect failed to communicate with the model.")
        self.assertNotIn("Error", result, "RelationshipArchitect encountered an error.")

    def test_plot_agent_communication(self):
        task = Task(description="Introduce yourself.", agent=self.crew.plot_agent)
        result = task.execute()
        self.assertNotEqual(result, "", "PlotAgent failed to communicate with the model.")
        self.assertNotIn("Error", result, "PlotAgent encountered an error.")

    def test_writer_communication(self):
        task = Task(description="Introduce yourself.", agent=self.crew.writer)
        result = task.execute()
        self.assertNotEqual(result, "", "Writer failed to communicate with the model.")
        self.assertNotIn("Error", result, "Writer encountered an error.")

    def test_editor_communication(self):
        task = Task(description="Introduce yourself.", agent=self.crew.editor)
        result = task.execute()
        self.assertNotEqual(result, "", "Editor failed to communicate with the model.")
        self.assertNotIn("Error", result, "Editor encountered an error.")

    def test_critic_communication(self):
        task = Task(description="Introduce yourself.", agent=self.crew.critic)
        result = task.execute()
        self.assertNotEqual(result, "", "Critic failed to communicate with the model.")
        self.assertNotIn("Error", result, "Critic encountered an error.")

    def test_reviser_communication(self):
        task = Task(description="Introduce yourself.", agent=self.crew.reviser)
        result = task.execute()
        self.assertNotEqual(result, "", "Reviser failed to communicate with the model.")
        self.assertNotIn("Error", result, "Reviser encountered an error.")

    def test_memory_keeper_communication(self):
        task = Task(description="Introduce yourself.", agent=self.crew.memory_keeper)
        result = task.execute()
        self.assertNotEqual(result, "", "MemoryKeeper failed to communicate with the model.")
        self.assertNotIn("Error", result, "MemoryKeeper encountered an error.")

    def test_item_developer_communication(self):
        task = Task(description="Introduce yourself.", agent=self.crew.item_developer)
        result = task.execute()
        self.assertNotEqual(result, "", "ItemDeveloper failed to communicate with the model.")
        self.assertNotIn("Error", result, "ItemDeveloper encountered an error.")

    def test_researcher_communication(self):
        task = Task(description="Introduce yourself.", agent=self.crew.researcher)
        result = task.execute()
        self.assertNotEqual(result, "", "Researcher failed to communicate with the model.")
        self.assertNotIn("Error", result, "Researcher encountered an error.")

if __name__ == '__main__':
    unittest.main()