from fastapi import Query

QUERY = Query(default=...)

FIELD = Query(default="Section",
              regex=r"^(section|term|courseTitle|instructor)$")

TERM = Query(default="Spring 2022",
             regex=r"^(Fall|Spring|Summer|Winter) (\d{4})$")