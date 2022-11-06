from fastapi import Query

QUERY = Query(default=..., )

FIELD = Query(default="Section",
              regex=r"^(Section|Term|Course Title|Instructors)")

TERM = Query(default="Fall 2022",
             regex=r"^(Fall|Spring|Summer|Winter) (\d{4})$")