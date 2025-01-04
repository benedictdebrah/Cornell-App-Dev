from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel
from typing import List, Optional

reddit_posts = [{
        "id": 1,
        "upvotes": 1,
        "title": "First post",
        "link": "https://www.reddit.com",
        "username": "TestUser1"
    },{
        "id": 2,
        "upvotes": 22,
        "title": "Second post",
        "link": "https://www.reddit.com",
        "username": "TestUser2"
    
    },{
        "id": 3,
        "upvotes": 90,
        "title": "Third post",
        "link": "https://www.reddit.com",
        "username": "TestUser3"
    }

]

reddit_comments = [{
        "id": 1,
        "upvotes": 1,
        "username": "TestUser1",
        "comment": "This is a comment"
    },{
        "id": 2,
        "upvotes": 1,
        "username": "TestUser2",
        "comment": "This is another comment"
    },{
        "id": 3,
        "upvotes": 2,
        "username": "TestUser3",
        "comment": "This is a comment"
    }
]


class Post(BaseModel):
    title: str
    link: str
    username: str

postId = 3


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/posts")
def read_posts():
    return {"posts" : reddit_posts}


@app.get("/api/posts/{post_id}")
def read_post(post_id: int):
    post = next((post for post in reddit_posts if post["id"] == post_id), None)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/api/posts", status_code=201)
def create_post(post : Post):
    global postId
    postId += 1
    new_post = {
        "id": postId,
        "upvotes": 0,
        "title": post.title,
        "link": post.link,
        "username": post.username
    }
    reddit_posts.append(new_post)
    return new_post



@app.delete("/api/posts/{post_id}", status_code=200)
def delete_post(post_id: int):
    global reddit_posts
    post = next((post for post in reddit_posts if post["id"] == post_id), None)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    reddit_posts = [post for post in reddit_posts if post["id"] != post_id]
    return post

@app.get("/api/posts/{id}/comments")
def _get_comments(id: int):
    comments = next((comment for comment in reddit_comments if comment["id"] == id), None)
    if comments is None:
        raise HTTPException(status_code=404, detail="Comments not found")
    return comments

class Comment(BaseModel):
    comment: str
    username: str

commentId = 0

@app.post("/api/posts/{id}/comments", status_code=201)
def create_comment(comment : Comment):
    global commentId
    commentId += 1
    new_comment = {
        "id": commentId,
        "upvotes": 1,
        "comment": comment.comment,
        "username": comment.username
    }
    reddit_comments.append(new_comment)
    return new_comment

@app.put("/api/posts/{post_id}/comments/{id}", status_code=200)
def _edit_comments(post_id: int, id: int, updated_comment: Comment):
    global reddit_comments
    comment = next((comment for comment in reddit_comments if comment["id"] == id), None)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    comment["comment"] = updated_comment.comment
    return comment

