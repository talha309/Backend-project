from fastapi import FastAPI
from routes.login_router import router  

app = FastAPI()

@app.get("/")
def fastapi():
    return {"message": "Welcome to API"}  

# Mount login routes here
app.include_router(router, prefix="/login", tags=["Login"])
