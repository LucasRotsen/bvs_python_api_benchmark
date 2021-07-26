import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.config import ALLOWED_ORIGINS

app = FastAPI(
    title='QuizApp API',
    description='RESTful API for Quiz / Trivia management',
    version='0.0.1',
    docs_url='/documentation',
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=ALLOWED_ORIGINS
)


@app.get("/{name}")
def hello_name(name: str):
    return f"Hello, {name}!"


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
