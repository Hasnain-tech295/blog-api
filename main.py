from fastapi import FastAPI

app = FastAPI()        # used to define all of our routes and endpoints

@app.get("/")
def home():
    return {"message": "Welcome to the Blog API"}