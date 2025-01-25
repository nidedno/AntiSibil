
import json
from ..shared.constants import ACCOUNTS_FOLDER

# Accounts entry.
# Contains account and all info which it can contains.
class Account:
    def __init__(self, name, fields):
        print(name, fields)
        self.name = name
        self.fields = fields

    def update_field(self, field_name, field_value):
        self.fields[field_name] = field_value

    def to_dict(self):
        return {"name": self.name, **self.fields}
    
    # return true/false that fields exists in dict.
    def contains_field(self, field):
        return field in self.fields.keys()

    # get fields
    def get(self, field):
        if self.contains_field(field) == False:
            raise Exception("Account {0} not contains field {1}".format(self.name, field))

        return self.fields[field]

    # Conver json data to account
    @staticmethod
    def from_dict(data):
        name = data.get("filename", "No_Name")
        return Account(name, data)
    
    def save(self):
        with open(ACCOUNTS_FOLDER + self.name + ".json", 'w') as f:
            json.dump(self.fields, f)