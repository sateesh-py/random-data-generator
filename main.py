from fastapi import FastAPI
from fastapi.responses import RedirectResponse,JSONResponse
import uvicorn
from datagen import generate_data,simple_random_data,generate_data_1,simple_data

app = FastAPI()


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    try:
        return RedirectResponse(url="/docs")
    except Exception as e:
        # Add logging or error handling here
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/data')
async def random_data():
    return JSONResponse(generate_data_1(),media_type="Application/json; charset=utf-8")

@app.get('/v2/random-data')
async def random_data():
    return JSONResponse(generate_data(),media_type="Application/json; charset=utf-8")

@app.get('/v2/random/data')
async def small_random_data():
    return JSONResponse(simple_random_data(),media_type="Application/json; charset=utf-8")

@app.get('/simple/data')
async def simple():
    try:
        return JSONResponse(simple_data(), media_type="application/json; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == '__main__':
    uvicorn.run(app)
