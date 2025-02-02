import unittest
from crewai import Agent, Task
from crew import BookWritingCrew

class AgentCommunicationTest(unittest.TestCase):
    def setUp(self):
        """Set up the test environment with a BookWritingCrew instance."""
        self.crew = BookWritingCrew(ywriter_project="dummy_project.yw7")  

    def test_story_planner_communication(self):
        """Test if StoryPlanner agent can communicate with the model."""
        try:
            task = Task(
                description="Introduce yourself.",
                agent=self.crew.story_planner(),
                expected_output="A concise introduction from the Story Planner agent"
            )
            result = task.run()
            self.assertNotEqual(result, "", "StoryPlanner failed to communicate with the model.")
            self.assertNotIn("Error", result, "StoryPlanner encountered an error.")
        except Exception as e:
            self.fail(f"Story Planner task execution failed with error: {str(e)}")

    def test_outline_creator_communication(self):
        """Test if OutlineCreator agent can communicate with the model."""
        try:
            task = Task(
                description="Introduce yourself.",
                agent=self.crew.outline_creator(),
                expected_output="A concise introduction from the Outline Creator agent"
            )
            result = task.run()
            self.assertNotEqual(result, "", "OutlineCreator failed to communicate with the model.")
            self.assertNotIn("Error", result, "OutlineCreator encountered an error.")
        except Exception as e:
            self.fail(f"Outline Creator task execution failed with error: {str(e)}")

    def test_setting_builder_communication(self):
        """Test if SettingBuilder agent can communicate with the model."""
        try:
            task = Task(
                description="Introduce yourself.",
                agent=self.crew.setting_builder(),
                expected_output="A concise introduction from the Setting Builder agent"
            )
            result = task.run()
            self.assertNotEqual(result, "", "SettingBuilder failed to communicate with the model.")
            self.assertNotIn("Error", result, "SettingBuilder encountered an error.")
        except Exception as e:
            self.fail(f"Setting Builder task execution failed with error: {str(e)}")

    def test_character_creator_communication(self):
        """Test if CharacterCreator agent can communicate with the model."""
        try:
            task = Task(
                description="Introduce yourself.",
                agent=self.crew.character_creator(),
                expected_output="A concise introduction from the Character Creator agent"
            )
            result = task.run()
            self.assertNotEqual(result, "", "CharacterCreator failed to communicate with the model.")
            self.assertNotIn("Error", result, "CharacterCreator encountered an error.")
        except Exception as e:
            self.fail(f"Character Creator task execution failed with error: {str(e)}")

    def test_relationship_architect_communication(self):
        """Test if RelationshipArchitect agent can communicate with the model."""
        try:
            task = Task(
                description="Introduce yourself.",
                agent=self.crew.relationship_architect(),
                expected_output="A concise introduction from the Relationship Architect agent"
            )
            result = task.run()
            self.assertNotEqual(result, "", "RelationshipArchitect failed to communicate with the model.")
            self.assertNotIn("Error", result, "RelationshipArchitect encountered an error.")
        except Exception as e:
            self.fail(f"Relationship Architect task execution failed with error: {str(e)}")

    def test_plot_agent_communication(self):
        """Test if PlotAgent can communicate with the model."""
        try:
            task = Task(
                description="Introduce yourself.",
                agent=self.crew.plot_agent(),
                expected_output="A concise introduction from the Plot agent"
            )
            result = task.run()
            self.assertNotEqual(result, "", "PlotAgent failed to communicate with the model.")
            self.assertNotIn("Error", result, "PlotAgent encountered an error.")
        except Exception as e:
            self.fail(f"Plot Agent task execution failed with error: {str(e)}")

    def test_writer_communication(self):
        """Test if Writer agent can communicate with the model."""
        try:
            task = Task(
                description="Introduce yourself.",
                agent=self.crew.writer(),
                expected_output="A concise introduction from the Writer agent"
            )
            result = task.run()
            self.assertNotEqual(result, "", "Writer failed to communicate with the model.")
            self.assertNotIn("Error", result, "Writer encountered an error.")
        except Exception as e:
            self.fail(f"Writer task execution failed with error: {str(e)}")

    def test_editor_communication(self):
        """Test if Editor agent can communicate with the model."""
        try:
            task = Task(
                description="Introduce yourself.",
                agent=self.crew.editor(),
                expected_output="A concise introduction from the Editor agent"
            )
            result = task.run()
            self.assertNotEqual(result, "", "Editor failed to communicate with the model.")
            self.assertNotIn("Error", result, "Editor encountered an error.")
        except Exception as e:
            self.fail(f"Editor task execution failed with error: {str(e)}")

    def test_critic_communication(self):
        """Test if Critic agent can communicate with the model."""
        try:
            task = Task(
                description="Introduce yourself.",
                agent=self.crew.critic(),
                expected_output="A concise introduction from the Critic agent"
            )
            result = task.run()
            self.assertNotEqual(result, "", "Critic failed to communicate with the model.")
            self.assertNotIn("Error", result, "Critic encountered an error.")
        except Exception as e:
            self.fail(f"Critic task execution failed with error: {str(e)}")

    def test_reviser_communication(self):
        """Test if Reviser agent can communicate with the model."""
        try:
            task = Task(
                description="Introduce yourself.",
                agent=self.crew.reviser(),
                expected_output="A concise introduction from the Reviser agent"
            )
            result = task.run()
            self.assertNotEqual(result, "", "Reviser failed to communicate with the model.")
            self.assertNotIn("Error", result, "Reviser encountered an error.")
        except Exception as e:
            self.fail(f"Reviser task execution failed with error: {str(e)}")

    def test_memory_keeper_communication(self):
        """Test if MemoryKeeper agent can communicate with the model."""
        try:
            task = Task(
                description="Introduce yourself.",
                agent=self.crew.memory_keeper(),
                expected_output="A concise introduction from the Memory Keeper agent"
            )
            result = task.run()
            self.assertNotEqual(result, "", "MemoryKeeper failed to communicate with the model.")
            self.assertNotIn("Error", result, "MemoryKeeper encountered an error.")
        except Exception as e:
            self.fail(f"Memory Keeper task execution failed with error: {str(e)}")

    def test_item_developer_communication(self):
        """Test if ItemDeveloper agent can communicate with the model."""
        try:
            task = Task(
                description="Introduce yourself.",
                agent=self.crew.item_developer(),
                expected_output="A concise introduction from the Item Developer agent"
            )
            result = task.run()
            self.assertNotEqual(result, "", "ItemDeveloper failed to communicate with the model.")
            self.assertNotIn("Error", result, "ItemDeveloper encountered an error.")
        except Exception as e:
            self.fail(f"Item Developer task execution failed with error: {str(e)}")

    def test_researcher_communication(self):
        """Test if Researcher agent can communicate with the model."""
        try:
            task = Task(
                description="Introduce yourself.",
                agent=self.crew.researcher(),
                expected_output="A concise introduction from the Researcher agent"
            )
            result = task.run()
            self.assertNotEqual(result, "", "Researcher failed to communicate with the model.")
            self.assertNotIn("Error", result, "Researcher encountered an error.")
        except Exception as e:
            self.fail(f"Researcher task execution failed with error: {str(e)}")

if __name__ == '__main__':
    unittest.main()