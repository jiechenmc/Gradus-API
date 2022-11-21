from fastapi import Query

QUERY = Query(default=...)

FIELD = Query(default="section",
              regex=r"^(section|term|courseTitle|instructor)$")

TERM = Query(default="Spring 2022",
             regex=r"^(Fall|Spring|Summer|Winter) (\d{4})$")