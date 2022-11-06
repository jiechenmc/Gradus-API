from fastapi import Query
import re

QUERY = Query(default=...)

FIELD = Query(default="Section",
              regex=r"^(Section|Term|Course Title|Instructors)$")

TERM = Query(default="Spring 2022",
             regex=r"^(Fall|Spring|Summer|Winter) (\d{4})$")