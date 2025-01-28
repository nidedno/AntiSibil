
import json
from ..shared.constants import PROJECTS_FOLDER
from enum import Enum

class ProjectStatus(Enum):
    NO_STARTED = 0
    IN_PROGRESS = 1
    FINISHED = 2

class Project:
    def __init__(self, name, description, tag):
        self.name = name
        self.description = description
        self.tag = tag

    def to_dict(self):
        return {"name": self.name, "description": self.description, "tag": self.tag}
    
    # Conver json data to account
    @staticmethod
    def from_dict(data):
        # validation
        name = data["name"]
        description = data["description"]
        tag = data['tag']

        return Project(name, description, tag) 
    
    def save(self):
        with open(PROJECTS_FOLDER + self.name + ".json", 'w') as f:
            json.dump(self.fields, f)