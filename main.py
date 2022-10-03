from pydantic import BaseModel
from fastapi import FastAPI
from datetime import datetime as dt

COUNT = {'GET': 0, 'POST': 0}

class Date(BaseModel):
    parameter: bool

tags_metadata = [
    {
        "name": "Get date",
        "description": "For a boolean parameter gets the date in different formats. "
                       "The *parameter* to be given is in json format (check request body in documentation),"
                       " change the value to **true** or **false** in order to get different responses.",
    },
    {
        "name": "Count",
        "description": "Counts the amount of times an endpoint has been called. Give the *parameter*"
                       " the values **POST** or **GET** to specify the endpoint",
    },
]
app = FastAPI(title="Marvik API Test", openapi_tags=tags_metadata)


@app.post("/", tags=["Get date"])
async def get_date(text: Date):
    actual_date = dt.now()
    COUNT['POST'] += 1
    if (text.parameter is True):
        return {"Response": actual_date.strftime("%Y-%m-%d %H:%M:%S")}
    else:
        return {'Response': actual_date.strftime("%Y-%d-%m")}


@app.get("/", tags=["Count"])
def read_param(parameter):
    COUNT['GET'] += 1
    return {'Response': COUNT[parameter]}
