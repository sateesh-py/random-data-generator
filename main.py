from fastapi import FastAPI
from fastapi.responses import RedirectResponse,JSONResponse
import uvicorn
from datagen import generate_data,simple_random_data,generate_data_1

app = FastAPI()


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.get('/data')
async def random_data():
    return JSONResponse(generate_data_1(),media_type="Application/json; charset=utf-8")

@app.get('/v2/random-data')
def random_data():
    return JSONResponse(generate_data(),media_type="Application/json; charset=utf-8")

@app.get('/v2/random/data')
def small_random_data():
    return JSONResponse(simple_random_data(),media_type="Application/json; charset=utf-8")


if __name__ == '__main__':
    uvicorn.run(app)
