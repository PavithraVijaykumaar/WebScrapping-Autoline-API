from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np
app = FastAPI()
df = pd.read_csv("C:/Users/TIGER/.spyder-py3/WEBSCRAPPING-API/ford.csv")
@app.get("/data")
async def get_data():
    # Handle NaN and Infinity values in the DataFrame
    df_cleaned = df.replace([np.nan, np.inf, -np.inf], np.finfo(np.float64).max)

    try:
        return JSONResponse(content=df_cleaned.to_dict(orient="records"))
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)