# Reddit API Documentation

## Overview
The Reddit API provides endpoints to manage posts and comments. Users can perform CRUD (Create, Read, Update, Delete) operations on posts and comments. The API is built using FastAPI.

### Base URL
```
http://<your-server-host>/
```

## Endpoints

### General
#### `GET /`
- **Description**: Returns a simple welcome message.
- **Response**:
  ```json
  {
    "Hello": "World"
  }
  ```

---

### Posts

#### `GET /api/posts`
- **Description**: Retrieves all posts.
- **Response**:
  ```json
  {
    "posts": [
      {
        "id": 1,
        "upvotes": 1,
        "title": "First post",
        "link": "https://www.reddit.com",
        "username": "TestUser1"
      },
      ...
    ]
  }
  ```

#### `GET /api/posts/{post_id}`
- **Description**: Retrieves a specific post by ID.
- **Path Parameters**:
  - `post_id` (int): ID of the post.
- **Response** (Success):
  ```json
  {
    "id": 1,
    "upvotes": 1,
    "title": "First post",
    "link": "https://www.reddit.com",
    "username": "TestUser1"
  }
  ```
- **Response** (Error):
  ```json
  {
    "detail": "Post not found"
  }
  ```

#### `POST /api/posts`
- **Description**: Creates a new post.
- **Request Body**:
  ```json
  {
    "title": "Post title",
    "link": "https://example.com",
    "username": "UserName"
  }
  ```
- **Response**:
  ```json
  {
    "id": 4,
    "upvotes": 0,
    "title": "Post title",
    "link": "https://example.com",
    "username": "UserName"
  }
  ```

#### `DELETE /api/posts/{post_id}`
- **Description**: Deletes a specific post by ID.
- **Path Parameters**:
  - `post_id` (int): ID of the post to delete.
- **Response** (Success):
  ```json
  {
    "id": 1,
    "upvotes": 1,
    "title": "First post",
    "link": "https://www.reddit.com",
    "username": "TestUser1"
  }
  ```
- **Response** (Error):
  ```json
  {
    "detail": "Post not found"
  }
  ```

---

### Comments

#### `GET /api/posts/{id}/comments`
- **Description**: Retrieves comments for a specific post by ID.
- **Path Parameters**:
  - `id` (int): ID of the post.
- **Response** (Success):
  ```json
  {
    "id": 1,
    "upvotes": 1,
    "username": "TestUser1",
    "comment": "This is a comment"
  }
  ```
- **Response** (Error):
  ```json
  {
    "detail": "Comments not found"
  }
  ```

#### `POST /api/posts/{id}/comments`
- **Description**: Creates a new comment for a specific post.
- **Path Parameters**:
  - `id` (int): ID of the post.
- **Request Body**:
  ```json
  {
    "comment": "This is a comment",
    "username": "UserName"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "upvotes": 1,
    "comment": "This is a comment",
    "username": "UserName"
  }
  ```

#### `PUT /api/posts/{post_id}/comments/{id}`
- **Description**: Updates a specific comment for a post.
- **Path Parameters**:
  - `post_id` (int): ID of the post.
  - `id` (int): ID of the comment.
- **Request Body**:
  ```json
  {
    "comment": "Updated comment",
    "username": "UserName"
  }
  ```
- **Response** (Success):
  ```json
  {
    "id": 1,
    "upvotes": 1,
    "comment": "Updated comment",
    "username": "UserName"
  }
  ```
- **Response** (Error):
  ```json
  {
    "detail": "Comment not found"
  }
  ```

---

## Notes
- All endpoints return errors with appropriate HTTP status codes and error messages.
- For creating or updating resources, provide the request body in JSON format.

## Status Codes
- **200 OK**: Request was successful.
- **201 Created**: Resource was successfully created.
- **404 Not Found**: Resource not found.

## Example Usage
### Creating a Post
**Request**:
```
POST /api/posts
```
**Body**:
```json
{
  "title": "New Post",
  "link": "https://example.com",
  "username": "NewUser"
}
```
**Response**:
```json
{
  "id": 4,
  "upvotes": 0,
  "title": "New Post",
  "link": "https://example.com",
  "username": "NewUser"
}
```

