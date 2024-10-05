from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)

# SQLite database engine (for demonstration)
engine = create_engine('sqlite:///example.db')

# Create tables
Base.metadata.create_all(engine)

# Session factory
Session = sessionmaker(bind=engine)


from flask import Flask
from flask_graphql import GraphQLView
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import User, Post, Session

# SQLAlchemy to GraphQL type mappings
class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)

class PostType(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (graphene.relay.Node,)

# GraphQL Queries
class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_posts = graphene.List(PostType)

    def resolve_all_users(self, info):
        session = Session()
        return session.query(User).all()

    def resolve_all_posts(self, info):
        session = Session()
        return session.query(Post).all()

# GraphQL Mutations
class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(lambda: UserType)

    def mutate(self, info, username, email):
        session = Session()
        user = User(username=username, email=email)
        session.add(user)
        session.commit()
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

# GraphQL Schema
schema = graphene.Schema(query=Query, mutation=Mutation)

# Flask app setup
app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enable GraphiQL interface for interactive queries
    )
)

if __name__ == '__main__':
    app.run(debug=True)

