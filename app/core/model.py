from pydantic import BaseModel


class Record(BaseModel):
    Section: str
    Term: str
    Course_Title: str
    Instructors: str
    Grades: str

    class Config:
        schema_extra = {
            "example": {
                "Section": "CSE214-01",
                "Term": "Fall 2021",
                "Course Title": "DATA STRUCTURES",
                "Instructors": "Ahmad Esmaili",
                "Grades": {
                    "A": 19,
                    "B": 16,
                    "C": 1,
                    "D": 1,
                    "F": 0
                },
            }
        }


class Term(BaseModel):

    class Config:
        schema_extra = {
            "example":
            {"Spring 2022", "Summer 2022", "Winter 2022", "Fall 2021"}
        }