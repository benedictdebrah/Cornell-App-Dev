from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas, auth
from database import get_db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

UserRouter = APIRouter()



# OAuth2 password bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@UserRouter.post("/register", response_model=schemas.UserResponse, tags=["Users"])
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return auth.create_user(db=db, user=user)


@UserRouter.post("/login", tags=["Users"])
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.get_user(db, form_data.username)
    if not user or not auth.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


