from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class TaskCreate(BaseModel):
    description: str

class Task(BaseModel):
    description: Optional[str] = None 
    status: str



tasks = {
    1: {"id" : 1, "description" :"wash the laundry", "status": "not started"},
    2: {"id" : 2, "description" :"clean the car", "status": "not started"},
}

task_id_count = 2




@app.get("/")
def read_root():
    return {"Message": "This is the Demo CRUD API"}


@app.get("/tasks", status_code=status.HTTP_200_OK)
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]



@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global task_id_count  
    task_id_count += 1  
    tasks[task_id_count] = {
        "id": task_id_count,
        "description": task.description,
        "status": "not started",
    }
    return tasks[task_id_count]


@app.put("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, task : Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.description is not None:
        tasks[task_id]["description"] = task.description

    tasks[task_id]["status"] = task.status

    return tasks[task_id]


@app.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted successfully"}