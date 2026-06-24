from app.db.session import get_db
from app.services.task import TaskService
from sqlalchemy.orm import Session 
from fastapi import Depends

def get_task_service(db: Session = Depends(get_db)): 
    return TaskService(db)