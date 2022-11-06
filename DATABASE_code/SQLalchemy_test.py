from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel

SQL_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQL_URL, echo=True, connect_args={"check_same_thread": False})
SessionLacol = sessionmaker(autocommit=False, autoFlush=False, bind=engine)

Base = declarative_base()

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, index=True)
  is_active=Column(Boolean, default=True)

class UserCreate(BaseModel):
  email: str
  class Config:
    orm_model=True

data = {
  "email":"tes2112@test.com",
}
user = UserCreate(**data)
print(user.email)

def create_users(db:Session, user: UserCreate):
  filtered_user = db.execute(select(User).filter(User.email==user.email)).scalarts().first()
  if filtered_user==None:
    db_user = User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
  else:
    print(f"'{filtered_user.email}' Exist email !!")

Base.metadata.create_all(bind=engine)
db = SessionLacol()
result = create_users(db = db, user = user)

result.email
db.close()
