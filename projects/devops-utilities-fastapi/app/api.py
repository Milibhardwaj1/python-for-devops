from fastapi import FastAPI

app = FastAPI(
    title = "Demo",
    description = "Demo", 
    version = "1.0.0",
    doc_url = "/docs"
)

@app.get("/")
def hello():
    return {"message":"Hello World"}