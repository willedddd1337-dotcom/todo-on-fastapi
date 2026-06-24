
from sqlalchemy import select 
from app.models.task import TaskOrm 
from sqlalchemy.orm import Session 

class TaskRepository: 
    def __init__(self, db: Session): 
        self.db = db 

    def get_all(self) -> list[TaskOrm]: 
        return self.db.scalars(select(TaskOrm)).all()
    
    def get_by_id(self, task_id: str): 
        return self.db.get(TaskOrm, task_id)
    
    def create(self, title: str) -> TaskOrm: 
        new_task = TaskOrm(title=title, completed=False)

        self.db.add(new_task)

        return new_task

    def delete(self, TaskOrm) -> None: 
        self.db.delete(TaskOrm)