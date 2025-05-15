from pydantic import BaseModel

class CafeBase(BaseModel):
    name: str
    city: str
    has_wifi: bool = False
    rating: int

class CafeCreate(CafeBase):
    pass

class Cafe(CafeBase):
    """
    Represents a Cafe entity that extends the base schema `CafeBase`.
    Attributes:
        id (int): A unique identifier for the cafe.
    Config:
        model_config (dict): Configuration for the model. The `from_attributes` key
            is set to `True`, enabling the model to be populated from attributes.
    """
    id: int

    class Config:
        model_config = {
                        'from_attributes': True # This allows the model to be populated from attributes
                                                 # This is useful when using the model with ORMs or other libraries  
                    }
