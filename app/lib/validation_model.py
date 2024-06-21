from dataclasses import dataclass

@dataclass
class AttributeModel:
    name: str
    type: str
    validation: str
    is_mandatory:bool

    def __init__(self, name:str, validation:str, is_mandatory:bool=False):
        self.name = name
        self.type = self.name.upper()
        self.validation = validation
        self.is_mandatory = is_mandatory
    
@dataclass
class RecordModel:
    record_model: str
    type: str
    attributes:list[AttributeModel]
    def __init__(self, record_model:str, attributes:list[AttributeModel]):
        self.record_model = record_model
        self.type = self.record_model.upper()
        self.attributes = attributes
