from ariadne import graphql_sync, make_executable_schema, ObjectType, load_schema_from_path
from ariadne.constants import PLAYGROUND_HTML
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Define Pydantic models
class User(BaseModel):
    id: int
    name: str
    email: str

class Post(BaseModel):
    id: int
    title: str
    content: str
    author_id: int

# Define SQLAlchemy database
engine = create_engine('sqlite:///example.db')
Base = declarative_base()

class UserTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class PostTable(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Define GraphQL schema
type_defs = """
    type Query {
        user(id: ID!): User
        users(limit: Int, offset: Int): [User]
        post(id: ID!): Post
        posts(limit: Int, offset: Int): [Post]
    }

    type Mutation {
        createUser(name: String!, email: String!): User
        createPost(title: String!, content: String!, authorId: ID!): Post
    }

    type User {
        id: ID!
        name: String!
        email: String!
        posts: [Post]
    }

    type Post {
        id: ID!
        title: String!
        content: String!
        author: User!
    }
"""

query = ObjectType("Query")
mutation = ObjectType("Mutation")

@query.field("user")
def resolve_user(_, info, id):
    user = session.query(UserTable).get(id)
    return User(id=user.id, name=user.name, email=user.email)

@query.field("users")
def resolve_users(_, info, limit, offset):
    users = session.query(UserTable).limit(limit).offset(offset).all()
    return [User(id=user.id, name=user.name, email=user.email) for user in users]

@query.field("post")
def resolve_post(_, info, id):
    post = session.query(PostTable).get(id)
    return Post(id=post.id, title=post.title, content=post.content, author_id=post.author_id)

@mutation.field("createUser")
def resolve_create_user(_, info, name, email):
    user = UserTable(name=name, email=email)
    session.add(user)
    session.commit()
    return User(id=user.id, name=user.name, email=user.email)

@mutation.field("createPost")
def resolve_create_post(_, info, title, content, author_id):
    post = PostTable(title=title, content=content, author_id=author_id)
    session.add(post)
    session.commit()
    return Post(id=post.id, title=post.title, content=post.content, author_id=post.author_id)

schema = make_executable_schema(type_defs, query, mutation)

# Create FastAPI app
app = FastAPI()

# Define GraphQL endpoint
@app.post("/graphql")
async def graphql(query: str):
    success, result = graphql_sync(
        schema,
        query,
        context_value={},
        debug=True
    )

    if success:
        return result
    else:
        return {"errors": result}

# Define GraphQL playground endpoint
@app.get("/graphql")
async def graphql_playground():
    return HTMLResponse(PLAYGROUND_HTML, status_code=200)

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)