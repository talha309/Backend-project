from fastapi import FastAPI
from routes.login_router import router  
# from routes.student_router import router as student_router

app = FastAPI()

@app.get("/")
def fastapi():
    return {"message": "Welcome to API"}  

# Mount login routes here
app.include_router(router, prefix="/login", tags=["Login"])
# app.include_router(student_router, prefix="/student", tags=["Student"])