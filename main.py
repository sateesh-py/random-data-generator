from fastapi import FastAPI
import uvicorn
from datagen import generate_data

app = FastAPI()


@app.get('/v2/random-data')
def random_data():
    return generate_data()


if __name__ == '__main__':
    uvicorn.run(app)
