from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return "qqqq"


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
