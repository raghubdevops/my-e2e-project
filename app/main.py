from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Raghu's E2E project!"}


@app.get("/health")
def health():
    return {"status": "ok"}