from pydantic import BaseModel, Field, computed_field
from typing import Literal

class Patient(BaseModel):
    id: str
    name: str
    city: str
    age: int = Field(gt=0, lt=120)
    gender: Literal['male', 'female', 'others']
    height: float = Field(gt=0)
    weight: float = Field(gt=0)

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
