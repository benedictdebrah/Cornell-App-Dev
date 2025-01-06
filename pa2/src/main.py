from fastapi import FastAPI, Depends, HTTPException, status
from routes.users import UserRouter



app = FastAPI()

app.include_router(UserRouter)
