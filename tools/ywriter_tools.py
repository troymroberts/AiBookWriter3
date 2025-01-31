import json
import os
from typing import Optional
from uuid import uuid4

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from pywriter.model.chapter import Chapter
from pywriter.model.project_note import ProjectNote
from pywriter.model.scene import Scene
from pywriter.yw.yw7_file import Yw7File

# Helper function to load a yWriter 7 project
def load_yw7_file(file_path: str) -> Yw7File:
    """
    Loads a yWriter 7 project file.

    Args:
        file_path (str): The path to the .yw7 file.

    Returns:
        Yw7File: The loaded yWriter 7 project.
    """

    yw7_file = Yw7File(file_path)
    yw7_file.read()
    return yw7_file

# --- Tools for reading data ---

class ReadProjectNotesInput(BaseModel):
    yw7_path: str = Field(..., description="The path to the .yw7 file.")

class ReadProjectNotesTool(BaseTool):
    name: str = "Read Project Notes"
    description: str = "Read project notes from a yWriter 7 project file."
    args_schema: type[BaseModel] = ReadProjectNotesInput

    def _run(self, yw7_path: str, **kwargs) -> str:
        """Reads and returns project notes."""
        yw7_file = load_yw7_file(yw7_path)
        notes = yw7_file.novel.projectNotes
        return "\n".join(
            f"Title: {note.title}\nDescription: {note.desc}"
            for note in notes.values()
        )

class ReadCharactersInput(BaseModel):
    yw7_path: str = Field(..., description="Path to the .yw7 file")

class ReadCharactersTool(BaseTool):
    name: str = "Read Characters"
    description: str = "Read character data from a yWriter 7 project file."
    args_schema: type[BaseModel] = ReadCharactersInput

    def _run(self, yw7_path: str, **kwargs) -> str:
        yw7_file = load_yw7_file(yw7_path)
        characters = yw7_file.novel.characters
        return "\n".join(
            f"ID: {char.id}, Name: {char.title}, Description: {char.desc}"
            for char in characters.values()
        )

class ReadLocationsInput(BaseModel):
    yw7_path: str = Field(..., description="Path to the .yw7 file")

class ReadLocationsTool(BaseTool):
    name: str = "Read Locations"
    description: str = "Read location data from a yWriter 7 project file."
    args_schema: type[BaseModel] = ReadLocationsInput

    def _run(self, yw7_path: str, **kwargs) -> str:
        yw7_file = load_yw7_file(yw7_path)
        locations = yw7_file.novel.locations
        return "\n".join(
            f"ID: {loc.id}, Name: {loc.title}, Description: {loc.desc}"
            for loc in locations.values()
        )

class ReadOutlineInput(BaseModel):
    yw7_path: str = Field(..., description="Path to the .yw7 file")
    chapter_id: Optional[str] = Field(
        None, description="Optional ID of a specific chapter to read"
    )

class ReadOutlineTool(BaseTool):
    name: str = "Read Outline"
    description: str = "Read chapter outlines from a yWriter 7 project file."
    args_schema: type[BaseModel] = ReadOutlineInput

    def _run(self, yw7_path: str, chapter_id: Optional[str] = None, **kwargs) -> str:
        yw7_file = load_yw7_file(yw7_path)
        output = ""
        for ch_id, chapter in yw7_file.novel.chapters.items():
            if chapter_id is None or ch_id == chapter_id:
                output += f"Chapter ID: {ch_id}, Title: {chapter.title}\n"
                if chapter.desc:
                    output += f"Description: {chapter.desc}\n"
                if "outline" in chapter.kwVar:
                    output += f"Outline: {chapter.kwVar['outline']}\n"
                output += "\n"
        return output

class ReadSceneInput(BaseModel):
    yw7_path: str = Field(..., description="Path to the .yw7 file")
    scene_id: str = Field(..., description="ID of the scene to read")

class ReadSceneTool(BaseTool):
    name: str = "Read Scene"
    description: str = "Read the content of a specific scene from a yWriter 7 project file."
    args_schema: type[BaseModel] = ReadSceneInput

    def _run(self, yw7_path: str, scene_id: str, **kwargs) -> str:
        yw7_file = load_yw7_file(yw7_path)
        if scene_id in yw7_file.novel.scenes:
            scene = yw7_file.novel.scenes[scene_id]
            return scene.sceneContent or "Content not found."
        return "Scene not found."

# --- Tools for writing data ---

class WriteProjectNoteInput(BaseModel):
    yw7_path: str = Field(..., description="Path to the .yw7 file")
    title: str = Field(..., description="Title of the project note")
    content: str = Field(..., description="Content of the project note")

class WriteProjectNoteTool(BaseTool):
    name: str = "Write Project Note"
    description: str = "Write a project note to a yWriter 7 project file."
    args_schema: type[BaseModel] = WriteProjectNoteInput

    def _run(self, yw7_path: str, title: str, content: str, **kwargs) -> str:
        yw7_file = load_yw7_file(yw7_path)
        note_id = str(uuid4())
        project_note = ProjectNote(ID=note_id)
        project_note.title = title
        project_note.desc = content
        yw7_file.novel.projectNotes[note_id] = project_note
        yw7_file.write()
        return f"Project note '{title}' written successfully."

class CreateChapterInput(BaseModel):
    yw7_path: str = Field(..., description="Path to the .yw7 file")
    title: str = Field(..., description="Title of the new chapter")
    description: Optional[str] = Field(None, description="Description of the chapter")

class CreateChapterTool(BaseTool):
    name: str = "Create Chapter"
    description: str = "Create a new chapter in a yWriter 7 project file."
    args_schema: type[BaseModel] = CreateChapterInput

    def _run(
        self, yw7_path: str, title: str, description: Optional[str] = None, **kwargs
    ) -> str:
        yw7_file = load_yw7_file(yw7_path)
        chapter_id = str(uuid4())
        chapter = Chapter(ID=chapter_id)
        chapter.title = title
        chapter.desc = description
        yw7_file.novel.chapters[chapter_id] = chapter
        yw7_file.novel.srtChapters.append(chapter_id)
        yw7_file.write()
        return f"Chapter '{title}' created successfully with ID: {chapter_id}"

# Writing the Scene Content
class WriteSceneContentInput(BaseModel):
    yw7_path: str = Field(..., description="Path to the .yw7 file")
    scene_id: str = Field(..., description="ID of the scene to write to")
    content: str = Field(..., description="Content to write to the scene")

class WriteSceneContentTool(BaseTool):
    name: str = "Write Scene Content"
    description: str = "Write content to a specific scene in a yWriter 7 project file."
    args_schema: type[BaseModel] = WriteSceneContentInput

    def _run(self, yw7_path: str, scene_id: str, content: str, **kwargs) -> str:
        yw7_file = load_yw7_file(yw7_path)
        if scene_id in yw7_file.novel.scenes:
            scene = yw7_file.novel.scenes[scene_id]
            scene.sceneContent = content
            yw7_file.write()
            return f"Content written to scene '{scene_id}' successfully."
        return "Scene not found."