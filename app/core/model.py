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
                "section": "CSE214-R01",
                "term": "Spring 2022",
                "courseTitle": "DATA STRUCTURES",
                "instructor": "Ahmad Esmaili",
                "grades": {
                    "A": 8,
                    "A-": 1,
                    "B+": 2,
                    "B": 2,
                    "B-": 6,
                    "C+": 3,
                    "C": 1,
                    "C-": 0,
                    "D+": 2,
                    "D": 3,
                    "F": 2,
                    "I": 0,
                    "W": 0
                }
            }
        }


class Term(BaseModel):

    class Config:
        schema_extra = {
            "example":
            {"Spring 2022", "Summer 2022", "Winter 2022", "Fall 2021"}
        }