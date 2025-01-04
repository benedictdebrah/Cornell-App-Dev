# DEMO API Documentation

## Overview
This Tasks API allows users to manage a list of tasks, including creating, reading, updating, and deleting tasks. The API is implemented using FastAPI.

### Base URL
```
http://<your-server-host>/
```

## Endpoints

### General
#### `GET /`
- **Description**: Returns a welcome message.
- **Response**:
  ```json
  {
    "Message": "This is the Demo CRUD API"
  }
  ```

---

### Tasks

#### `GET /tasks`
- **Description**: Retrieves a dictionary of all tasks.
- **Response**:
  ```json
  {
    "1": {
      "id": 1,
      "description": "wash the laundry",
      "status": "not started"
    },
    "2": {
      "id": 2,
      "description": "clean the car",
      "status": "not started"
    }
  }
  ```

#### `GET /tasks/{task_id}`
- **Description**: Retrieves a specific task by its ID.
- **Path Parameters**:
  - `task_id` (int): ID of the task.
- **Response** (Success):
  ```json
  {
    "id": 1,
    "description": "wash the laundry",
    "status": "not started"
  }
  ```
- **Response** (Error):
  ```json
  {
    "detail": "Task not found"
  }
  ```

#### `POST /tasks`
- **Description**: Creates a new task.
- **Request Body**:
  ```json
  {
    "description": "New task description"
  }
  ```
- **Response**:
  ```json
  {
    "id": 3,
    "description": "New task description",
    "status": "not started"
  }
  ```

#### `PUT /tasks/{task_id}`
- **Description**: Updates an existing task.
- **Path Parameters**:
  - `task_id` (int): ID of the task to update.
- **Request Body**:
  ```json
  {
    "description": "Updated description",
    "status": "in progress"
  }
  ```
- **Response** (Success):
  ```json
  {
    "id": 1,
    "description": "Updated description",
    "status": "in progress"
  }
  ```
- **Response** (Error):
  ```json
  {
    "detail": "Task not found"
  }
  ```

#### `DELETE /tasks/{task_id}`
- **Description**: Deletes a task by its ID.
- **Path Parameters**:
  - `task_id` (int): ID of the task to delete.
- **Response** (Success):
  ```json
  {
    "message": "Task deleted successfully"
  }
  ```
- **Response** (Error):
  ```json
  {
    "detail": "Task not found"
  }
  ```

---

## Notes
- All endpoints return errors with appropriate HTTP status codes and error messages.
- Task IDs are unique and auto-incremented when a new task is created.
- Use JSON format for all request bodies.

## Status Codes
- **200 OK**: Request was successful.
- **201 Created**: Resource was successfully created.
- **404 Not Found**: Resource not found.

## Example Usage
### Creating a Task
**Request**:
```
POST /tasks
```
**Body**:
```json
{
  "description": "New task description"
}
```
**Response**:
```json
{
  "id": 3,
  "description": "New task description",
  "status": "not started"
}
```

### Updating a Task
**Request**:
```
PUT /tasks/1
```
**Body**:
```json
{
  "description": "Updated description",
  "status": "completed"
}
```
**Response**:
```json
{
  "id": 1,
  "description": "Updated description",
  "status": "completed"
}
```

