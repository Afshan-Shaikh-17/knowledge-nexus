from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Hello World!"}


if __name__=='__main__':
    uvicorn.run(
        "main:app",  # Module name : FastAPI app object
        host="127.0.0.1",
        port=8000,
        reload=True  # Auto-reload when code changes
    )