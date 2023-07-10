import os
from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.core.model import Record, Term
from app.core.query import QUERY, TERM, FIELD
from app.core.utility import find
from typing import List

load_dotenv()
client = MongoClient(os.getenv("mongo_url"))
db = client.get_database(os.getenv("mongo_db"))

description = """
Gradus 🚀
## Introduction
You will be able to:
* **Obtain grade distribution data for classes** 
* **Data for all semesters will be available soon!** 
"""

app = FastAPI(
    title="Gradus",
    description=description,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


@app.get("/api/meta/", response_model=Term)
async def get_supported_terms():
    return JSONResponse(db.list_collection_names())


@app.get("/api/all/", response_model=list[Record])
async def get_all_data(query: str = QUERY, field: str = FIELD):
    result = []

    for collection in db.list_collection_names():
        result.extend(find(db.get_collection(collection), field, query))

    return JSONResponse(result)


@app.get("/api/class", response_model=list[Record])
async def get_class_by_instructor(query: str = QUERY, instructor: str = None):
    all_classes_by_ins = []

    for collection in db.list_collection_names():
        all_classes_by_ins.extend(
            find(db.get_collection(collection), "instructor", instructor))

    class_by_ins = [x for x in all_classes_by_ins if query in x["section"]]

    return JSONResponse(class_by_ins)


@app.get("/api/instructor/class", response_model=list[Record])
async def get_all_class_by_instructor(instructor: str = QUERY):
    all_classes_by_ins = []

    for collection in db.list_collection_names():
        all_classes_by_ins.extend(
            find(db.get_collection(collection), "instructor", instructor))

    return JSONResponse(all_classes_by_ins)


@app.get("/api/term/", response_model=list[Record])
async def get_data_by_term(query: str = QUERY,
                           field: str = FIELD,
                           term: str = TERM):
    return JSONResponse(find(db.get_collection(term), field, query))