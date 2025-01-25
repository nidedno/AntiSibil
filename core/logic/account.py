
import json

# Accounts entry.
# Contains account and all info which it can contains.
class Account:
    def __init__(self, name, **fields):
        self.name = name
        self.fields = fields

    def update_field(self, field_name, field_value):
        self.fields[field_name] = field_value

    def to_dict(self):
        return {"name": self.name, **self.fields}
    
    # return true/false that fields exists in dict.
    def contains_feield(self, field):
        return field in self.fields

    # get fields
    def get(self, field):
        if self.contains_feield(field) == False:
            raise "Account {0} not contains field {1}".format(self.name, field)

        return self.fields[field]

    # Conver json data to account
    @staticmethod
    def from_dict(data):
        name = data.pop("name", None)
        return Account(name, **data)
    
    @staticmethod
    def to_dict(account):
        return False