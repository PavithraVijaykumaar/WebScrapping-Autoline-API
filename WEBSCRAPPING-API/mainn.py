from fastapi import FastAPI
from fastapi.responses import JSONResponse
import csv
import pandas as pd
import numpy as np
app = FastAPI()
@app.get("/data")
async def get_data():
    with open(
        "ford.csv",
        newline="",
        encoding="utf-8",
    ) as csvfile:
        data = list(csv.DictReader(csvfile))
        return data